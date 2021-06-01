import json
import os
from dotenv import load_dotenv
from pymongo import MongoClient
import argparse

parser = argparse.ArgumentParser()
parser.add_argument(
    "-o",
    "--outputdirectory",
    help="the path to the directory of the output files",
    required=True,
)
args = parser.parse_args()

# load environment variables:
load_dotenv()
MONGO_HOST = os.getenv("MONGO_HOST")
MONGO_PORT = os.getenv("MONGO_PORT")
MONGO_USERNAME = os.getenv("MONGO_USERNAME")
MONGO_PASSWORD = os.getenv("MONGO_PASSWORD")
MONGO_DB = os.getenv("MONGO_DB")

client = MongoClient(
    host=MONGO_HOST,
    port=MONGO_PORT,
    username=MONGO_USERNAME,
    password=MONGO_PASSWORD,
    authSource="admin",
    authMechanism="SCRAM-SHA-1",
)

db = client["records-of-processing-activities"]

organisations = list(db.organizations.find())
with open(
    args.outputdirectory + "organisations.json", "w", encoding="utf-8"
) as outfile:
    for organisation in organisations:
        json.dump(organisation, outfile, ensure_ascii=False, indent=4)
