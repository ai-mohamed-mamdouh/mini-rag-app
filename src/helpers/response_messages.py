from enum import Enum

class ResponseMessages(Enum):
    FILE_UPLOADED_SUCCESSFULLY = "File uploaded successfully."
    FILE_TYPE_NOT_ALLOWED = "File type is not allowed."
    FILE_SIZE_TOO_LARGE = "File size is too large."
    FILE_REQUIRED = "File is required."
    SERVER_ERROR = "Something went wrong."