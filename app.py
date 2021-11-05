import os,sys
from flask import Flask,request
from pymessenger import Bot
from requests.models import Response
from utils import wit_response
app = Flask(__name__)

PAGE_ACCESS_TOKEN = "your_fbpage_token"
VERIFICATION_TOKEN = "hallo"

bot = Bot(PAGE_ACCESS_TOKEN)

@app.route('/', methods=['GET'])
def verify():
	if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
		if not request.args.get("hub.verify_token") == VERIFICATION_TOKEN:
			return "Verification token mismatch", 403
		return request.args["hub.challenge"], 200
	return "Hello world", 200

@app.route('/', methods=['POST'])
def webhook():
	data = request.get_json()
	#log(data)

	if data['object'] == 'page':
		for entry in data['entry']:
			for messaging_event in entry['messaging']:

				# ID message
				sender_id = messaging_event['sender']['id']
				recipient_id = messaging_event['recipient']['id']

				if messaging_event.get('message'):
					# Extracting text message
					if 'text' in messaging_event['message']:
						messaging_text = messaging_event['message']['text']
					else:
						messaging_text = 'no text'
					
					response = None
					#text handle by wit.ai
					intent_name,sentiment_value = wit_response(messaging_text)
					
					#mapping
					if intent_name == "gretting":
						response = """Welcome to our coffee shop
									Please select the option bellow according to your need

									1. Coffeeshop Menu 
									2. Make an Order
									3. Check order Status
									4. Reservation 
									5. Get our Location
									6. Contact Us"""

					elif intent_name =="menu":
						response = """You can see our menu in the list below
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
										
										Please type what you want order"""

					elif intent_name == "make_an_order":
						response = "Please enter the name of drinks or foods you want to order"

					elif intent_name == "order_status":
						response = "Please enter your Order ID"

					elif intent_name == "reservation":
						response = """Please enter the following data for reservation
										Name =
										Address =
										Ordered Menu =
										Order Date =
										Order Time ="""
					
					elif intent_name == "location":
						response = "You can access our coffee shop location via the following link(#Link)"

					elif intent_name == "contact_us":
						response = "What can we help?"
					
					elif intent_name == "buy_coffe":
						if sentiment_value == "positive" or sentiment_value == "neutral":
							response = "you made an order ......"
						else:
							response = "please use polite word for making order"

					else:
						response = "Your choice not in menu please type Hello to star the conversation."
					
					# Echo
					#response = messaging_text
					#send response
					bot.send_text_message(sender_id, response)
					

	return "ok", 200

#def log(message):
	print(message)
	sys.stdout.flush()

if __name__ == "__main__":
    app.run(debug=True,port=80)