import os
from twilio.rest import TwilioRestClient

account_sid = "AC42d3f5d0c9ff3634ecc99c9fcc441c2c" # Your Account SID from www.twilio.com/console
auth_token  = "7b40168c74e1347df6216e36b2ef026e"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="You'll Die in 7 days",
    to="+919781577496",    # Replace with your phone number
    from_="+13126472200") # Replace with your Twilio number

print(message.sid)
