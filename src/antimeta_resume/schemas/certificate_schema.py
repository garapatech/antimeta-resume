from typing import Optional
from antimeta_resume.schemas.base_schema import ResumeBaseModel

class CertificateSchema(ResumeBaseModel):
    name: str
    issuer: Optional[str] = None
    url: Optional[str] = None
