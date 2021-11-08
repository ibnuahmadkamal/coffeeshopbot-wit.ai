from wit import Wit
import wit

access_token = "63MG3GNV62P7RWRWZBRZBXVULROAMQL2"

client = Wit(access_token = access_token)

all_responses = {
    'greeting' : ["""Welcome to our coffee shop
									Please select the option bellow according to your need

									1. Coffeeshop Menu 
									2. Make an Order
									3. Check order Status
									4. Reservation 
									5. Get our Location
									6. Contact Us"""],
    'menu' : ["""You can see our menu in the list below
										==============================
										Signature menu

										1. Drinks
										Single origin
										2. Foods
										Tahu Walik
										==============================
										Drinks

										1. Single origin 
										2. Americano
										3.Cappucino
										==============================
										Foods

										1. Tahu walik
										2. French fries
										3. Mendoan
										
										Please type what you want order"""],
    'make_an_order' : ["Please enter the name of drinks or foods you want to order"],
    'order_status' : ["Please enter your Order ID"],
    'reservation' : ["""Please enter the following data for reservation
										Name =
										Address =
										Ordered Menu =
										Order Date =
										Order Time ="""],
    'location': ["You can access our coffee shop location via the following link(#Link)"],
    'contact_us' : ["What can we help?"]
}

def wit_response(message_text):
    resp = client.message(message_text)
    
    #extract value from massage
    try:
        #intent_name = intent['name']
        intent_name = resp['intents'][0]['name']
        sentiment_value =resp['traits']['wit$sentiment'][0]['value']
    except:
        pass
    
    #mapping responses
    if intent_name == "gretting":
        response = all_responses['greeting'][0]
    elif intent_name == "menu":
        response = all_responses ['menu'][0]
    elif intent_name == "make_an_order":
        response = all_responses['make_an_order'][0]
    elif intent_name == "order_status":
        response = all_responses['order_status'][0]
    elif intent_name == "reservation":
        response = all_responses['reservation'][0]
    elif intent_name == "location":
        response = all_responses['location'][0]
    elif intent_name == "contact_us":
        response = all_responses['contact_us'][0]
    else:
        response = "Your choice not in menu please type Hello to star the conversation."

    return(response)

#print(wit_response("hai"))