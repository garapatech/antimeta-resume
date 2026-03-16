from pydantic import BaseModel
from pydantic import ConfigDict

class ResumeBaseModel(BaseModel):
    model_config = ConfigDict(
        extra="allow",
        populate_by_name=True
    )
