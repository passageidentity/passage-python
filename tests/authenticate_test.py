from passage import Passage
from errors import PassageError
import pytest
import os
from flask import Flask, request
from werkzeug.http import dump_cookie

app = Flask(__name__)

def testvalidToken():
    # set pub key
    os.environ["PASSAGE_PUBLIC_KEY"] = "LS0tLS1CRUdJTiBSU0EgUFVCTElDIEtFWS0tLS0tCk1JSUJDZ0tDQVFFQTVrZGlybnk1WnFjZ2NxcTg3YklMamtycFI3Ly9FRXRHR3lVL0xESkwxSnU2THRyaVNJemkKdzVPY2h4RkFKb25OUWhwd3dwKzNoT05OWWpKeFY1WWpibWlsc2ZMNWxsajJzZlJxY3lTMjBlZFZ2RDJqZ3hYWQpvT1g2SzU5dWtNQllzU0ZCcWtzM0UvYmNxd2YxN0U2bEIwVFhNY3NYUEtBNUE2QlJoMUVQSGtvQjlKWHJiS3hXCnhGT3JsRkJSRnJMVncvVmNUYnM3SXZRSGU4c3kxdlZoZGlkSng5R095MXVaQVlPL2dTcVNGNFRYd2RaaXJBQ1MKMjJFQlJFSSsrbWh1WWR3aWpaL3lZU1JwRFM4V0h1aVVMYjJrYnhVNUhoVG1jcnNrSjNjeEdnNHM1ZFA0V0YvZwpoMUNnYmdUczQ0dzFPVnUxdkNpNmMxQTQxMng3Wmh3UnR3SURBUUFCCi0tLS0tRU5EIFJTQSBQVUJMSUMgS0VZLS0tLS0K"
    psg = Passage()

    token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJwYXNzYWdlIiwic3ViIjoiQ2NGa0djWXdLTkxJcEFtWkpIdnQifQ.EdUKRJwgK7ICRm4uIfGcL3v8zZRyrPWm1zUg5bnQ0m2ovLPGk2yLARZfpE6xhYhd22aemBx8EtNvg6hBg3qOVxKgrAsL-V78Z7S6DKJRRxbKSfJlz55SZOfklo5pz_VwVtOE34oWlq9JRbFaFHxhJuST3Z9ykJEm-1Ihr9ACX453pX9iTcLJmVMWbT4AlPAPtAL4rNsAU9b-KDQC1FUlTNE5e7HfOAaSnwz9qQZpviDAHYomJcWxFCWMri4Zj6PVQb8l57nMUqhf2BU4_q5iVJpV7DlODwApkQIPNWCGZj3oqeJv4T0ldUivtgq1YzEdK4Cw6__13f2IRuDTBHFKsQ"
    user = psg.authenticateJwt(token)
    assert user == 'CcFkGcYwKNLIpAmZJHvt'

def testInvalidToken():
    # set pub key
    os.environ["PASSAGE_PUBLIC_KEY"] = "LS0tLS1CRUdJTiBSU0EgUFVCTElDIEtFWS0tLS0tCk1JSUJDZ0tDQVFFQTVrZGlybnk1WnFjZ2NxcTg3YklMamtycFI3Ly9FRXRHR3lVL0xESkwxSnU2THRyaVNJemkKdzVPY2h4RkFKb25OUWhwd3dwKzNoT05OWWpKeFY1WWpibWlsc2ZMNWxsajJzZlJxY3lTMjBlZFZ2RDJqZ3hYWQpvT1g2SzU5dWtNQllzU0ZCcWtzM0UvYmNxd2YxN0U2bEIwVFhNY3NYUEtBNUE2QlJoMUVQSGtvQjlKWHJiS3hXCnhGT3JsRkJSRnJMVncvVmNUYnM3SXZRSGU4c3kxdlZoZGlkSng5R095MXVaQVlPL2dTcVNGNFRYd2RaaXJBQ1MKMjJFQlJFSSsrbWh1WWR3aWpaL3lZU1JwRFM4V0h1aVVMYjJrYnhVNUhoVG1jcnNrSjNjeEdnNHM1ZFA0V0YvZwpoMUNnYmdUczQ0dzFPVnUxdkNpNmMxQTQxMng3Wmh3UnR3SURBUUFCCi0tLS0tRU5EIFJTQSBQVUJMSUMgS0VZLS0tLS0K"
    psg = Passage()

    token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJwYXNzYWdlIiwic3VjoiQ2NGa0djWXdLTkxJcEFtWkpIdnQifQ.EdUKRJwgK7ICRm4uIfGcL3v8zZRyrPWm1zUg5bnQ0m2ovLPGk2yLARZfpE6xhYhd22aemBx8EtNvg6hBg3qOVxKgrAsL-V78Z7S6DKJRRxbKSfJlz55SZOfklo5pz_VwVtOE34oWlq9JRbFaFHxhJuST3Z9ykJEm-1Ihr9ACX453pX9iTcLJmVMWbT4AlPAPtAL4rNsAU9b-KDQC1FUlTNE5e7HfOAaSnwz9qQZpviDAHYomJcWxFCWMri4Zj6PVQb8l57nMUqhf2BU4_q5iVJpV7DlODwApkQIPNWCGZj3oqeJv4T0ldUivtgq1YzEdK4Cw6__13f2IRuDTBHFKsQ"
    with pytest.raises(PassageError) as e:
        user = psg.authenticateJwt(token)

def testFlaskValidTokenInHeader():
    # set pub key
    os.environ["PASSAGE_PUBLIC_KEY"] = "LS0tLS1CRUdJTiBSU0EgUFVCTElDIEtFWS0tLS0tCk1JSUJDZ0tDQVFFQTVrZGlybnk1WnFjZ2NxcTg3YklMamtycFI3Ly9FRXRHR3lVL0xESkwxSnU2THRyaVNJemkKdzVPY2h4RkFKb25OUWhwd3dwKzNoT05OWWpKeFY1WWpibWlsc2ZMNWxsajJzZlJxY3lTMjBlZFZ2RDJqZ3hYWQpvT1g2SzU5dWtNQllzU0ZCcWtzM0UvYmNxd2YxN0U2bEIwVFhNY3NYUEtBNUE2QlJoMUVQSGtvQjlKWHJiS3hXCnhGT3JsRkJSRnJMVncvVmNUYnM3SXZRSGU4c3kxdlZoZGlkSng5R095MXVaQVlPL2dTcVNGNFRYd2RaaXJBQ1MKMjJFQlJFSSsrbWh1WWR3aWpaL3lZU1JwRFM4V0h1aVVMYjJrYnhVNUhoVG1jcnNrSjNjeEdnNHM1ZFA0V0YvZwpoMUNnYmdUczQ0dzFPVnUxdkNpNmMxQTQxMng3Wmh3UnR3SURBUUFCCi0tLS0tRU5EIFJTQSBQVUJMSUMgS0VZLS0tLS0K"
    psg = Passage()

    # flask request context
    with app.test_request_context("thisisaurl.com",headers={'Authorization':'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJwYXNzYWdlIiwic3ViIjoiQ2NGa0djWXdLTkxJcEFtWkpIdnQifQ.EdUKRJwgK7ICRm4uIfGcL3v8zZRyrPWm1zUg5bnQ0m2ovLPGk2yLARZfpE6xhYhd22aemBx8EtNvg6hBg3qOVxKgrAsL-V78Z7S6DKJRRxbKSfJlz55SZOfklo5pz_VwVtOE34oWlq9JRbFaFHxhJuST3Z9ykJEm-1Ihr9ACX453pX9iTcLJmVMWbT4AlPAPtAL4rNsAU9b-KDQC1FUlTNE5e7HfOAaSnwz9qQZpviDAHYomJcWxFCWMri4Zj6PVQb8l57nMUqhf2BU4_q5iVJpV7DlODwApkQIPNWCGZj3oqeJv4T0ldUivtgq1YzEdK4Cw6__13f2IRuDTBHFKsQ'}):
        user = psg.authenticateRequest(request)
        assert user == 'CcFkGcYwKNLIpAmZJHvt'

def testFlaskTokenInCookie():
    # set pub key
    os.environ["PASSAGE_PUBLIC_KEY"] = "LS0tLS1CRUdJTiBSU0EgUFVCTElDIEtFWS0tLS0tCk1JSUJDZ0tDQVFFQTVrZGlybnk1WnFjZ2NxcTg3YklMamtycFI3Ly9FRXRHR3lVL0xESkwxSnU2THRyaVNJemkKdzVPY2h4RkFKb25OUWhwd3dwKzNoT05OWWpKeFY1WWpibWlsc2ZMNWxsajJzZlJxY3lTMjBlZFZ2RDJqZ3hYWQpvT1g2SzU5dWtNQllzU0ZCcWtzM0UvYmNxd2YxN0U2bEIwVFhNY3NYUEtBNUE2QlJoMUVQSGtvQjlKWHJiS3hXCnhGT3JsRkJSRnJMVncvVmNUYnM3SXZRSGU4c3kxdlZoZGlkSng5R095MXVaQVlPL2dTcVNGNFRYd2RaaXJBQ1MKMjJFQlJFSSsrbWh1WWR3aWpaL3lZU1JwRFM4V0h1aVVMYjJrYnhVNUhoVG1jcnNrSjNjeEdnNHM1ZFA0V0YvZwpoMUNnYmdUczQ0dzFPVnUxdkNpNmMxQTQxMng3Wmh3UnR3SURBUUFCCi0tLS0tRU5EIFJTQSBQVUJMSUMgS0VZLS0tLS0K"
    psg = Passage()

    # flask request context
    cookie = dump_cookie('psg_auth_token','eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJwYXNzYWdlIiwic3ViIjoiQ2NGa0djWXdLTkxJcEFtWkpIdnQifQ.EdUKRJwgK7ICRm4uIfGcL3v8zZRyrPWm1zUg5bnQ0m2ovLPGk2yLARZfpE6xhYhd22aemBx8EtNvg6hBg3qOVxKgrAsL-V78Z7S6DKJRRxbKSfJlz55SZOfklo5pz_VwVtOE34oWlq9JRbFaFHxhJuST3Z9ykJEm-1Ihr9ACX453pX9iTcLJmVMWbT4AlPAPtAL4rNsAU9b-KDQC1FUlTNE5e7HfOAaSnwz9qQZpviDAHYomJcWxFCWMri4Zj6PVQb8l57nMUqhf2BU4_q5iVJpV7DlODwApkQIPNWCGZj3oqeJv4T0ldUivtgq1YzEdK4Cw6__13f2IRuDTBHFKsQ')
    with app.test_request_context("thisisaurl.com",environ_base={'HTTP_COOKIE':cookie}):
        user = psg.authenticateRequest(request)
        assert user == 'CcFkGcYwKNLIpAmZJHvt'

def testFlaskInValidToken():
    # set pub key
    os.environ["PASSAGE_PUBLIC_KEY"] = "LS0tLS1CRUdJTiBSU0EgUFVCTElDIEtFWS0tLS0tCk1JSUJDZ0tDQVFFQTVrZGlybnk1WnFjZ2NxcTg3YklMamtycFI3Ly9FRXRHR3lVL0xESkwxSnU2THRyaVNJemkKdzVPY2h4RkFKb25OUWhwd3dwKzNoT05OWWpKeFY1WWpibWlsc2ZMNWxsajJzZlJxY3lTMjBlZFZ2RDJqZ3hYWQpvT1g2SzU5dWtNQllzU0ZCcWtzM0UvYmNxd2YxN0U2bEIwVFhNY3NYUEtBNUE2QlJoMUVQSGtvQjlKWHJiS3hXCnhGT3JsRkJSRnJMVncvVmNUYnM3SXZRSGU4c3kxdlZoZGlkSng5R095MXVaQVlPL2dTcVNGNFRYd2RaaXJBQ1MKMjJFQlJFSSsrbWh1WWR3aWpaL3lZU1JwRFM4V0h1aVVMYjJrYnhVNUhoVG1jcnNrSjNjeEdnNHM1ZFA0V0YvZwpoMUNnYmdUczQ0dzFPVnUxdkNpNmMxQTQxMng3Wmh3UnR3SURBUUFCCi0tLS0tRU5EIFJTQSBQVUJMSUMgS0VZLS0tLS0K"
    psg = Passage()

    # flask request context
    with app.test_request_context("thisisaurl.com",headers={'Authorization':'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJwYXNzYWdlIiwic3ViIjoiQ2NdjWXdLTkxJcEFtWkpIdnQifQ.EdUKRJwgK7ICRm4uIfGcL3v8zZRyrPWm1zUg5bnQ0m2ovLPGk2yLARZfpE6xhYhd22aemBx8EtNvg6hBg3qOVxKgrAsL-V78Z7S6DKJRRxbKSfJlz55SZOfklo5pz_VwVtOE34oWlq9JRbFaFHxhJuST3Z9ykJEm-1Ihr9ACX453pX9iTcLJmVMWbT4AlPAPtAL4rNsAU9b-KDQC1FUlTNE5e7HfOAaSnwz9qQZpviDAHYomJcWxFCWMri4Zj6PVQb8l57nMUqhf2BU4_q5iVJpV7DlODwApkQIPNWCGZj3oqeJv4T0ldUivtgq1YzEdK4Cw6__13f2IRuDTBHFKsQ'}):
        with pytest.raises(PassageError) as e:
            user = psg.authenticateRequest(request)