from typing import List
from typing import Optional
from pydantic import Field
from antimeta_resume.schemas.base_schema import ResumeBaseModel
from antimeta_resume.schemas.course_schema import CourseSchema

class EducationSchema(ResumeBaseModel):
    institution: str
    area: str
    study_type: str = Field(alias="studyType")
    location: Optional[str] = None
    website: Optional[str] = None
    specialization: Optional[str] = None
    start_date: str = Field(alias="startDate")
    end_date: Optional[str] = Field(default=None, alias="endDate")
    gpa: Optional[str] = None
    courses: List[CourseSchema] = Field(default_factory=list)
