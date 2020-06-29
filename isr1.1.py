import json

def jsontolib():
    try:
        with open('myfile.json', 'r', encoding='utf-8') as f:
            try:
                data = json.load(f)
                print(data)
                return data
            except json.decoder.JSONDecodeError as error:
                print("Файл пуст: ", error)
                return None
    except FileNotFoundError:
        print("Такого файла не существует!")
        return None

jsontolib()
