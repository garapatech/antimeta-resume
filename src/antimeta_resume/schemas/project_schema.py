from typing import Optional
from antimeta_resume.schemas.base_schema import ResumeBaseModel

class ProjectSchema(ResumeBaseModel):
    name: str
    description: str
    url: Optional[str] = None
