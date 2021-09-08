import requests

PARAMETER = {"amount": 10, "type": "boolean"}
response = requests.get(url="https://opentdb.com/api.php", params=PARAMETER).json()
question_data = response['results']
