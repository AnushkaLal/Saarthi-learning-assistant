"""
Custom exceptions for Learning MRI backend
"""

from fastapi import status
from typing import Optional


class APIException(Exception):
    """Base API exception"""

    def __init__(
        self,
        message: str,
        status_code: int = status.HTTP_400_BAD_REQUEST,
        error_code: Optional[str] = None,
    ):
        self.message = message
        self.status_code = status_code
        self.error_code = error_code or "API_ERROR"
        super().__init__(self.message)


class ValidationException(APIException):
    """Validation error"""

    def __init__(self, message: str, error_code: str = "VALIDATION_ERROR"):
        super().__init__(message, status.HTTP_422_UNPROCESSABLE_ENTITY, error_code)


class FileException(APIException):
    """File handling error"""

    def __init__(self, message: str, error_code: str = "FILE_ERROR"):
        super().__init__(message, status.HTTP_400_BAD_REQUEST, error_code)


class FileSizeException(FileException):
    """File size exceeds limit"""

    def __init__(self, message: str = "File size exceeds maximum allowed"):
        super().__init__(message, "FILE_SIZE_ERROR")


class FileTypeException(FileException):
    """Invalid file type"""

    def __init__(self, message: str = "File type not allowed"):
        super().__init__(message, "FILE_TYPE_ERROR")


class NotFoundError(APIException):
    """Resource not found"""

    def __init__(self, message: str = "Resource not found"):
        super().__init__(message, status.HTTP_404_NOT_FOUND, "NOT_FOUND")


class ProcessingException(APIException):
    """Document processing error"""

    def __init__(self, message: str, error_code: str = "PROCESSING_ERROR"):
        super().__init__(message, status.HTTP_500_INTERNAL_SERVER_ERROR, error_code)


class ExternalServiceException(APIException):
    """External service error (API, Database, etc)"""

    def __init__(self, message: str, error_code: str = "EXTERNAL_SERVICE_ERROR"):
        super().__init__(message, status.HTTP_503_SERVICE_UNAVAILABLE, error_code)
