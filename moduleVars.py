import requests
import httpx
import asyncio
import time

api_vars = {
    "zadaca1": {
        "expected": {
            "test0": "1",
            "test1": "2",
            "test2": "3",
            "test3": "4",
            "test4": "5",
            "test5": "6",
            "test6": "7",
            "test7": "8",
            "test8": "9",
            "test9": "100"
        },
        "input": {
            "test0": "1",
            "test1": "2",
            "test2": "3",
            "test3": "4",
            "test4": "5",
            "test5": "6",
            "test6": "7",
            "test7": "8",
            "test8": "9",
            "test9": "10"
        }
    },
    "zadaca2": {
        "expected": {
            "test0": "1",
            "test1": "2",
            "test2": "3",
            "test3": "4",
            "test4": "5",
            "test5": "6",
            "test6": "7",
            "test7": "8",
            "test8": "9",
            "test9": "10"
        },
        "input": {
            "test0": "1",
            "test1": "2",
            "test2": "3",
            "test3": "4",
            "test4": "5",
            "test5": "6",
            "test6": "7",
            "test7": "8",
            "test8": "9",
            "test9": "10"
        }
    },
    "zadaca3": {
        "expected": {
            "test0": "1",
            "test1": "2",
            "test2": "3",
            "test3": "4",
            "test4": "5",
            "test5": "6",
            "test6": "7",
            "test7": "8",
            "test8": "9",
            "test9": "10"
        },
        "input": {
            "test0": "1",
            "test1": "2",
            "test2": "3",
            "test3": "4",
            "test4": "5",
            "test5": "6",
            "test6": "7",
            "test7": "8",
            "test8": "9",
            "test9": "10"	
        }
    }
}

async def submision_vars(data):
    cpp_code = data.get('jsonData', {}).get('cpp_code', '')
    zad = data.get('jsonData', {}).get('zadaca', '')

    expected = api_vars.get(zad, '').get("expected", '')
    input = api_vars.get(zad, '').get("input", '')
    querystring = {"wait":"true"}
    url = "http://localhost:2358/submissions/batch"
    payload = {"submissions": []}
    for i in range(len(input)):
        submission = {
            "language_id": 52,
            "source_code": cpp_code,
            "stdin": input["test" + str(i)],
            "expected_output": expected["test" + str(i)]
        }
        payload["submissions"].append(submission)
    temp = requests.post(url, json=payload, params=querystring)
    # time.sleep(5)
    print("done")
    return temp
