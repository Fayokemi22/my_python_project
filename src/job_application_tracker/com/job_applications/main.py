from fastapi import FastAPI

from job_application_tracker.com.job_applications.controllers.applicant_controller import router

app = FastAPI(title="Job Application Tracker")

app.include_router(router)