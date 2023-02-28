import requests
import random
import string
import uuid
import pytest
import unittest

loginsna4ala_url=""
data = {'login': '', 'password': ''}

res1 = requests.post(loginsna4ala_url, data = data)
print(res1.status_code)
print(res1.headers['Content-Type'])
print(res1.json())
data = res1.json()
access_token=data['access_token']
print(access_token)

api_url = ''

=(''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(17)))


newtestuuid=str(uuid.uuid4())
print(newtestuuid)

params = {
}
print(params)
print('Bearer '+access_token)

auth = {'Authorization': 'Bearer '+access_token, 'Content-Type': 'application/json', 'Host': ''}


res = requests.post(api_url, headers=auth, json=params)
print(res.status_code)
data = res.json()
print(data)
proverka=data['id']
print(proverka)

class TestStringMethods(unittest.TestCase):

    def test_nato4tovresponseEstId(data):
        data.assertTrue('id')

    def test_nato4toPrishloIntPosleID(data):
        data.assertTrue(proverka>0)
