import time
from fastapi import APIRouter

router = APIRouter()


@router.get('/access-check', description='Checking API access using the GET method')
async def access_check():
    """
    :return:
    """
    return {'status': 'OK', 'time': time.time()}


@router.post('/access-check', description='Checking API access using the POST method')
async def access_check():
    """
    :return:
    """
    return {'status': 'OK', 'time': time.time()}

