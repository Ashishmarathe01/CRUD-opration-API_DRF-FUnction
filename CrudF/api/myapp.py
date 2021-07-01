# this thid party app for testinmg purpose for sending json responese
# made client side app for giving data

import requests
import json
URL="http://127.0.0.1:8000/"


# for geting data using with id or withough id
def get_data(id=None):
    data={}
    if id is not None:
        data={'id':id}
    json_data=json.dumps(data) # converting data into json
    r =requests.get(url=URL,data=json_data) # sending request to api
    data=r.json() # converting get response to json
    print(data)

# get_data(2)

# for update data


# complter update
def complete_update_data():
    data={
        'id':17,
        'name':'to',
        'age':1,

        'email':'ok@k.com'
    }
    json_data=json.dumps(data)
    r=requests.put(url=URL,data=json_data)
    print(r.json())
complete_update_data()

# delete data
def delete_data():
    data={
        'id':2,

    }
    json_data=json.dumps(data)
    r=requests.delete(url=URL,data=json_data)
    print(r.json())
# delete_data()




# for POST


def post_data():
    data={

        'name':'love',
        'age': 30,
        'email':'yo@go.com'

    }
    json_data=json.dumps(data)
    r=requests.post(url=URL,data=json_data)
    print(r.json())









