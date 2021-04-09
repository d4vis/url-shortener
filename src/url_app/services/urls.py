from fastapi import Depends
import short_url
from sqlalchemy.orm import Session

from ..db_tables import Url
from ..database import get_session


class UrlService:
    def __init__(self, session: Session = Depends(get_session)) -> None:
        self.session = session

    def shorten_url(self, url) -> Url:
        shortened_url = str(short_url.encode(url))
        db_operation = Url(full_url=url, short_url=shortened_url)
        self.session.add(db_operation)
        self.session.commit()
        return db_operation

    def get_full_url(self, short_url) -> str:
        query = self.session.query(Url).filter_by(short_url=short_url)
        link_data = query.first()
        return link_data.full_url
