"""Generates authentication token"""
import jwt
import datetime

SECRET_KEY = 'allhailtheking'
def encode_auth_token(*args):
    try:
        payload={
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30), 
            'iat' : datetime.datetime.utcnow()
        }
        return encode_auth_token(
            payload,
            SECRET_KEY
        )
    except Exception as e:
        return e
