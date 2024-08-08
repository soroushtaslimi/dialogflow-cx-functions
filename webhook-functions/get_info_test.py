from get_info import hello_http
# from flask import request

class RequstTest:
    def __init__(self, json_f, args):
        self.json_f = json_f
        self.args = args

    def get_json(self, silent=True):
        return self.json_f
    


req_json = {'detectIntentResponseId': '43939215-37ae-4fb7-a44d-f2e3782edec2', 'pageInfo': {'currentPage': 'projects/gcpc-429512/locations/us-central1/agents/bb70a7c4-0c6f-4cb7-b9f9-d88a2daff02c/flows/00000000-0000-0000-0000-000000000000/pages/3c182653-dd9c-49af-a5e7-059fbfd7c947', 'formInfo': {'parameterInfo': [{'displayName': 'phone_number', 'required': True, 'state': 'FILLED', 'value': '14165059687', 'justCollected': True}]}, 'displayName': 'PhoneNumber'}, 'sessionInfo': {'session': 'projects/gcpc-429512/locations/us-central1/agents/bb70a7c4-0c6f-4cb7-b9f9-d88a2daff02c/sessions/d30b89-028-537-8a5-154179bd8', 'parameters': {'phone_number': '14165059687'}}, 'fulfillmentInfo': {'tag': 'get-info'}, 'text': '14165059687', 'languageCode': 'en', 'languageInfo': {'inputLanguageCode': 'en', 'resolvedLanguageCode': 'en', 'confidenceScore': 1.0}}
req = RequstTest(req_json, args={})

response_test = hello_http(req)
print(response_test)
