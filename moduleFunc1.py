import time
import requests
from moduleVars1 import submision_vars, api_vars
import asyncio

def save_submission_to_json(data):
    zad = data.get('jsonData', {}).get('zadaca', '')
    submission_data = {}
    cor_data = {}
    trues = 0
    cpp_code = data.get('jsonData', {}).get('cpp_code', '')
    for i in range(10):
        zad = data.get('jsonData', {}).get('zadaca', '')
        token = submision_vars(data, i, cpp_code, zad)
        tempData = token.json().get("stdout", "")
        isCor = token.json().get("status", {}).get("description", '')
        if isCor == 'Compilation Error':
            return {"input": ' ', "expected": ' ',"got": ' ', "is_same": ' ', "correct": ' ', "CompilationError": 'Compilation Error'}
        if isCor == 'Time Limit Exceeded':
            print("nice")
            return {"input": ' ', "expected": ' ',"got": ' ', "is_same": ' ', "correct": ' ',"CompilationError": 'Time Limit Exceeded'}
        if i == 0:
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
        if i > 0:
            submission_data["test" + str(i)] = tempData
            if isCor == "Accepted":
                trues += 1
                cor_data["test" + str(i)] = "true"
            else:
                cor_data["test" + str(i)] = "false"


    return {"input": api_vars.get(zad, '').get("input", ''), "expected": api_vars.get(zad, '').get("expected", ''),"got": submission_data, "is_same": cor_data, "correct": str(trues), "CompilationError": '0'}
