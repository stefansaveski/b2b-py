import requests
import httpx
import asyncio
import time

api_vars = {
    "zadaca1": {
    "expected": {
    "test0": "1 2 4 5 5 6 7 9",
    "test1": "1 3 4 5 7 8 12 42 53 56",
    "test2": "1 2 2 5 6 7 8 9",
    "test3": "2 2 3 4 4 5 5 6 7 7 8 9",
    "test4": "2 2 3 4 4 5 5 6 7 7 8 9",
    "test5": "20 30 40 50 60 70",
    "test6": "12 16 18 24 24 32 36 40",
    "test7": "10 20 30 40",
    "test8": "-1",
    "test9": "-1"
  },
    "input": {
    "test0": "5 3\n1 2 3 4 5\n9 5 3 6 7",
    "test1": "7 2\n7 3 2 4 8 2 5\n12 56 2 2 42 53 1",
    "test2": "6 4\n8 4 2 6 4 1\n5 7 4 2 9 4",
    "test3": "7 1\n3 5 7 1 9 2 4\n6 8 1 4 7 2 5",
    "test4": "7 1\n3 5 7 1 9 2 4\n6 8 1 4 7 2 5",
    "test5": "4 10\n20 30 40 10\n50 60 70 10",
    "test6": "5 8\n12 18 8 24 36\n8 16 24 32 40",
    "test7": "3 5\n10 5 20\n30 5 40",
    "test8": "-1 5\n",
    "test9": "0 25\n"
  }
    },
    "zadaca2": {
    "input": {
    "test0": "5\n2 7 4 1 9",
    "test1": "3\n6 3 8",
    "test2": "7\n5 2 1 9 4 7 3",
    "test3": "2\n8 3",
    "test4": "4\n1 7 3 9",
    "test5": "6\n5 2 8 4 1 6",
    "test6": "3\n9 6 2",
    "test7": "4\n3 8 1 5",
    "test8": "1\n4",
    "test9": "8\n7 2 5 9 1 4 3 8"
  },
"expected": {
    "test0": "2 4\n7 1 9",
    "test1": "6 8\n3",
    "test2": "2 4\n5 1 9 7 3",
    "test3": "8\n3",
    "test4": "\n1 7 3 9",
    "test5": "2 8 4 6\n5 1",
    "test6": "6 2\n9",
    "test7": "8\n3 1 5",
    "test8": "4\n",
    "test9": "2 4 8\n7 5 9 1 3"
  }
},
    "zadaca3": {
  "expected": {
    "test0": "1 2 3\n4 5 6\n7 8 9",
    "test1": "1 2\n3 4",
    "test2": "1 2 3 4\n5 6 7 8\n9 10 11 12\n13 14 15 16",
    "test3": "42",
    "test4": "1 2 3 4 5\n6 7 8 9 10\n11 12 13 14 15\n16 17 18 19 20\n21 22 23 24 25",
    "test5": "1 2 3\n4 5 6\n7 8 9",
    "test6": "1 2\n3 4",
    "test7": "1 2 3 4\n5 6 7 8\n9 10 11 12\n13 14 15 16",
    "test8": "99",
    "test9": "1 2 3 4 5 6\n7 8 9 10 11 12\n13 14 15 16 17 18\n19 21 22 23 24 25\n26 26 27 28 29 30\n31 32 33 34 35 36"
  },
  "input": {
    "test0": "3\n3 1 2\n6 4 5\n7 8 9",
    "test1": "2\n2 1\n3 4",
    "test2": "4\n1 3 4 2\n6 8 7 5\n11 10 13 12\n15 16 14 9",
    "test3": "1\n42",
    "test4": "5\n2 3 1 4 5\n6 8 7 9 10\n11 13 12 15 14\n16 20 17 18 19\n23 22 24 25 21",
    "test5": "3\n2 3 1\n6 4 5\n8 9 7",
    "test6": "2\n1 2\n4 3",
    "test7": "4\n2 4 3 1\n5 7 6 8\n9 10 11 12\n16 14 15 13",
    "test8": "1\n99",
    "test9": "6\n6 1 4 3 2 5\n10 7 9 8 12 11\n15 14 17 13 16 18\n19 23 25 24 26 21\n30 32 28 31 27 29\n35 34 33 36 22 26"
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
