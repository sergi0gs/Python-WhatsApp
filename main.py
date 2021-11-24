from time import sleep
import pywhatkit as kt
import pandas as pd
import pyautogui

def send_message(number, hour,min, message):
    kt.sendwhatmsg(number, message, hour, min, wait_time=10)
    print('Mensaje enviado')

def send_message_now(numeros, mensaje):
    numbers = numeros
    mensaje = mensaje

def get_list_excel(doc_name, sheet):
    lista = pd.read_excel(doc_name, sheet_name=sheet)
    lista['Lista'] = lista['Lista'].str.replace("'","")
    lista = lista.iloc[33:]
    lista = lista['Lista'].unique()
    lista = lista.tolist()
    return lista
    
if __name__=='__main__':
    numbers = ['+51965745585'] #'+51992573015''+51955459221','+51947517417','+51992573015'
    numbers_2 = ['+14155238886']
    message = '''
Hola 🖐

Te saluda Thelmo de Orange Team

Te escribo debido a tu inscripción al DESAFÍO OBJETIVOS PODEROSOS 2022

🎯En unos minutos iniciamos con el Webinar: Como crear objetivos poderosos para el 2022

⏰ 7 PM (Hora UTC -5)

Ingresa 👉 https://bit.ly/desafio_objetivo1

Grupo de soporte 👉https://bit.ly/soporte_desafio_whatsapp

Siguiente etapa de mañana 👉https://bit.ly/etapa2_desafio

Saludos.
    
'''
    twilio = '+14155238886'
    mensaje_2 = 'join pan-dozen'


    lista = get_list_excel('Envio de zoom - whatsapp.xlsx', sheet='normalizado')
    
    for i in lista:
        try:
            kt.sendwhatmsg_instantly(i, message, tab_close=False, wait_time=20)
            sleep(1)
            pyautogui.moveTo(x=1538,y=941)
            pyautogui.leftClick()
            pyautogui.press('enter')
            sleep(3)
            pyautogui.moveTo(x=1507,y=24)
            pyautogui.leftClick()

            print('Mensaje enviado')
        except:
            print('Ocurrio un error')
