# Pick yourself up.

Send yourself a motivating text message with a quote of the day. Whenever you
think that should be.

## Usage
You can simply plug your Twilio credentials into secrets.py and you can get a
small motivational boost every morning!

the code is very simple, everything is inside `server.py`, we set up a twilio
client, and ping the quotes of the day api for the quote every day. then we just
send a text to the soon-to-be happy camper.

To add it to your crontab for the correctly timed script execution, simply type `crontab -e` and add the following. 
```
00 09 * * * /home/david/TwilMotivaBot/server.py
```
Then it should scrape the entire database of twitter users and send the texts to them. 

you can make sure it's working by checking crontab. 
`crontab -l` 

## Potential research use case. 
Does this affect a person's pschology? why not find out for yourself?
[Analyze their psychology over time using twitter after you set this up for them](https://github.com/DavidAwad/deTweector)

### resources 
[crontab](http://www.thegeekstuff.com/2009/06/15-practical-crontab-examples/)


**\#yolo**
