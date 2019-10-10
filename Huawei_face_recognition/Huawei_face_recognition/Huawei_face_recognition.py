
import requests
import base64
with open("C:/image.jpg", "rb") as img_file:
    my_string = base64.b64encode(img_file.read())
print(my_string)
# importing the requests library 
import requests 

# defining the api-endpoint 
API_ENDPOINT = "https://iam.ap-southeast-1.myhuaweicloud.com/v3/auth/tokens"



data = {'api_option':'paste', 
		'api_paste_format':'python'} 

# sending post request and saving response as response object 
r = requests.post(url = API_ENDPOINT, data = data) 

# extracting response text 
pastebin_url = r.text 
print("The pastebin URL is:%s"%pastebin_url) 
