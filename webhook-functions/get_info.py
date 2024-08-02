import functions_framework

@functions_framework.http
def hello_http(request):
    """HTTP Cloud Function.
    Args:
        request (flask.Request): The request object.
        <https://flask.palletsprojects.com/en/1.1.x/api/#incoming-request-data>
    Returns:
        The response text, or any set of values that can be turned into a
        Response object using `make_response`
        <https://flask.palletsprojects.com/en/1.1.x/api/#flask.make_response>.
    """
    request_json = request.get_json(silent=True)
    request_args = request.args

    if request_json and 'name' in request_json:
        name = request_json['name']
    elif request_args and 'name' in request_args:
        name = request_args['name']
    else:
        name = 'World'
        
    message = 'Hello {}!'.format(name)
    
    print("The request is ", request)
    print("The request json is ", request_json)
    print("The request args is ", request_args)
    
    """
    jsonResponse = {
        'fullfillment_response': {
            'messages': [
                {
                    'text': {
                        'text': [message]
                    }
                }
            ]
        }
    }
    """
    """
    jsonResponse = {
        "fulfillmentText": "Here is the information you requested.",
        "fulfillmentMessages": [
            {
                "text": {
                    "text": ["Here is the information you requested."]
                }
            }
        ],
        "source": "get-info-function"
    }
    """
    
    """
    jsonResponse = {
        "fulfillmentText": "Here is the fulfillmentText you requested.",
        "fulfillmentMessages": [
            {
                "text": {
                    "text": ["Here is the information you requested."]
                }
            }
        ]
    }
    """
    
    text = "Here is the info requested response."
    parameters = {"cancel-period": "2"}
    jsonResponse = {
        "fulfillmentResponse": {
            "messages": [
                {
                    "text": {
                        "text": [text]
                    }
                }
            ]
        },
        "sessionInfo": {
            "parameters": parameters
        }
    }

    return jsonResponse
