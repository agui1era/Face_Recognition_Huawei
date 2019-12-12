
import requests
import base64
import json
import time

from datetime import datetime

while 1:

    
    # path imagenes

    path_base_image="C:/base_image.jpg"
    path_sample_image="C:/sample_image.jpg"

    # endpoint Huawei Cloud

    API_ENDPOINT_AUTH = "https://iam.ap-southeast-1.myhuaweicloud.com/v3/auth/tokens"
    API_ENDPOINT_FR = "https://face.ap-southeast-1.myhuaweicloud.com/v2/061618654d800fc02f6ac00fdca63540/face-compare"

    # url servidor interfaz gráfica 
    
    URL_SERVER="http://kognitive.cl/FR.php"

    # imagen de base

    try:

         with open(path_base_image, "rb") as img_file:
            stringb64_base = base64.b64encode(img_file.read())    
    except:
        print("An exception occurred with stringb64_base") 


    # imagen de muestra

    try:

     with open(path_sample_image, "rb") as img_file:
        stringb64_sample = base64.b64encode(img_file.read())
    
    except:
        print("An exception occurred with stringb64_sample") 

    # obtención del token de autorizacion

    data = {
      "auth": {
        "identity": {
          "methods": ["password"],
          "password": {
            "user": {
              "name": "oaguilera", 
               "password":"",
              "domain": {
                "name": "oaguilera" 
              }
            }
          }
        },
        "scope": {
          "project": {
            "name": "ap-southeast-1" 
          }
        }
      }
    }

    data=json.dumps((data))

    # sending post request and saving response as response object 
    try:
        r = requests.post(url = API_ENDPOINT_AUTH, data = data) 

    except:
        print("An exception occurred with token request") 

    pastebin_url = r.text 

    Token=r.headers['X-Subject-Token']

    # request al API de Face Recognition 

    stringb64_base=str(stringb64_base)
    stringb64_sample=str(stringb64_sample)

    data={

      "image1_base64":stringb64_base.strip("b'"),"image2_base64":stringb64_sample.strip("b'")

         }

    data=json.dumps((data))

    headers={"Content-Type":"application/json","X-Auth-Token":Token}

    try:

       r = requests.post(url = API_ENDPOINT_FR, data = data,headers=headers) 

    except:
        print("An exception occurred with request api FR") 

    # extracting response text 

    response_json = r.json() 
    print("Similarity="+ str(response_json["similarity"]))

    dateTimeObj = datetime.now()
 
    timestampStr = dateTimeObj.strftime("%d-%b-%Y (%H:%M:%S.%f)")
 
    print('Current Timestamp : ', timestampStr)

    #envío hacía el servidor 


    r = requests.get(url = URL_SERVER)

    print(r)

    time.sleep(3)