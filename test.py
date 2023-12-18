import json


def get_submission_input(json_string):
    try:
        data = json.loads(json_string)
        return data.get('input', '')
    except json.JSONDecodeError:
        print("Error: Invalid JSON format.")
        return ''


data = {
    "cpp_code": "#include <iostream>\n\nusing namespace std;\n\nint main()\n{\n    int a, b, c;\n    cin >> a ;\n    cout<<\"HI\"<<a<<endl<<\"HI\";\n}"
}
print(type(data))
