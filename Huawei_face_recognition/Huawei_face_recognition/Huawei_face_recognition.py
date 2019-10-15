
import requests
import base64
import json
import time

from datetime import datetime

# path imagenes
while 1:

    path_base_image="C:/base_image.jpg"
    path_sample_image="C:/sample_image.jpg"

    # endpint Huawei Cloud

    API_ENDPOINT_AUTH = "https://iam.ap-southeast-1.myhuaweicloud.com/v3/auth/tokens"
    API_ENDPOINT_FR = "https://face.ap-southeast-1.myhuaweicloud.com/v2/061618654d800fc02f6ac00fdca63540/face-compare"

    # imagen de base



    with open(path_base_image, "rb") as img_file:
        stringb64_base = base64.b64encode(img_file.read())
    # print(string_base)

    # imagen de muestra

    with open(path_sample_image, "rb") as img_file:
        stringb64_sample = base64.b64encode(img_file.read())
    # print(string_sample)

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

    r = requests.post(url = API_ENDPOINT_AUTH, data = data) 
    pastebin_url = r.text 

    Token=r.headers['X-Subject-Token']

    #print("The pastebin URL is:%s"%pastebin_url) 

    # request al API de Face Recognition 



    stringb64_base=str(stringb64_base)
    stringb64_sample=str(stringb64_sample)

    data={

      "image1_base64":stringb64_base.strip("b'"),"image2_base64":stringb64_sample.strip("b'")

         }

    data=json.dumps((data))

    #print(data)

    headers={"Content-Type":"application/json","X-Auth-Token":Token}

    #headers=json.dumps((headers))

    #print(headers)
    r = requests.post(url = API_ENDPOINT_FR, data = data,headers=headers) 


    # extracting response text 
    pastebin_url = r.text 
    print("The pastebin URL is:%s"%pastebin_url) 

    dateTimeObj = datetime.now()
 
    timestampStr = dateTimeObj.strftime("%d-%b-%Y (%H:%M:%S.%f)")
 
    print('Current Timestamp : ', timestampStr)
    time.sleep(1)