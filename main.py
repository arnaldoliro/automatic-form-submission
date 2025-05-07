import os
import requests
import time
import hashlib
from typing import Dict, Any
from dotenv import load_dotenv

load_dotenv()

class SecureRequester:
    def __init__(self):
        self.API_URL = os.getenv('API_URL')
        self.BEARER_TOKEN = os.getenv('BEARER_TOKEN')
        self.emails = self._load_emails()
    
    def _load_emails(self):
        raw_emails = os.getenv('EMAILS', '')
        return [email.strip() for email in raw_emails.split(',') if email.strip()]
    
    def _secure_headers(self) -> Dict[str, str]:

        return {
            "accept": "application/json",
            "authorization": f"Bearer {self.BEARER_TOKEN}",
            "content-type": "application/json"
        }

    def _secure_payload(self, email: str) -> Dict[str, any]:
        return {
            "record": {
                "email": email,
                "name": os.getenv('ROLE_NAME'),
                "occupation_area": "",
                "start_at": os.getenv('START_DATE')
            }
        }
    
    def _safe_log(self, message: str, sensitive_data: str) -> str:
        sensitive_hash = hashlib.sha256(sensitive_data.encode()).hexdigest()[:8]
        return f"{message} [HASH:{sensitive_hash}]"