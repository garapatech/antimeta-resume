from typing import List
from pydantic import Field
from antimeta_resume.schemas.base_schema import ResumeBaseModel
from antimeta_resume.schemas.keyword_schema import KeywordSchema

class InterestSchema(ResumeBaseModel):
    name: str
    keywords: List[KeywordSchema] = Field(default_factory=list)
