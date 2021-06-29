# passage-python

This Python SDK allows for verification of server-side authentication for applications using [Passage](https://passage.id)

## Authenticating a Request

To authenticate an HTTP request in a Flask application, you can use the Passage library in a middleware function. 

Please make sure you export your Passage public key and set it as an environment variable in your application (`PASSAGE_PUBLIC_KEY`)

```python
from passageidentity import Passage

def exampleFlaskMiddleware(request):
    psg = Passage()
    user = psg.authenticateRequest(request)
```

