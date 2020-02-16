import os
import dialogflow
from google.api_core.exceptions import InvalidArgument
import json
from google.protobuf.json_format import MessageToDict
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'private_key.json'


DIALOGFLOW_PROJECT_ID = 'leavebuddy-ufocwu'
DIALOGFLOW_LANGUAGE_CODE = 'en'
SESSION_ID = 'me'

def text_analyser(text_input):
    text_to_be_analyzed = text_input
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(DIALOGFLOW_PROJECT_ID, SESSION_ID)
    text_input = dialogflow.types.TextInput(text=text_to_be_analyzed, language_code=DIALOGFLOW_LANGUAGE_CODE)
    query_input = dialogflow.types.QueryInput(text=text_input)
    try:
        response = session_client.detect_intent(session=session, query_input=query_input)
    except InvalidArgument:
        raise

    print("Query text:", response.query_result.query_text)
    print("Detected intent:", response.query_result.intent.display_name)
    print("Detected intent confidence:", response.query_result.intent_detection_confidence)
    print("Fulfillment text:", response.query_result.fulfillment_text)
    data = response.query_result.parameters.fields
    date = data['date']
    date = MessageToDict(date)
    print(date)
    responder = response.query_result.fulfillment_text
    responder = str(responder)
    print('not eror')
    leave_type = data['type']
    print(leave_type)
    leave_type = MessageToDict(leave_type)
    return date,leave_type,responder