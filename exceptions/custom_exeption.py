class CustomException(Exception):
    def __init__(self, message):
        super().__init__(message)

        self.message = message

    def db_error(self):
        error_data = {
            'error': self.error,
            'status_code': 500
        }
        return error_data
