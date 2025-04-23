from http.client import responses
from pprint import pprint
import requests

API_ENDPOINT = "https://api.sheety.co/23902d0e084208c1ff66b450a1524184/flightDeals/sheet1"
HEADERS = { "Authorization": "Bearer mkedhcefsdkfowef2342"}

class DataManager:
    def __init__(self):
        self.sheet_data = {}
        self.users_endpoint = "https://api.sheety.co/23902d0e084208c1ff66b450a1524184/flightDeals/users"
        self.customer_data = {}
    def get_sheetdata (self):
        response = requests.get(API_ENDPOINT, headers=HEADERS)
        data = response.json()
        # print(data)
        self.sheet_data = data["sheet1"]
        return self.sheet_data

    def update_destination_codes(self):
        for city in self.sheet_data:
            new_data ={
                "sheet1" : {
                    "iataCode" : city["iataCode"]
                }
            }
            resp = requests.put(url=f"{API_ENDPOINT}/{city["id"]}",json=new_data,headers=HEADERS)

    def get_customer_emails(self):
        response = requests.get(url=self.users_endpoint)
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data
