from passageidentity import Passage, PassageUser
from passageidentity import PassageError
import pytest
import os
from flask import Flask, request
from werkzeug.http import dump_cookie

app = Flask(__name__)


def testFlaskValidTokenInHeader():
    psg = Passage(os.environ.get("PASSAGE_APP_ID"), auth_strategy=Passage.HEADER_AUTH)
    # flask request context
    with app.test_request_context("thisisaurl.com",headers={'Authorization':'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NjgyOTAxMDgsImlzcyI6IlRyV1NVYkREVFBDS1RRRHRMQTlNTzhFZSIsInN1YiI6IkZYbWR1QUc1NWxFc3VlQWlLcVo0S2pmeSJ9.RdMCeMwH4d2Aianp7aik5lsM6nuZY0KGR56B6gaTO9e2NWU9kGom-Nfh0bmw7NK_CuqLFcaBYAx43HxfJ_-4JY3ybEJ0Ie8Mi17HXQcnnWdMZsEbtoKHcSoCv4s_VBssBL-panPFexmEHuRzfKJBqdM12YkGTNFMvb2h7v9DeXQCAsO8BxOtc7ljFK_cljjLnFEl3Cue4p2Uq6Xc_XPnJtmg0aOduFVMtxatnfdNPT_hga8UAD-6XbOyDAl6YYf1c23ohYiAq0tZj72EspYDhnEFjlpxhe_px1fTZl_gYCc5rdk0U6SeUv37vQ2Y_nFQrbh2Mmh5ZVnR4XCBOpS_rA'}):
        user = psg.authenticateRequest(request)
        assert user == 'FXmduAG55lEsueAiKqZ4Kjfy'

def testFlaskTokenInCookie():
    psg = Passage(os.environ.get("PASSAGE_APP_ID"))
    # flask request context
    cookie = dump_cookie('psg_auth_token','eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NjgyOTAxMDgsImlzcyI6IlRyV1NVYkREVFBDS1RRRHRMQTlNTzhFZSIsInN1YiI6IkZYbWR1QUc1NWxFc3VlQWlLcVo0S2pmeSJ9.RdMCeMwH4d2Aianp7aik5lsM6nuZY0KGR56B6gaTO9e2NWU9kGom-Nfh0bmw7NK_CuqLFcaBYAx43HxfJ_-4JY3ybEJ0Ie8Mi17HXQcnnWdMZsEbtoKHcSoCv4s_VBssBL-panPFexmEHuRzfKJBqdM12YkGTNFMvb2h7v9DeXQCAsO8BxOtc7ljFK_cljjLnFEl3Cue4p2Uq6Xc_XPnJtmg0aOduFVMtxatnfdNPT_hga8UAD-6XbOyDAl6YYf1c23ohYiAq0tZj72EspYDhnEFjlpxhe_px1fTZl_gYCc5rdk0U6SeUv37vQ2Y_nFQrbh2Mmh5ZVnR4XCBOpS_rA')
    with app.test_request_context("thisisaurl.com",environ_base={'HTTP_COOKIE':cookie}):
        user = psg.authenticateRequest(request)
        assert user == 'FXmduAG55lEsueAiKqZ4Kjfy'


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
    
    user = psg.getUser('TguJZxPXuc2owkpeIDvX0LeP')
    assert user.email == "dylan.brookes10+31@gmail.com"

def testActivateUser():
    psg_apikey = os.environ.get("PASSAGE_API_KEY")
    psg_id = os.environ.get("PASSAGE_APP_ID")
    psg = Passage(psg_id, psg_apikey)
    
    user = psg.activateUser('TguJZxPXuc2owkpeIDvX0LeP')
    assert user.active == True

def testDeactivateUser():
    psg_apikey = os.environ.get("PASSAGE_API_KEY")
    psg_id = os.environ.get("PASSAGE_APP_ID")
    psg = Passage(psg_id, psg_apikey)
    
    user = psg.getUser('TguJZxPXuc2owkpeIDvX0LeP')
    assert user.email == "dylan.brookes10+31@gmail.com"
    user = psg.deactivateUser(user.id)
    assert user.active == False 

def testUpdateUser():
    psg_apikey = os.environ.get("PASSAGE_API_KEY")
    psg_id = os.environ.get("PASSAGE_APP_ID")
    psg = Passage(psg_id, psg_apikey)
    
    user = psg.getUser('TguJZxPXuc2owkpeIDvX0LeP')
    assert user.email == "dylan.brookes10+31@gmail.com"
    user = psg.updateUser(user.id, {"email":"testingemail@passage.id"})
    assert user.email ==  "testingemail@passage.id"

def testGetUserInfoUserDoesNotExist():
    pass