from twilio.rest import TwilioRestClient
# acct_id and auth_tkn values replaced with foo values so I don't get charged from random people using my codes
account_sid = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
auth_token = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
client = TwilioRestClient(account_sid, auth_token)

toNumber = ""
messagE = "Reminder Test"

# code to send message to phone numbers with a message. phone numbers commented out for privacy
message = client.messages.create(to=("+1" + toNumber), from_="+14079017873", body=messagE)
#                                   to: user                from: twillio                  message



