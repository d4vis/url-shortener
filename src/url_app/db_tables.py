import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Url(Base):
    __tablename__ = 'urls'

    id = sa.Column(sa.Integer, primary_key=True)
    full_url = sa.Column(sa.Text)
    short_url = sa.Column(sa.Text)
