import requests
import httpx
import asyncio
import time

api_vars = {
    "zadaca1": {
    "expected": {
        "test0": "1 1",
        "test1": "4 8",
        "test2": "9 27",
        "test3": "16 64",
        "test4": "25 125",
        "test5": "36 216",
        "test6": "49 343",
        "test7": "64 512",
        "test8": "81 729",
        "test9": "100 1000"
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
    "test0": "4 2 3 3",
    "test1": "7 3 10 2.5",
    "test2": "10 4 21 2.33333",
    "test3": "15 5 50 2",
    "test4": "16 8 48 3",
    "test5": "18 12 45 5",
    "test6": "30 10 200 2",
    "test7": "30 20 125 5",
    "test8": "45 15 450 2",
    "test9": "60 20 800 2"
  },
  "input": {
    "test0": "3 1",
    "test1": "5 2",
    "test2": "7 3",
    "test3": "10 5",
    "test4": "12 4",
    "test5": "15 3",
    "test6": "20 10",
    "test7": "25 5",
    "test8": "30 15",
    "test9": "40 20"
  }
},
    "zadaca3": {
  "expected": {
    "test0": "1",
    "test1": "3",
    "test2": "10",
    "test3": "21",
    "test4": "55",
    "test5": "78",
    "test6": "105",
    "test7": "120",
    "test8": "136",
    "test9": "171"
  },
  "input": {
    "test0": "1",
    "test1": "2",
    "test2": "4",
    "test3": "6",
    "test4": "10",
    "test5": "12",
    "test6": "14",
    "test7": "15",
    "test8": "16",
    "test9": "18"
  }
}
}

def submision_vars(data, i, cpp_code, zad):
    expected = api_vars.get(zad, '').get("expected", '')
    input = api_vars.get(zad, '').get("input", '')
    querystring = {"base64_encoded":"false","wait":"true","fields":"stdout,status"}
    url = "http://localhost:2358/submissions"
    payload = {
        "language_id": 52,
        "source_code": cpp_code,
        "stdin": input["test" + str(i)],
        "expected_output": expected["test" + str(i)]
    }
    return requests.post(url, json=payload, params=querystring)
