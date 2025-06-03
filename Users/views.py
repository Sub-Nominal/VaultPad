from django.shortcuts import render
from pyotp import random_base32, TOTP, totp
from qrcode import 

# Create your views here.
def MFA():
    totp=pyotp.TOTP(secret)