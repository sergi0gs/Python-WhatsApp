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
    #ista= lista[lista['Lista'].str.startswith('+51')]

    indices_peru = lista[lista['Lista'].str.startswith('+51')].index
    lista = lista.drop(indices_peru.tolist(), axis=0)

    lista = lista['Lista'].unique()
    lista = lista.tolist()
    return lista
    
if __name__=='__main__':
    numbers = ['+51123123456'] #'+51992573015''+51955459221','+51947517417','+51992573015'
    numbers_2 = ['+14155238886']
    message = '''
Hola 🖐

Te saluda Thelmo de Orange Team

Te escribo debido a tu inscripción al DESAFÍO OBJETIVOS PODEROSOS 2022

🎯Preguntas frecuentes:


⁉¿Puedo participar si no asistí a la primera sesión en vivo?

Si , puedes ver la repetición aquí: https://bit.ly/desafio_webinar1

⁉¿Dónde puedo ver las clases asincrónicas y dejar mi proyecto para el concurso?

Puedes acceder en el siguiente enlace : https://bit.ly/etapa2_desafio

Recuerda que la entrega de proyectos es hasta mañana(25 nov) 11:59 AM Hora Perú (UTC- 5)

⁉¿Cómo ingreso a la sesión de feedback en vivo?

Es el mismo enlace de la sesión 1 , te dejo el link aquí : https://bit.ly/desafio_objetivo1
Nos vemos en vivo el 25 nov - 7 PM horas Perú (UTC - 5)

Que tengas un excelente día.
Saludos.
'''
    twilio = '+14155238886'
    mensaje_2 = 'join pan-dozen'


    lista = get_list_excel('envío del 24 de nov.xlsx', sheet='Hoja1')
    
    for i in lista:
        try:
            kt.sendwhatmsg_instantly(i, message, tab_close=False, wait_time=20)
            sleep(1)
            pyautogui.moveTo(x=1108,y=934)
            pyautogui.leftClick()
            pyautogui.press('enter')
            sleep(3)
            pyautogui.moveTo(x=712,y=46)
            pyautogui.leftClick()

            print('Mensaje enviado')
        except:
            print('Ocurrio un error')
