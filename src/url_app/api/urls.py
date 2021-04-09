from fastapi import APIRouter, Depends
from fastapi.responses import RedirectResponse

from ..models.urls import ShortLink
from ..services.urls import UrlService

router = APIRouter()


@router.post('/', response_model=ShortLink)
def shorten_url(
    url: str,
    service: UrlService = Depends(),

):
    return service.shorten_url(url)


@router.get('/{short_url}')
def shorten_url(
    short_url: str,
    service: UrlService = Depends(),
):
    original_url = service.get_full_url(short_url)
    original_url = original_url.__dict__
    return RedirectResponse(original_url['full_url'])
