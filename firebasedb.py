import firebase_admin
from firebase_admin import credentials, firestore


cred = credentials.Certificate('./animerecommendation-firebase-adminsdk-c0r7a-55fe253e51.json')

default_app = firebase_admin.initialize_app(cred)


db = firestore.client()