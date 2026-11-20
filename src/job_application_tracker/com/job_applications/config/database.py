
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

database = client["applicant_db"]

applicants_collection = database["applicants"]
