from passageidentity import Passage
from passageidentity import PassageError
import pytest
import os
from flask import Flask, request
from werkzeug.http import dump_cookie

app = Flask(__name__)


def testFlaskValidTokenInHeader():
    psg = Passage(os.environ.get("PASSAGE_APP_ID"))
    # flask request context
    with app.test_request_context("thisisaurl.com",headers={'Authorization':'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2MzA0Mjc2NjgsImlzcyI6IlRyV1NVYkREVFBDS1RRRHRMQTlNTzhFZSIsInN1YiI6IldXTXhOeVpkZUJGUmhhcFJ5MHlraFR2SSJ9.TganXdRVM_d__oAyWpWXGh0lDJ2N74b941hJaj2bg0-M2OAK_3nlmxA-351pXkwpAU6lccNB66SNc-KZE-sOxCJLMfK84ipIDZL3EPR40Mx1FM0ZvpgkYxIUL9nezVHy--9vIIXN7qpM9uWmOOhHZc9p0Tihkq7ZuhsQP5Q5Uo8LzEIy3Rd0vky1IDqtro065h3qhjxkf8eu6WZ32Bgie-ckg9VZZvBhxKkhZkrXKYrc4kazca135MitTj71V7ecCqxa1j-e157FQMGhMkoIasoEFZVvictc2yeZs-qEih0rVejYdHNwi90EtY3VokvkQG22Ma8rWNb118_MmHduqQ'}):
        user = psg.authenticateRequest(request)
        assert user == 'WWMxNyZdeBFRhapRy0ykhTvI'

def testFlaskTokenInCookie():
    psg = Passage(os.environ.get("PASSAGE_APP_ID"))
    # flask request context
    cookie = dump_cookie('psg_auth_token','eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2MzA0Mjc2NjgsImlzcyI6IlRyV1NVYkREVFBDS1RRRHRMQTlNTzhFZSIsInN1YiI6IldXTXhOeVpkZUJGUmhhcFJ5MHlraFR2SSJ9.TganXdRVM_d__oAyWpWXGh0lDJ2N74b941hJaj2bg0-M2OAK_3nlmxA-351pXkwpAU6lccNB66SNc-KZE-sOxCJLMfK84ipIDZL3EPR40Mx1FM0ZvpgkYxIUL9nezVHy--9vIIXN7qpM9uWmOOhHZc9p0Tihkq7ZuhsQP5Q5Uo8LzEIy3Rd0vky1IDqtro065h3qhjxkf8eu6WZ32Bgie-ckg9VZZvBhxKkhZkrXKYrc4kazca135MitTj71V7ecCqxa1j-e157FQMGhMkoIasoEFZVvictc2yeZs-qEih0rVejYdHNwi90EtY3VokvkQG22Ma8rWNb118_MmHduqQ')
    with app.test_request_context("thisisaurl.com",environ_base={'HTTP_COOKIE':cookie}):
        user = psg.authenticateRequest(request)
        assert user == 'WWMxNyZdeBFRhapRy0ykhTvI'


def testFlaskInValidToken():
    psg = Passage(os.environ.get("PASSAGE_APP_ID"))
    # flask request context
    with app.test_request_context("thisisaurl.com",headers={'Authorization':'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2MzA0Mjc2NjgsImlzcyI6IlRyV1NVYkREVFBDS1RRRHRMQTlNTzhFZSIsInN1YiI6IldXTXhOeVpkZUJGUmhhcFJ5MHlraFR2SSJ9.TganXdRVM_d__oAyWpWXGh0lDJ2N74b941hJaj2bg0-M2OAK_3nlmxA-351pXkwpAU6lccNB66SNc-KZE-sOxCJLMfK84ipIDZL3EPR40Mx1FM0ZvpgkYxIUL9nezVHy--9vIIXN7qpM9uWmOOhHZc9p0Tihkq7ZuhsQP5Q5Uo8LzEIy3Rd0vky1IDqtro065h3qhjxkf8eu6WZ32Bgie-ckg9VZZvBhxKkhZkrXKYrc4kazca135MitTj71V7ecCqxa1j-e157FQMGhMkoIasoEFZVvictc2yeZs-qEih0rVejYdHNwi90EtY3VokvkQG22Ma8rWNb118_MmHduqQ123'}):
        with pytest.raises(PassageError) as e:
            user = psg.authenticateRequest(request)

def testGetUserInfoValid():
    psg_apikey = os.environ.get("PASSAGE_API_KEY")
    psg_id = os.environ.get("PASSAGE_APP_ID")
    psg = Passage(psg_id, psg_apikey)
    
    user = psg.getUser('j6PYZBq3GwUjeRHLqmgR')
    assert user.email == "fae@ar"
    
def testActivateUser():
    psg_apikey = os.environ.get("PASSAGE_API_KEY")
    psg_id = os.environ.get("PASSAGE_APP_ID")
    psg = Passage(psg_id, psg_apikey)
    
    user = psg.getUser('j6PYZBq3GwUjeRHLqmgR')
    assert user.email == "fae@ar"
    user.activate()
    assert user.active == True

def testDeactivateUser():
    psg_apikey = os.environ.get("PASSAGE_API_KEY")
    psg_id = os.environ.get("PASSAGE_APP_ID")
    psg = Passage(psg_id, psg_apikey)
    
    user = psg.getUser('j6PYZBq3GwUjeRHLqmgR')
    assert user.email == "fae@ar"
    user.deactivate()
    assert user.active == False 

def testGetUserInfoUserDoesNotExist():
    pass