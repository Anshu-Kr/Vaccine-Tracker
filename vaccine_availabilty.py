import requests
import time
from datetime import date
from playsound import playsound

dist = int(input()) # ex:-294
d1=date.today()
d1 = d1.strftime("%d-%m-%y")

Alldate = ['d1']

def findAvailability():
    counter = 0
    result = requests.get(URL, headers=header)
    
    response_json = result.json()
    
    data = response_json["sessions"]
    
    for each in data:
        if((each["available_capacity_dose1"] > 0) & (each["min_age_limit"] == 18) & (each["vaccine"]=="COVISHIELD") & (each["pincode"]>=560000)& (each["pincode"]<560100)):
            counter += 1
            if(each["fee"]<'251'):
                print("-------------------------------",counter,"-----------------------------")
                print(each["date"])
                print(each["name"])
                print(each["pincode"])
                print(each["vaccine"])
                print(each["available_capacity_dose1"])
                print("Fee: "+each["fee"])
                print("-----------------------------FEE ZERO-----------------------------------\n")
                playsound("C:/Users/anshu/python intership/pocof1.mp3")
            else:
                print("-------------------------------",counter,"------------------------------")
                print(each["date"])
                print(each["name"])
                print(each["pincode"])
                print(each["vaccine"])
                print(each["available_capacity_dose1"])
                print("Fee: "+each["fee"])
                print("------------------------------------------------------------------------\n")
            
    if(counter == 0):
        print("No Available Slots")
        return False
    else:
        print("Total count=",counter)
    
while(True):
    for i in Alldate:
        date=i
        URL = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id={}&date={}'.format(
        dist, date)
        header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}   
        findAvailability()
        time.sleep(10)
    time.sleep(30)




