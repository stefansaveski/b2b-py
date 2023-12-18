import time
import requests
from moduleVars import submision_vars, api_vars
import asyncio

def save_submission_to_json(data):
    print("Yo")
    zad = data.get('jsonData', {}).get('zadaca', '')
    tokens = asyncio.run(submision_vars(data))
    # print(tokens.json())

    done = False
    while not done:
        submission_data = {
        }
        cor_data = {}
        temp = 0
        trues = 0
        done = True
        for token in tokens.json():
            subs = "http://192.168.100.18:2358/submissions/" + str(token.get('token', ''))
            # print(token.get('token', ''))
            response = requests.get(subs).json()
            state = response.get("status", { }).get("id", "")
            # print(response)
            if state != 4 and state != 3:
                done = False
            tempData = response.get("stdout", "")
            isCor = response.get("status", {}).get("description", '')
            if temp == 0:
                submission_data = {
                    "test0": tempData
                }
                if isCor == "Accepted":
                    trues += 1
                    cor_data = {
                        "test0": "true"
                    }
                else:
                    cor_data = {
                        "test0": "false"
                    }
            if temp > 0:
                submission_data["test" + str(temp)] = tempData
                if isCor == "Accepted":
                    trues += 1
                    cor_data["test" + str(temp)] = "true"
                else:
                    cor_data["test" + str(temp)] = "false"
 
            temp += 1

        time.sleep(1)
    return {"input": api_vars.get(zad, '').get("input", ''), "expected": api_vars.get(zad, '').get("expected", ''),"got": submission_data, "is_same": cor_data, "correct": str(trues)}
