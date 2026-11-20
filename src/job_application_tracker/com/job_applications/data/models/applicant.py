
from uuid import UUID


class Applicant:
    def __init__(self, id: UUID, first_name, email, last_name,
                 phone_number, address, role, education, company,
                 application_date, job_link, status, location):

        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
        self.address = address
        self.role = role
        self.education = education
        self.company = company
        self.application_date = application_date
        self.job_link = job_link
        self.status = status
        self.location = location

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        self._first_name = first_name

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        self._last_name = last_name

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email

    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        self._phone_number = phone_number

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, address):
        self._address = address

    @property
    def role(self):
        return self._role

    @role.setter
    def role(self, role):
        self._role = role

    @property
    def education(self):
        return self._education

    @education.setter
    def education(self, education):
        self._education = education

    @property
    def company(self):
        return self._company

    @company.setter
    def company(self, company):
        self._company = company

    @property
    def application_date(self):
        return self._application_date

    @application_date.setter
    def application_date(self, application_date):
        self._application_date = application_date

    @property
    def job_link(self):
        return self._job_link

    @job_link.setter
    def job_link(self, job_link):
        self._job_link = job_link

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        self._status = status

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, location):
        self._location = location
