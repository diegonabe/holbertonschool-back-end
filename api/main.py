import requests

if __name__== '__main__':
    link = 'https://www.google.com.pe/'
    respuesta = requests.get(link)

    print(respuesta)  