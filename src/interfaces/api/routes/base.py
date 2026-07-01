from fastapi import APIRouter, Depends
from src.helpers.settings import get_settings , Settings
base_router = APIRouter(
    prefix='/base'
)

@base_router.get('/health')
def health(settings : Settings = Depends(get_settings)) :
    return {'messaage' : settings.APP_NAME}