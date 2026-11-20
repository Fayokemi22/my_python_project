from datetime import datetime
from pydantic import Field, BaseModel


class ApplicantRequestDto(BaseModel):
    first_name: str
    last_name: str
    phone_number: str = Field(min_length=11, max_length=11)
    address: str
    role: str
    education: str
    company: str
    application_date: datetime
    job_link: str
    status: str
    location: str
    email: str