import json
import base64
import os
from dotenv import load_dotenv, find_dotenv

# get the value of `SERVICE_ACCOUNT_KEY`environment variable
load_dotenv(find_dotenv())
encoded_key = os.getenv("FIREBASE_API_KEY")

# decode
SERVICE_ACCOUNT_JSON = json.loads(base64.b64decode(encoded_key).decode('utf-8'))


from google.cloud import firestore

# Authenticate to Firestore with the JSON account key.
db = firestore.Client.from_service_account_json(SERVICE_ACCOUNT_JSON)

# Create a reference to the Google post.
collection = db.collection("marine-alerts")
doc_ref = collection.document("alerts")

# Then get the data at that reference.
doc = doc_ref.get()
