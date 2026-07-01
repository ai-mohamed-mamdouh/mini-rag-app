from fastapi import APIRouter, Depends, UploadFile, status
from fastapi.responses import JSONResponse
from src.helpers.settings import get_settings,Settings
from src.controllers import UploadController
from src.controllers import ProjectController
import aiofile
from src.helpers.response_messages import ResponseMessages

data_router = APIRouter(
    prefix='/data'
) 

@data_router.get('/health')
def data_health() : 
    return {'message' : 'data route is running '}

@data_router.post('/upload/{project_id}')
async def upload(project_id : str, file : UploadFile,
           settings : Settings = Depends(get_settings)) :
    

    is_valid, message = UploadController().validate_upload_file(file=file)
    
    if not is_valid :
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={'message' : message}
        )

    project_controller = ProjectController()
    project_files_dir = project_controller.get_project_path(project_id)

    file_path, unique_name = project_controller.get_unique_key(
        project_files_dir=project_files_dir,
         filename=file.filename)
    
    try :
        async with aiofile.async_open(file_path, 'wb') as f:
            while chunk := await file.read(get_settings().FILE_CHUNK_SIZE) :
                await f.write(chunk)


        return JSONResponse(
            content= {'message' : ResponseMessages.FILE_UPLOADED_SUCCESSFULLY.value}
        ),file_path, unique_name
    
    except Exception as e :

        return JSONResponse(
            content= {'message' : e }
        )

