class ResponseStructure():
    def __init__(self, status_code: int, message: str, response_code: str):
        self.status_code = status_code
        self.message = message
        self.response_code = response_code
