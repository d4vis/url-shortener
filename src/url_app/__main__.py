import uvicorn

from .settings import settings


uvicorn.run('url_app.app:app', reload=True)
