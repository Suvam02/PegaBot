import os
from gnewsclient import gnewsclient
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="pegabot-ugvo.json"
'''
import dialogflow_v2 as dialogflow
dialogflow_session_client=dialogflow.sessions_client()
project_id="pegabot-ugvo" '''

project_id="pegabot-ugvo"

client=gnewsclient.NewsClient()


def detect_intent_texts(project_id, session_id, text, language_code):
    """Returns the result of detect intent with texts as inputs.

    Using the same `session_id` between requests allows continuation
    of the conversation."""
    from google.cloud import dialogflow

    session_client = dialogflow.SessionsClient()
    
    session = session_client.session_path(project_id, session_id)
    print("Session path: {}\n".format(session))

##for text in texts:
    text_input = dialogflow.TextInput(text=text, language_code=language_code)

    query_input = dialogflow.QueryInput(text=text_input)

    response = session_client.detect_intent(
        request={"session": session, "query_input": query_input}
    )
    return response
    '''
    print("=" * 20)
    print("Query text: {}".format(response.query_result.query_text))
    print(
            "Detected intent: {} (confidence: {})\n".format(
                response.query_result.intent.display_name,
                response.query_result.intent_detection_confidence,
        )
    )
    print("Fulfillment text: {}\n".format(response.query_result.fulfillment_text))
    '''


'''
h="Kolkata OF TEMPERATURE"
response=detect_intent_texts(project_id,1234,h,"en-US") 
print(response)      
'''

def fetch_news(parameters):
    
    client.language=parameters.get('language')
    client.location=parameters.get('geo-country')
    client.topic=parameters.get('topics')
    
    ##{'topics': 'News', 'language': '', 'geo-state': '', 'geo-country': 'United States', 'geo-city': ''}
    return(client.get_news()[:5])

def get_reply(query,chat_id):
    response=detect_intent_texts(project_id,chat_id,query,"en-US")
    if response.query_result.intent.display_name == "Topic_news":
        return "Topic_news",dict(response.query_result.parameters)
    else:
        return "small_talk",response.query_result.fulfillment_text
'''
h="Sports of kolkata in English"
i,r=get_reply(h,1234)
print(r)
a=fetch_news(r)
for i in a:
    print(i["link"])'''

topics_keyboard=[['Top Stories','World','Nation'],
['Business','Technology','Entertainment'],['Sports','Science','Health']]

