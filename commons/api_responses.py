from commons import Response, ResponseStructure
from http import HTTPStatus

class ApiResponse():
    CREATED = ResponseStructure(HTTPStatus.CREATED, "Created.", "LC0200")
    OK = ResponseStructure(HTTPStatus.OK, "Success.", "LC0201")

    BAD_REQUEST = ResponseStructure(HTTPStatus.BAD_REQUEST, "Bad Request.", "LC0400")