import datetime
import unittest
from unittest.mock import Mock, AsyncMock

from job_application_tracker.com.job_applications.data.models.applicant import Applicant
from job_application_tracker.com.job_applications.dtos.request.applicant_request_Dto import RegisterApplicantRequestDto
from job_application_tracker.com.job_applications.services.applicant_service import ApplicantService


class ApplicantTest(unittest.TestCase):
    def setUp(self):
        self.mock = Mock()
        self.mock.find_by_id = Mock()
        self.mock.save = Mock()
        self.mock.delete = Mock()
        self.applicant = ApplicantService(self.mock)

    def test_register_applicant_request(self):
     applicant_request = RegisterApplicantRequestDto(first_name="first name", last_name="last name", phone_number="08131289879", address="address", role="role", education="education", company="company", application_date=datetime.datetime.now(), status="status", location="location", email="email", job_link="job link")
     self.assertEqual("Applicant created successfully",self.applicant.register_applicant(applicant_request))

    def test_update_applicant(self):
         applicant_request = RegisterApplicantRequestDto(
             first_name="first name",
             last_name="last name",
             phone_number="08131289879",
             address="address",
             role="role",
             education="education",
             company="company",
             application_date=datetime.datetime.now(),
             status="status",
             location="location",
             email="email",
             job_link="job link"
         )

         applicant_request.first_name = "joe"

         updated_applicant = self.applicant.update_applicant(applicant_request, "id")

         self.assertEqual("joe", updated_applicant.first_name)

    def test_view_applicant(self):
        applicant = Mock()
        applicant.role = "computer_analyst"

        self.mock.find_by_id.return_value = applicant

        view_applicant = self.applicant.view_applicant("123")

        self.assertEqual("computer_analyst", view_applicant.role)

    def test_delete_applicant(self):
         self.applicant.delete_applicant("id")

         self.mock.delete.assert_called_once_with("id")



if __name__ == '__main__':
    unittest.main()
