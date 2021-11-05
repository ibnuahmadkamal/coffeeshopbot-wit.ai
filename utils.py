from wit import Wit
import wit

access_token = "your_wit.ai_token"

client = Wit(access_token = access_token)

#extract value from massage
def wit_response(message_text):
    resp = client.message(message_text)
    intent = None
    intent_name = None
    sentiment_value = None
    drinken_coffe = None
    order_coffe=None
    coffe =None
    
    try:
        intent_name = list(resp['intents'])[0]['name']
        #intent_name = intent['name']
        sentiment_value =resp['traits']['wit$sentiment'][0]['value']
        drinken_coffe = resp['entities']['']
    except:
        pass
    return(intent_name,sentiment_value)

print(wit_response("i have order one latte and i want order one cup fucking ice americano"))