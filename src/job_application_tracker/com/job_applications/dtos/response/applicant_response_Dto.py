from datetime import datetime

from pydantic import BaseModel, EmailStr


class ApplicantResponseDto(BaseModel):
    id: str
    email: EmailStr
    first_name: str
    last_name: str
    phone_number: str
    address: str
    role: str
    education: str
    company: str
    application_date: datetime
    job_link: str
    status: str
    location: str