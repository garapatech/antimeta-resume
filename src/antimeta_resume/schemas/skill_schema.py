from typing import List
from typing import Optional
from pydantic import Field
from antimeta_resume.schemas.base_schema import ResumeBaseModel
from antimeta_resume.schemas.keyword_schema import KeywordSchema

class SkillSchema(ResumeBaseModel):
    name: str
    level: Optional[str] = None
    keywords: List[KeywordSchema] = Field(default_factory=list)
