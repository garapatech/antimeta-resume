from typing import Optional
from pydantic import Field
from antimeta_resume.schemas.base_schema import ResumeBaseModel

class BasicsLocationSchema(ResumeBaseModel):
    address: Optional[str] = None
    postal_code: Optional[str] = Field(default=None, alias="postalCode")
    city: Optional[str] = None
    country_code: Optional[str] = Field(default=None, alias="countryCode")
    region: Optional[str] = None
