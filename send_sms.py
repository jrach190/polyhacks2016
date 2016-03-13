from twilio.rest import TwilioRestClient
#acct_id and auth_tkn values replaced with foo values so I dont get charged from random people using my codes
account_sid = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
auth_token = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
client = TwilioRestClient(account_sid, auth_token)

#code to send message to phone numbers with a message. phone numbers commented out for privacy
message = client.messages.create(to="+1XXXXXXXXXX", from_= "+1XXXXXXXXXX", body="Hello, World! Love from Twilio.")
message = client.messages.create(to="+1XXXXXXXXXX", from_= "+1XXXXXXXXXX", body="Hello, World! Love from Twilio.")
message = client.messages.create(to="+1XXXXXXXXXX", from_= "+1XXXXXXXXXX", body="Hello, World! Love from Twilio.")
message = client.messages.create(to="+1XXXXXXXXXX", from_= "+1XXXXXXXXXX", body="Hello, World! Love from Twilio.")



