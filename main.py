import pywhatkit
import pandas as pd
import os

def send_message(data_path:str = None):
    "Send message using a DataFrame"
    data = pd.read_excel(data_path)
    print(data['Nombre'][0])
    print(type(data['Nombre'][0]))
    
    for i in (0,len(data)):
        name = data['Nombre'][i]
        number = data['Celular'][i]
        message = data['Mensaje'][i]
        image = data['Imagen'][i]

        pywhatkit.sendwhats_image(receiver=number, 
                                  img_path=r'D:\Personal\Personal Projects\Python-WhatsApp\Images\robot_hi.png', 
                                  tab_close=True,
                                  caption=f'Hola {Prueba bot {i}',
                                  wait_time=15)

if __name__ == '__main__':
    send_message(data_path=r'./data.xlsx')