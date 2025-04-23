from http.client import responses

import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"

USER_NAME = "yasinnn"
TOKEN = "erhffweusfnwfsdferieworf"

users_params ={
    "token" :TOKEN,
    "username" : USER_NAME,
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes"
}

# response = requests.post(pixela_endpoint,json=users_params)
# print(response.json())

graph_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs"

graph_params = {
    "id" :  "yasin17",
    "name" : "Coding Graph",
    "unit" : "commit",
    "type" :  "int",
    "color" : "shibafu"
}
headers ={
    "X-USER-TOKEN" : TOKEN
}

# response = requests.post(url=graph_endpoint,json=graph_params,headers=headers)
# print(response.json())
today = datetime.now()
Today = today.strftime("%Y%m%d")

posting_pixel =  f"{pixela_endpoint}/{USER_NAME}/graphs/yasin17"

pp_params = {
    "date" : Today,
    "quantity" : "10",
}

# response = requests.post(url=posting_pixel,json=pp_params,headers=headers)
# print(response.json())

update_pixel = f"{pixela_endpoint}/{USER_NAME}/graphs/yasin17/{Today}"

up = {
    "quantity" : "20",
}

# response = requests.put(url=update_pixel,json=up,headers=headers)
# print(response.status_code)

delete_pixel = f"{pixela_endpoint}/{USER_NAME}/graphs/yasin17/{Today}"

# response = requests.delete(delete_pixel,headers=headers)
# print(response.text)