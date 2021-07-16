from passageidentity import Passage
from passageidentity import PassageError
import pytest
import os
from flask import Flask, request
from werkzeug.http import dump_cookie

app = Flask(__name__)


def testFlaskValidTokenInHeader():
    psg = Passage("UKbRUx")
    # flask request context
    with app.test_request_context("thisisaurl.com",headers={'Authorization':'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2MjY0OTA3NzQsImlzcyI6IlVLYlJVeCIsInN1YiI6IlZabVFhU0NYbG5DZUJGUFVYU0x4In0.k3bNx4cpg06pt_2O0feaWxT0ashRGCXzv_CclwBnhMfzwQnSLPhI_eAzOKR6gRq4Y_gvdKKtFIsGaxCSJS1PT2mqFzHFDyyTt0nrXrtN6BD_cURVr91JMQo7-7Sx3k2bFvtPYhzInipi-cW60upAmXuZOpO_2MefHY-8-46Dl5WckJd3SK0uYQ5EEk0-gDc_6zyCu2faiCh5pA91SJKW78iwL3Y02tIolQ3gMpqSWOBWks1e2Ht73YkvY39O6mBY2fOmtzw3lIA290NO_-42km7X41O3JpA-3mzHwYtTj2g1qEAaKc9pjPY4SNYx3z6rlu9oty9Eku9Ee1fpS-dBzw'}):
        user = psg.authenticateRequest(request)
        assert user == 'VZmQaSCXlnCeBFPUXSLx'

def testFlaskTokenInCookie():
    psg = Passage("UKbRUx")
    # flask request context
    cookie = dump_cookie('psg_auth_token','eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2MjY0OTA3NzQsImlzcyI6IlVLYlJVeCIsInN1YiI6IlZabVFhU0NYbG5DZUJGUFVYU0x4In0.k3bNx4cpg06pt_2O0feaWxT0ashRGCXzv_CclwBnhMfzwQnSLPhI_eAzOKR6gRq4Y_gvdKKtFIsGaxCSJS1PT2mqFzHFDyyTt0nrXrtN6BD_cURVr91JMQo7-7Sx3k2bFvtPYhzInipi-cW60upAmXuZOpO_2MefHY-8-46Dl5WckJd3SK0uYQ5EEk0-gDc_6zyCu2faiCh5pA91SJKW78iwL3Y02tIolQ3gMpqSWOBWks1e2Ht73YkvY39O6mBY2fOmtzw3lIA290NO_-42km7X41O3JpA-3mzHwYtTj2g1qEAaKc9pjPY4SNYx3z6rlu9oty9Eku9Ee1fpS-dBzw')
    with app.test_request_context("thisisaurl.com",environ_base={'HTTP_COOKIE':cookie}):
        user = psg.authenticateRequest(request)
        assert user == 'VZmQaSCXlnCeBFPUXSLx'


def testFlaskInValidToken():
    psg = Passage("UKbRUx")
    # flask request context
    with app.test_request_context("thisisaurl.com",headers={'Authorization':'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJwYXNzYWdlIiwic3ViIjoiQ2NdjWXdLTkxJcEFtWkpIdnQifQ.EdUKRJwgK7ICRm4uIfGcL3v8zZRyrPWm1zUg5bnQ0m2ovLPGk2yLARZfpE6xhYhd22aemBx8EtNvg6hBg3qOVxKgrAsL-V78Z7S6DKJRRxbKSfJlz55SZOfklo5pz_VwVtOE34oWlq9JRbFaFHxhJuST3Z9ykJEm-1Ihr9ACX453pX9iTcLJmVMWbT4AlPAPtAL4rNsAU9b-KDQC1FUlTNE5e7HfOAaSnwz9qQZpviDAHYomJcWxFCWMri4Zj6PVQb8l57nMUqhf2BU4_q5iVJpV7DlODwApkQIPNWCGZj3oqeJv4T0ldUivtgq1YzEdK4Cw6__13f2IRuDTBHFKsQ'}):
        with pytest.raises(PassageError) as e:
            user = psg.authenticateRequest(request)

def testGetUserInfoValid():
    psg_apikey = os.environ.get("PASSAGE_API_KEY")
    psg = Passage("UKbRUx", psg_apikey)
    
    user = psg.getPassageUser('j6PYZBq3GwUjeRHLqmgR')
    assert user.email == "fae@ar"

def testGetUserInfoUserDoesNotExist():
    pass