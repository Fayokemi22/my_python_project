
from abc import ABC, abstractmethod

from job_application_tracker.com.job_applications.data.models.applicant import Applicant


class ApplicantRepository(ABC):

    @abstractmethod
    def save(self, applicant: Applicant):
        ...

    @abstractmethod
    def find_by_id(self, applicant_id):
        ...

    @abstractmethod
    def update(self, applicant_id, applicant: Applicant):
        ...

    @abstractmethod
    def delete(self, applicant_id):
        ...
