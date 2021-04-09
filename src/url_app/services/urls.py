from fastapi import Depends
from sqlalchemy.orm import Session
import uuid

from ..db_tables import Url
from ..database import get_session


class UrlService:
    def __init__(self, session: Session = Depends(get_session)) -> None:
        self.session = session

    def shorten_url(self, url) -> Url:
        url_exists = self.session.query(Url).filter_by(full_url=url).first()
        if url_exists:
            return url_exists
        shortened_url = uuid.uuid5(uuid.NAMESPACE_URL, url).hex[:5]
        db_operation = Url(full_url=url, short_url=shortened_url)
        self.session.add(db_operation)
        self.session.commit()
        return db_operation

    def get_full_url(self, short_url) -> Url:
        query = self.session.query(Url).filter_by(short_url=short_url)
        link_data = query.first()
        return link_data
