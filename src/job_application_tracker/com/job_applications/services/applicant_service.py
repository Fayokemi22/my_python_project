
from uuid import uuid4

from job_application_tracker.com.job_applications.data.models.applicant import Applicant
from job_application_tracker.com.job_applications.data.repositories.applicant_repository_impl import ApplicationRepositoryImpl
from job_application_tracker.com.job_applications.dtos.request.applicant_request_Dto import ApplicantRequestDto
from job_application_tracker.com.job_applications.exceptions.ApplicantNotFoundException import ApplicantNotFoundException


class ApplicantService:
    def __init__(self, applicant_impl: ApplicationRepositoryImpl):
        self.applicant_impl = applicant_impl

    def register_applicant(self, request: ApplicantRequestDto):

        applicant = Applicant(
            uuid4(), request.first_name, request.email, request.last_name,
            request.phone_number, request.address, request.role,
            request.education, request.company, request.application_date,
            request.job_link, request.status, request.location
        )

        self.applicant_impl.save(applicant)


        return f"Applicant created successfully , id : {applicant.id}"

    def update_applicant(self, request: ApplicantRequestDto, id: str):
        find_applicant = self.applicant_impl.find_by_id(id)

        if find_applicant is None:
            raise ApplicantNotFoundException("Applicant not found")

        applicant = Applicant(
            find_applicant["id"], request.first_name, request.email, request.last_name,
            request.phone_number, request.address, request.role,
            request.education, request.company, request.application_date,
            request.job_link, request.status, request.location
        )

        if find_applicant is None:
            return None

        if request.first_name is not None:
            applicant.first_name = request.first_name

        if request.last_name is not None:
            applicant.last_name= request.last_name

        if request.location is not None:
            applicant.location = request.location

        if request.company is not None:
            applicant.company = request.company

        if request.email is not None:
            applicant.email = request.email

        if request.education is not None:
            applicant.education = request.education

        if request.application_date is not None:
            applicant.application_date = request.application_date

        if request.phone_number is not None:
            applicant.phone_number = request.phone_number

        if request.job_link is not None:
            applicant.job_link = request.job_link

        if request.address is not None:
            applicant.address = request.address

        if request.role is not None:
            applicant.role = request.role

        if request.status is not None:
            applicant.status = request.status

        self.applicant_impl.update(id, applicant)
        return applicant

    def view_applicant(self, id: str):
        found_applicant = self.applicant_impl.find_by_id(id)
        if found_applicant is None:
            raise ApplicantNotFoundException("Applicant not found")
        found_applicant["_id"] = str(found_applicant["_id"])

        return found_applicant

    def view_all_applicants(self):
        found_applicants = self.applicant_impl.find_all()

        for applicant in found_applicants:
            applicant["_id"] = str(applicant["_id"])

        return found_applicants

    def delete_applicant(self, id: str):

        found_applicant =  self.applicant_impl.find_by_id(id)

        if found_applicant is None:
            raise ApplicantNotFoundException("Applicant not found")

        self.applicant_impl.delete(id)

        return "Applicant deleted successfully"

