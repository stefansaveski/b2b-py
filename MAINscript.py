from moduleFunc import save_submission_to_json
from sheets import save_to_sheets

def start(data, index, name):
    jsons = save_submission_to_json(data)
    if jsons.get("correct", '') == "2":
        print("sheet")
        save_to_sheets(index, name, data.get('jsonData', {}).get("zadaca", ''),data.get('jsonData', {}).get("cpp_code", ''))
    return jsons