import pywhatkit
import pandas as pd
import os
import time

def send_message(project_path):
    "Send message using a DataFrame"
    # Define data excel path
    data_path = os.path.join(project_path, "data.xlsx")

    # Define Images directory path
    image_path = os.path.join(project_path, "Images")

    # Read DataFrame data
    data = pd.read_excel(data_path, dtype={'Celular':str})
    
    # Send messages 
    for i in range(0,len(data)):
        name = data['Nombre'][i]
        number = data['Celular'][i]
        message = data['Mensaje'][i]
        image = os.path.join(image_path, data['Imagen'][i])

        print(f'Enviar mensaje a {name} con numero {number}') 
 
        pywhatkit.sendwhats_image(receiver=number, 
                                  img_path=image, 
                                  tab_close=True,
                                  caption=message,
                                  wait_time=15)
        time.sleep(2)

if __name__ == '__main__':
    #Eg: D:\Personal\Personal Projects\Python-WhatsApp
    send_message(project_path= r'D:\Personal\Personal Projects\Python-WhatsApp') 
