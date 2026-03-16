from typing import Optional
from antimeta_resume.schemas.base_schema import ResumeBaseModel

class LanguageSchema(ResumeBaseModel):
    language: str
    fluency: Optional[str] = None
