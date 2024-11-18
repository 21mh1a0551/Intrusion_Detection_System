# from twilio.rest import Client

# # Replace these placeholders with your actual account SID and auth token
# account_sid = 'ACe18998ef467b04fafba29a3946197af9'
# auth_token = 'c866a5d7ca8e220cd57a5c20ad209cbd'
# client = Client(account_sid, auth_token)

# # Create and send the message
# def sendSms():
#     message = client.messages.create(
#     from_='+15203143778',  # Twilio-provided number
#     body='ALERT!! Did you access your laptop?',
#     to='+916202981527'  # Your number
#     )
#     print(message.sid)  # Print message SID to confirm it was sent


from twilio.rest import Client

account_sid = 'ACe18998ef467b04fafba29a3946197af9'
auth_token = 'c866a5d7ca8e220cd57a5c20ad209cbd'
client = Client(account_sid, auth_token)

def sendSms():
    message = client.messages.create(
    from_='whatsapp:+14155238886',
    body='ALERT! Your Desktop was accessed.',
    to='whatsapp:+916202981527'
    )
    print(message.sid)