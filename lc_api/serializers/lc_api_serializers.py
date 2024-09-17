from rest_framework import serializers
from lc_api.models import LeetcodeProblemsModel, ContestModel, TagModel

class ContestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContestModel
        exclude = ['id']

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = TagModel
        exclude = ['id']

class LCProblemsSerializer(serializers.ModelSerializer):
    contest = ContestSerializer(write_only=True)
    tags = serializers.JSONField(default=list)
    class Meta: 
        model = LeetcodeProblemsModel
        exclude = ["id"]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['tags'] = [tag.name for tag in instance.tags.all()]
        return representation

    def create(self, validated_data):
        contest_data = validated_data.pop('contest')
        contest_number = contest_data.get('contest_number')
        
        contest = ContestModel.objects.filter(contest_number=contest_number).first()
        if not contest:
            contest_serializer = ContestSerializer(data=contest_data)
            contest_serializer.is_valid(raise_exception=True)
            contest = contest_serializer.save()

        tag_list = list(set(validated_data.pop('tags')))
        tags = TagModel.objects.filter(name__in=tag_list)
        if len(tags) == 0:
            raise Exception("No tags.")
    
        instance = LeetcodeProblemsModel.objects.create(contest=contest, **validated_data)
        instance.tags.add(*tags)
        return instance
