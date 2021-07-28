from twilio.rest import Client

accountSID = YOURACCOUNTSIDHERE
authToken = YOURAUTHTOKENHERE
twilioNumber = YOURTWILIONUMBERHERE


def SMSsend(msg):
    """
    Sends a SMS Message to a preconfigured list of numbers
    :param msg: Message that is sent to each recipient(String)
    """
    numbers = [ALLRECIPIENTNUMBERSHERE]
    client = Client(accountSID, authToken)
    for i in numbers:
        x = client.messages.create(to=i,
                                   from_=twilioNumber,
                                   body=msg)
        print(x.sid)
