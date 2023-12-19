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

def submision_vars(data, i, cpp_code, zad):
    expected = api_vars.get(zad, '').get("expected", '')
    input = api_vars.get(zad, '').get("input", '')
    querystring = {"base64_encoded":"false","wait":"true","fields":"stdout,status"}
    url = "http://192.168.100.18:2358/submissions"
    payload = {
        "language_id": 52,
        "source_code": cpp_code,
        "stdin": input["test" + str(i)],
        "expected_output": expected["test" + str(i)]
    }
    return requests.post(url, json=payload, params=querystring)
