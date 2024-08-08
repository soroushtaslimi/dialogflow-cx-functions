import functions_framework
from google_sheet import GoogleSheetManager
import os
from data_manager import DataManager


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
    
    print("The request is ", request)
    print("The request json is ", request_json)
    print("The request args is ", request_args)

    phone_number = request_json['sessionInfo']['parameters']['phone_number']
    print("phone number is", phone_number)

    doc_info = request_doc_info()
    dm = DataManager(doc_info)

    customer_info = dm.get_row(phone_number)

    # text = str(customer_info)
    text = "thank you for calling."
    parameters = {"cancel-period": "2"}
    if not customer_info.empty:
        text = "Hi" + customer_info['name'] + "thank you for calling"
        parameters['name'] = customer_info['name']
        parameters['last-task'] = customer_info['last task']
        parameters['last-task-date'] = customer_info['last task date']

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


def request_doc_info():
    sheet_id = "1GJKFrXgyPWngS4Uz44z_xuu3nXOJdywOY8tBsF8F_Jg"
    credentials_file = os.path.join("credentials.json")
    sheet_name = "Sheet1"

    google_sheet_manager = GoogleSheetManager(sheet_id, credentials_file)

    doc_val = google_sheet_manager.read_sheet(sheet_name)
    return doc_val

