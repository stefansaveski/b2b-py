from moduleFunc1 import save_submission_to_json
from sheets import save_to_sheets

def start(data, index, name, timestart, time_end):
    jsons = save_submission_to_json(data)
    if jsons.get("correct", '') == "10":
        save_to_sheets(index, name, data.get('jsonData', {}).get("zadaca", ''), timestart, time_end, data.get('jsonData', {}).get("cpp_code", ''))
    return jsons