
from pymongo.collection import Collection

from job_application_tracker.com.job_applications.data.models.applicant import Applicant
from job_application_tracker.com.job_applications.data.repositories.applicant_repository import ApplicantRepository


class ApplicationRepositoryImpl(ApplicantRepository):

    def __init__(self, mongodb_collection: Collection):
        self.mongodb_collection = mongodb_collection

    def save(self, applicant: Applicant):
        applicant_data = {
            "id": str(applicant.id),
            "first_name": applicant.first_name,
            "last_name": applicant.last_name,
            "email": applicant.email,
            "phone_number": applicant.phone_number,
            "address": applicant.address,
            "role": applicant.role,
            "education": applicant.education,
            "company": applicant.company,
            "application_date": applicant.application_date,
            "job_link": applicant.job_link,
            "status": applicant.status,
            "location": applicant.location
        }

        self.mongodb_collection.insert_one(applicant_data)
        return "Applicant saved successfully"

    def find_by_id(self, applicant_id):
        applicant = self.mongodb_collection.find_one({"id": str(applicant_id)})
        return applicant

    def update(self, applicant_id, applicant: Applicant):
        applicant_data = {
            "first_name": applicant.first_name,
            "last_name": applicant.last_name,
            "email": applicant.email,
            "phone_number": applicant.phone_number,
            "address": applicant.address,
            "role": applicant.role,
            "education": applicant.education,
            "company": applicant.company,
            "application_date": applicant.application_date,
            "job_link": applicant.job_link,
            "status": applicant.status,
            "location": applicant.location
        }

        self.mongodb_collection.update_one(
            {"id": str(applicant_id)},
            {"$set": applicant_data}
        )

        return "Applicant updated successfully"

    def delete(self, applicant_id):
        self.mongodb_collection.delete_one({"id": str(applicant_id)})
        return "Applicant deleted successfully"
