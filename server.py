# @author DavidAwad

from flask import Flask,render_template,request,redirect,url_for
from twilio.rest import TwilioRestClient
from uwsgidecorators import *
import requests
import datetime
import pytz
import secrets
    
twil_client = TwilioRestClient(secrets.twil_acct, secrets.twil_token)
app=Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

def send_quote():
    r = requests.get('http://api.theysaidso.com/qod.json')
    
    # decompose JSON for quote
    quote = str(r.json()['contents']['quotes'][0]['quote'])
    # decompose JSON for author
    author = str(r.json()['contents']['quotes'][0]['author'])
    

    # Twilio sends the user a text message thanking them.
    # twil_client.messages.create( to="+1 732-925-4874", from_="+1 732-479-1418", body="#powerthrough" )
    twil_client.messages.create(
        to="+1 732-925-4874", # that's my number.
        from_="+1 732-479-1418", # change this number to your twilio trial number
        body= ' "{0}" " - {1}'.format(quote, author) #this would then be the quote
        )
    return

'''
if __name__ == '__main__':
    app.run(
        debug=True
        )
'''

if __name__ == '__main__':
    send_quote()
