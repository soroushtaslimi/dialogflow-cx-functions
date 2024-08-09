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

    start_date = request_json['sessionInfo']['parameters']['start_date']
    print(start_date)

    text = "welcome to calendar booking func."
    parameters = {}

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
