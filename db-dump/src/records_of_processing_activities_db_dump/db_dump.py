"""Module for dumping data from db for statistical purposes."""
import json
import os

from dotenv import load_dotenv
from pymongo import MongoClient


# load environment variables:
load_dotenv()
MONGO_HOST = os.getenv("MONGO_HOST")
MONGO_PORT = os.getenv("MONGO_PORT")
MONGO_USERNAME = os.getenv("MONGO_USERNAME")
MONGO_PASSWORD = os.getenv("MONGO_PASSWORD")
MONGO_DB = os.getenv("MONGO_DB")
OUTPUT_DIR = os.getenv("OUTPUT_DIR", "./")

client = MongoClient(
    host=MONGO_HOST,
    port=MONGO_PORT,
    username=MONGO_USERNAME,
    password=MONGO_PASSWORD,
    authSource="admin",
    authMechanism="SCRAM-SHA-1",
)

db = client[MONGO_DB]

organizations = list(db.organizations.find())
with open(OUTPUT_DIR + "organizations.json", "w", encoding="utf-8") as outfile:
    for organization in organizations:
        json.dump(organization, outfile, ensure_ascii=False, indent=4)
