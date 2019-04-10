import os
import firebase_admin
from firebase_admin import credentials, firestore

service_account_path = os.path.join(os.getcwd(), 'railcarunloadingdev-firebase-adminsdk-xdak0-e710be458f.json')

cred = credentials.Certificate(service_account_path)
client = firebase_admin.initialize_app(cred)
db = firestore.client()
