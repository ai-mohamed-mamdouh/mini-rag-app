from src.controllers.BaseController import BaseController
from fastapi import UploadFile
from src.helpers import ResponseMessages

class UploadController(BaseController) :
    def __init__( self ) : 
        super().__init__()
        self.size_scale = 1048576
    
    def validate_upload_file(self, file : UploadFile) :
        
        if file.content_type not in self.settings.FILE_ALLOWED_TYPES :
            return False , ResponseMessages.FILE_TYPE_NOT_ALLOWED.value
        
        if file.size > self.settings.FILE_ALLOWED_SIZE * self.size_scale :
            return False , ResponseMessages.FILE_SIZE_TOO_LARGE.value
        
        return True, ResponseMessages.FILE_UPLOADED_SUCCESSFULLY.value
    
    