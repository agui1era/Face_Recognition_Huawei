
import requests
import base64
import json

image_base="C:/base_image.jpg"
sample_image="C:/sample_image.jpg"

with open(image_base, "rb") as img_file:
    my_string = base64.b64encode(img_file.read())
print(my_string)

API_ENDPOINT = "https://iam.ap-southeast-1.myhuaweicloud.com/v3/auth/tokens"



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

# sending post request and saving response as response object 
r = requests.post(url = API_ENDPOINT, data = data) 

# extracting response text 
pastebin_url = r.text 
print("The pastebin URL is:%s"%pastebin_url) 
