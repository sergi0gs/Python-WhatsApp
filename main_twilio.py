import os
from twilio.rest import Client

# las credenciales son leídas desde las variables de entorno TWILIO_ACCOUNT_SID y AUTH_TOKEN
account_sid = os.environ['AC037b357171e598eafaf17994b1846dba']
auth_token = os.environ['d5f785f6e2d762d8f1564c4a8393fd9e']

client = Client(account_sid, auth_token)
# este es el número de testeo de Twilio sandbox sandboxtfrom_whatsapp_number='whatsapp:+14155238886'
# reemplace este número con su numero personal de whastapp
message = client.messages.create(
                              body='Hello there!',
                              from_='whatsapp:+51965745585',
                              to='whatsapp:+5151937272854'
                          )

print(message.sid)