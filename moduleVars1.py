import requests
import httpx
import asyncio
import time

api_vars = {
    "zadaca1": {
    "expected": {
        "test0": "3 7 8 2 4\n4 10 4 7 9\n1 5 20 7 3\n9 25 8 17 7\n30 7 8 4 20",
        "test1": "3 8 6\n9 16 5\n18 0 11",
        "test2": "7 2 4 1\n4 15 5 0\n6 13 16 2\n13 6 8 20",
        "test3": "9 9\n17 17",
        "test4": "5 4 3 2 1 0\n6 10 4 3 2 1\n7 6 15 6 3 2\n8 7 12 20 4 3\n9 20 7 6 25 4\n30 9 8 7 6 30",
        "test5": "10 11 12 13\n14 25 29 17\n18 48 45 21\n70 23 24 70",
        "test6": "3 2 1 0\n4 6 2 1\n5 6 9 2\n12 5 4 12",
        "test7": "-1",
        "test8": "-1",
        "test9": "1 0 0 0 0\n0 3 0 0 0\n0 0 6 0 0\n0 6 0 10 0\n6 0 0 0 15"
    },
    "input": {
        "test0": "5\n3 7 8 2 4\n4 7 4 3 9\n1 5 3 7 3\n9 5 8 4 7\n5 7 8 4 3",
        "test1": "3\n3 8 6\n9 7 5\n2 0 1",
        "test2": "4\n7 2 4 1\n4 8 4 0\n6 8 1 2\n0 6 8 4",
        "test3": "2\n9 9\n8 8",
        "test4": "6\n5 4 3 2 1 0\n6 5 4 3 2 1\n7 6 5 4 3 2\n8 7 6 5 4 3\n9 8 7 6 5 4\n10 9 8 7 6 5",
        "test5": "4\n10 11 12 13\n14 15 16 17\n18 19 20 21\n22 23 24 25",
        "test6": "4\n3 2 1 0\n4 3 2 1\n5 4 3 2\n6 5 4 3",
        "test7": "-5",
        "test8": "0",
        "test9": "5\n1 0 0 0 0\n0 2 0 0 0\n0 0 3 0 0\n0 0 0 4 0\n0 0 0 0 5"
    }
    },
    "zadaca2": {
    "expected": {
    "test0": "2",
    "test1": "2",
    "test2": "0",
    "test3": "2",
    "test4": "1",
    "test5": "3",
    "test6": "4",
    "test7": "2",
    "test8": "4",
    "test9": "4"
  },
  "input": {
    "test0": "bobo\nbo",
    "test1": "eestecisthebest\nest",
    "test2": "windows\nwd",
    "test3": "finkinemazgrada\nin",
    "test4": "niziodznaci?\nci?",
    "test5": "uiuiuiaaaiiaaiii\nui",
    "test6": "asdasdggffasdasd\nasd",
    "test7": "opopopoopopoop\noop",
    "test8": "qwertyhdifnqwertyjjifdjqwertycjdjqwerty\nqwerty",
    "test9": "ploploiikkpliploikiuplok\nplo"
  }
},
    "zadaca3": {
  "expected": {
    "test0": "6",
    "test1": "0",
    "test2": "8",
    "test3": "0",
    "test4": "2",
    "test5": "10",
    "test6": "10",
    "test7": "20",
    "test8": "20",
    "test9": "10"
  },
  "input": {
    "test0": "1234",
    "test1": "20",
    "test2": "182",
    "test3": "2023",
    "test4": "221223",
    "test5": "11224243414",
    "test6": "1784692001",
    "test7": "1802345987",
    "test8": "9876543210",
    "test9": "322982245"
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
