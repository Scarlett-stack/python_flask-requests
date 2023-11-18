import requests
import task
import json
url = "http://127.0.0.1:5000/"

while True:
    command = input()
    if command == "Sanity check":
        x = requests.get(url)
        print(x.status_code)
    elif command == "Add":
        '''
        x = requests.get(url)
        
        params = {'id': 'value1', 'name':'value2', 'description':'value3','priority':'value4','status':'value5'}
        x = requests.put(url, params)
        r = requests.post(url, params=params)
        print(r.status_code)
        '''
        json = {
        "id": 78912,
        "name": "Pisoiul Oskar",
        "description": "pisici",
        "priority": 1,
        "status":"not done"
        }
        headers = {'Content-type': 'application/json'}
        r = requests.post(url + 'add', data=json.dumps(json), headers=headers)
        print(r.status_code)
        
    elif command == "Print":
        pass
    elif command == "Print Employee Tasks":
        pass
    elif command == "Print Pending Tasks":
        pass
    elif command == "Print Completed Tasks":
        pass
    elif command == "Delete":
        pass
    elif command == "Delete All":
        pass
    elif command == "Complete Task":
        pass
    elif command == "Change Task Assignee":
        pass
    elif command == "Save":
        pass
    elif command == "Load":
        pass
    elif command == "Exit":
        break
