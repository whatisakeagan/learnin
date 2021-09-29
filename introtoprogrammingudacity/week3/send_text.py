from twilio import rest

# Your account Sid and Auth Token from twilio.com/user/account
account_sid = "ACdd4dbdabe94b20990ea04db5ae746ec3"
auth_token = "9933d0a1f41348b9937f5e1479dddb4b"
client = rest.TwilioRestClient(account_sid, auth_token)

message = client.sms.messages.create (body="My name is Ron Burgundy?",
	to="redacted",
	from_="+12096268665")
print messsage
