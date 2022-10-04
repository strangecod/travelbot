from operator import truediv
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route ("/")
def hello():
    return "Hi this side ambuj!!"

@app.route("/sms", methods=['POST'])
def sms_reply():
    msg = request.form.get('Body')

    resp = MessagingResponse()
    resp.message("You said: {}".format(msg))
    
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)

#We have to deploy our application on some website so that we can ge3t the url which can be 
##used by the twilio to access our messages

