from fastapi import APIRouter

from schemas import InputParams
from core import hoge

router = APIRouter()

@router.post('/hoge')
def hoge_endpoint(request: InputParams) -> str:
    return hoge(request)
