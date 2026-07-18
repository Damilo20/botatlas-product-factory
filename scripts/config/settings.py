import os
from dotenv import load_dotenv

load_dotenv()

AIRTABLE_API_KEY = os.getenv("AIRTABLE_API_KEY")
AIRTABLE_BASE_ID = os.getenv("AIRTABLE_BASE_ID")

if not AIRTABLE_API_KEY:
    raise ValueError("Missing AIRTABLE_API_KEY in .env")

if not AIRTABLE_BASE_ID:
    raise ValueError("Missing AIRTABLE_BASE_ID in .env")