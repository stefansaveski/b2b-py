import requests
import httpx
import asyncio
import time

api_vars = {
    "zadaca1": {
    "expected": {
        "test0": "O",
        "test1": "XX\nXO",
        "test2": "XXX\nX#X\nXXO",
        "test3": "XXXX\nX##X\nX##X\nXXXO",
        "test4": "XXXXX\nX###X\nX###X\nX###X\nXXXXO",
        "test5": "XXXXXXXXXX\nX########X\nX########X\nX########X\nX########X\nX########X\nX########X\nX########X\nX########X\nXXXXXXXXXO",
        "test6": "XXXXXXXXXXXXXXX\nX#############X\nX#############X\nX#############X\nX#############X\nX#############X\nX#############X\nX#############X\nX#############X\nX#############X\nX#############X\nX#############X\nX#############X\nX#############X\nXXXXXXXXXXXXXXO",
        "test7": "O",
        "test8": "O",
        "test9": "XXXXXXXXXXXXXXXXXXXXXX\nX####################X\nX####################X\nX####################X\nX####################X\nX####################X\nX####################X\nX####################X\nX####################X\nX####################X\nX####################X\nX####################X\nX####################X\nX####################X\nX####################X\nX####################X\nX####################X\nX####################X\nX####################X\nX####################X\nX####################X\nXXXXXXXXXXXXXXXXXXXXXO"
    },
    "input": {
        "test0": "1",
        "test1": "2",
        "test2": "3",
        "test3": "4",
        "test4": "5",
        "test5": "10",
        "test6": "15",
        "test7": "-1",
        "test8": "0",
        "test9": "22"
    }
    },
    "zadaca2": {
    "expected": {
    "test0": "1",
    "test1": "0",
    "test2": "0",
    "test3": "3",
    "test4": "1",
    "test5": "3",
    "test6": "2",
    "test7": "0",
    "test8": "0",
    "test9": "1"
  },
  "input": {
    "test0": "999",
    "test1": "102",
    "test2": "907905",
    "test3": "99999",
    "test4": "9909",
    "test5": "19099909",
    "test6": "9909909",
    "test7": "-1",
    "test8": "990099",
    "test9": "109090"
  }
},
    "zadaca3": {
  "expected": {
    "test0": "2345\n645\n245\n85\n40\n4",
    "test1": "1631\n631\n181\n81\n8",
    "test2": "21\n2",
    "test3": "1",
    "test4": "20321\n2321\n621\n121\n21\n2",
    "test5": "233\n63\n18\n8",
    "test6": "4232\n832\n242\n82\n16\n6",
    "test7": "25\n10\n1",
    "test8": "36\n18\n8",
    "test9": "28\n16\n6"
  },
  "input": {
    "test0": "12345",
    "test1": "4431",
    "test2": "211",
    "test3": "10",
    "test4": "54321",
    "test5": "1233",
    "test6": "14232",
    "test7": "125",
    "test8": "136",
    "test9": "128"
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
