
import nexmo

def send_sms(number,msg):
    
    client = nexmo.Client(key='b6057824', secret='dvMmi1fr8PtfHNjR')
    client.send_message({
    'from': 'Nexmo',
    'to': number,
    'text': msg,
    })
    print("sent")


    
