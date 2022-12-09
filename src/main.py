import json
import base64
import os
import datetime
from google.cloud import firestore

encoded_key = os.getenv("FIREBASE_API_KEY")

SERVICE_ACCOUNT_JSON = json.loads(base64.b64decode(encoded_key).decode("utf-8"))

db = firestore.Client.from_service_account_info(SERVICE_ACCOUNT_JSON)

# Create a reference to the Google post.
collection = db.collection("marine-alerts")
doc_ref = collection.document("alerts")

# Then get the data at that reference.
doc = doc_ref.get()

doc_ref.set({
    'first': 'Peter',
    'last': 'Pan',
    'born': 1815,
    'timestamp': datetime.datetime.now()
    
    
})
