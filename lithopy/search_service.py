from serpapi import GoogleSearch
import requests
import os
import sys
import shutil


def remove_dir():
    folder_path = "images"
    # checking whether folder exists or not
    if os.path.exists(folder_path):
        # checking whether the folder is empty or not
        if len(os.listdir(folder_path)) == 0:
            # removing the file using the os.remove() method
            os.rmdir(folder_path)
        else:
            # messaging saying folder not empty
            shutil.rmtree(folder_path)
    else:
        # file not found message
        print("La carpeta no existe, no fue necesario eliminarla")

def download_images(imagelinks,query):
    remove_dir()
    os.mkdir("images")
    contador = 0
    print("LINK DE LA IMAGEN")
    print(imagelinks)
    for link in imagelinks:
        image_url = link
        filename = "images/"+query+str(contador)+".jpg"
    # Open the url image, set stream to True, this will return the stream content.
        r = requests.get(image_url, stream = True)
        # Check if the image was retrieved successfully
        if r.status_code == 200:
            # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
            r.raw.decode_content = True
            # Open a local file with wb ( write binary ) permission.
            with open(filename,'wb') as f:
                shutil.copyfileobj(r.raw, f)
            print('Imagen descargada correctamente',filename)
        else:
            print('La imagen no pudo ser procesada de acuerdo al contexto')
        print('Imagen descargada')
        contador +=1



def main_process(query):
    params = {
        "engine": "google",
        "q": query+" 1920x1080",
        "tbm": "isch",
        "api_key":"7c617063d60f7f7a1c123c46b2bdcab05987e60cb27e7e2463d638ac9922113c",
        "tbs":"itp:photos,isz:l" 
    }

    client = GoogleSearch(params)
    data = client.get_dict()
    links_images =[]
    for result in data['images_results']:
        if len(links_images)<=0:
            links_images.append(result['original'])
        else:
            break
    download_images(links_images,params["q"])
    return query

