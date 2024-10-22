import json
import os

def load_tests():
    '''Собирает все тесты из JSON-файлов в указанной директории и возвращает их в виде словаря, где ключами являются имена тестов, а значениями — данные тестов'''
    tests = {}
    tests_dir = "tests"
    for filename in os.listdir(tests_dir): # os.listdir используется, чтобы получить список всех файлов в директории tests
        if filename.endswith('.json'): #Проверяется, заканчивается ли имя файла на '.json'. Это позволяет отфильтровать только файлы с расширением JSON
            with open(os.path.join(tests_dir, filename), 'r', encoding='utf-8') as f:
                #Файл открывается в режиме чтения ('r') с указанием кодировки 'utf-8'.
                # os.path.join используется для построения полного пути к файлу, объединяя директорию tests_dir и имя файла filename
                test_data = json.load(f)
                tests[test_data['name']] = test_data
    return tests