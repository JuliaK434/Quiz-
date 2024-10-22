#Импортируем функцию и класс из модулей
from quiz_loader import load_tests
from quiz_manager import QuizManager


def main():
    '''Основная функция программы, которая управляет всем процессом, выбор и выполнение теста'''
    tests = load_tests()
    print("Доступные тесты:")
    for i, test_name in enumerate(tests.keys(), 1): #enumerate используется для нумерации тестов, начиная с 1
        print(f"{i}. {test_name}")

    #Выбираем тест, вводя его номер. Программа продолжает запрашивать ввод, пока пользователь не введет корректное число, соответствующее одному из тестов
    while True:
        try:
            choice = int(input("\nВыберите номер теста: "))
            if 1 <= choice <= len(tests):
                break
            print("Пожалуйста, выберите существующий тест")
        except ValueError:
            print("Пожалуйста, введите число")

    # Получаем выбранный тест
    test_name = list(tests.keys())[choice - 1] #Поскольку нумерация в списке начинается с 0, а пользователь вводит номер, начиная с 1, используется choice - 1
    test_data = tests[test_name]

    print(f"\nВы выбрали тест: {test_name}")

    # Создаем и запускаем тест
    quiz = QuizManager(test_data)
    quiz.run_quiz()
    quiz.show_results()

main()