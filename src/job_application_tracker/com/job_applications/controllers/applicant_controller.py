
from fastapi import APIRouter

from job_application_tracker.com.job_applications.config.database import applicants_collection
from job_application_tracker.com.job_applications.data.repositories.applicant_repository_impl import ApplicationRepositoryImpl
from job_application_tracker.com.job_applications.services.applicant_service import ApplicantService
from job_application_tracker.com.job_applications.dtos.request.applicant_request_Dto import ApplicantRequestDto

router = APIRouter()

applicant_repo = ApplicationRepositoryImpl(applicants_collection)
applicant_service = ApplicantService(applicant_repo)

@router.post("/applicants/register")
def register_applicant(request: ApplicantRequestDto):
    return applicant_service.register_applicant(request)


@router.get("/applicants/{applicant_id}")
def get_applicant_by_id(applicant_id: str):
    return applicant_service.view_applicant(applicant_id)

@router.get("/applicants")
def view_all_applicants():
    return applicant_service.view_all_applicants()


@router.put("/applicants/{applicant_id}")
def update_applicant(applicant_id: str, request: ApplicantRequestDto):
    return applicant_service.update_applicant(request, applicant_id)


@router.delete("/applicants/{applicant_id}")
def delete_applicant(applicant_id: str):
    return applicant_service.delete_applicant(applicant_id)
