import requests
import json

def tranlate(source, direction="auto2zh"):


    url = "http://api.interpreter.caiyunai.com/v1/translator"

    # WARNING, this token is a test token for new developers, and it should be replaced by your token
    token = "3975l6lr5pcbvidl6jl2"

    payload = {
        "source": source,
        "trans_type": direction,
        "request_id": "demo",
        "detect": True,
    }

    headers = {
        'content-type': "application/json",
        'x-authorization': "token " + token,
    }

    response = requests.request("POST", url, data=json.dumps(payload), headers=headers)

    return json.loads(response.text)['target']


def translation_str(str):
    target = tranlate([str])
    return target[0]

source = ["Lingocloud is the best translation service."]
target = tranlate(source)

print(target)

print(translation_str("my name is John"))