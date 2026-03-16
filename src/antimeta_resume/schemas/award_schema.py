from typing import Optional
from antimeta_resume.schemas.base_schema import ResumeBaseModel

class AwardSchema(ResumeBaseModel):
    title: str
    date: Optional[str] = None
    awarder: Optional[str] = None
    summary: Optional[str] = None
