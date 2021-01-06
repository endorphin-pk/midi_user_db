import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

import secret

def setup(firebase_secret):
    cred = credentials.Certificate(firebase_secret)
    firebase_admin.initialize_app(cred, {
        "databaseURL": secret.dbURL
    })

def delete(data_dir):
    firebase_dir=db.reference(data_dir)
    firebase_dir.delete()

def read(data_dir="/"):
    firebase_dir = db.reference(data_dir)  # 기본 위치 지정
    tmp=firebase_dir.get()
    return tmp

def write(data,data_dir="/"):
    firebase_dir = db.reference(data_dir)  # 기본 위치 지정
    firebase_dir.update(data)