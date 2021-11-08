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
					response = wit_response(messaging_text)
					#send response
					bot.send_text_message(sender_id, response)
					
	return "ok", 200

#def log(message):
	print(message)
	sys.stdout.flush()

if __name__ == "__main__":
    app.run(debug=True,port=80)