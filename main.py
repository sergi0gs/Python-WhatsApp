import pywhatkit as pwssp

def send_message(number, hour,min, message):
    pwssp.sendwhatmsg(number, message, hour, min, wait_time=10)
    print('Mensaje enviado')

def send_message_now(numeros, mensaje):
    numbers = numeros
    mensaje = mensaje

    
if __name__=='__main__':
    numbers = ['+51955459221','+51947517417','+51937272854','+51992573015'] #'+51992573015'
    numbers_2 = ['+14155238886']
    message = '''
Mensaje bot - WhatsApp <3 Python. Link: https://bit.ly/desafio_objetivo1

Espacio simple \n
otro tipo de espacio

    👀
    
'''
    twilio = '+14155238886'
    mensaje_2 = 'join pan-dozen'


    
    for i in numbers:
        try:
            pwssp.sendwhatmsg_instantly(i, message, tab_close=True, wait_time=20)
            print('Mensaje enviado')
        except:
            print('Ocurrio un error')
