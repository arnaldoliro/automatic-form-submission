import os
from dotenv import load_dotenv

load_dotenv()

API_URL = os.getenv('API_URL')
BEARER_TOKEN = os.getenv('BEARER_TOKEN')

emails = [emails.strip() for email in os.getenv('EMAILS').split(',') if email.strip()]