from rest_framework.decorators import action
from rest_framework import status
from rest_framework.viewsets import ViewSet
from django.http import JsonResponse
from django.db.models import Count
from lc_api.models import LeetcodeProblemsModel, ContestModel, TagModel
from lc_api.serializers import LCProblemsSerializer, ContestSerializer
from django.core.paginator import InvalidPage, Paginator
from http import HTTPStatus
from math import ceil
from commons import Response, PaginationData, ApiResponse

class LCApi(ViewSet):    
    def get_problems(self, request):
        problems = LeetcodeProblemsModel.objects.all()

        page_number = request.GET.get("page", 1)
        items_per_page = request.GET.get("limit", 10)
        paginator = Paginator(problems, items_per_page)

        try:
            page_data = paginator.page(page_number)
        except InvalidPage as e:
            self.logger.error(
                "Invalid Page. Request Data:{} Errors:{}", request.data, e
            )
            return JsonResponse({"message": "Invalid page."}, status=HTTPStatus.BAD_REQUEST)

        response_serializer = LCProblemsSerializer(
            page_data, many=True)
        pagination_data = PaginationData({
            "count": len(response_serializer.data),
            "pages": ceil(len(response_serializer.data)/items_per_page),
            "next": page_data.has_next(),
            "previous": page_data.has_previous(),
        })

        response_serializer = LCProblemsSerializer(problems, many=True)
        return Response(ApiResponse.OK, data=response_serializer.data, pagination_data=pagination_data)

    def get_contests(self, request):
        contests = ContestModel.objects.all()
        contest_serializer = ContestSerializer(contests, many=True)
        return Response(ApiResponse.OK, data=contest_serializer)
    
    def create_problem(self, request):
        request_serializer = LCProblemsSerializer(data=request.data)
        if not request_serializer.is_valid():
            print(f"Error at request serializer: {request_serializer.errors}")
            return Response(ApiResponse.BAD_REQUEST)
        request_serializer.save()
        return Response(ApiResponse.CREATED, data=request_serializer.validated_data)
    
    def filter_problems(self, request):
        tag_names = request.query_params.getlist('tags', [])
        filter_by_or = request.GET.get('filter_by_or', 'false') == 'true'

        if filter_by_or:
            problems = LeetcodeProblemsModel.objects.filter(tags__name__in=tag_names).distinct()
        else:
            problems = LeetcodeProblemsModel.objects.filter(tags__name__in=tag_names) \
                .annotate(num_tags=Count('tags')) \
                .filter(num_tags=len(tag_names))


        response_serializer = LCProblemsSerializer(problems, many=True)
        return Response(ApiResponse.OK, response_serializer)