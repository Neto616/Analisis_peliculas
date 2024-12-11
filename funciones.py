import requests

def peticion_api(url, headers):
    return (requests.get(url, headers=headers)).json()

def jsonFormat(json):
    if isinstance(json, list):
        result = """[\n\x20\n"""
        for x in json:
            result += "\x20{\n"
            for key, value in x.items():
                result += f'\x20\x20"{key}": {value}, \n'
            result += """\x20},\n"""
        result += """]\n"""
        print(result)
        return 
    if isinstance(json, dict):
        result = """{\n"""
        for key, val in json.items():
            result += f'\x20\x20"{key}": {val}, \n'
        result += """}\n"""
        print(result)
        return

if __name__ == "__main__":
    jsonFormat({"nombre": "NetoUwU", "edad": 20})
    # jsonFormat([{"nombre": "NetoUwU", "edad": 21}, {"nombre": "Ali Pilin", "edad": 21}, {"nombre": "RubusUwU", "edad": 21}])