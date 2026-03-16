from antimeta_resume.schemas.base_schema import ResumeBaseModel

class ReferenceSchema(ResumeBaseModel):
    name: str
    reference: str
