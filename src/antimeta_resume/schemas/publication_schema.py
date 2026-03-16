from typing import Optional
from pydantic import Field
from antimeta_resume.schemas.base_schema import ResumeBaseModel

class PublicationSchema(ResumeBaseModel):
    name: str
    publisher: str
    release_date: Optional[str] = Field(default=None, alias="releaseDate")
    website: Optional[str] = None
    summary: Optional[str] = None
