class QuizManager: #класс QuizManager управляет процессом проведения викторины
    def __init__(self, test_data): #__init__ — это конструктор класса, который инициализирует объект
        self.test_data = test_data #test_data — данные теста, которые передаются при создании объекта. Предполагается, что это словарь, содержащий вопросы и ответы
        self.user_answers = [] #user_answers — список, в который будут сохраняться ответы пользователя
        self.total_points = 0 #total_points — общее количество баллов, которые можно набрать за все вопросы
        self.earned_points = 0 #earned_points — количество баллов, заработанных пользователем.

    def run_quiz(self):
        '''метод класса, который запускает викторину'''
        questions = self.test_data['questions']

        for i, q in enumerate(questions, 1):
            print(f"\nВопрос {i}: {q['question']}")
            for j, option in enumerate(q['options'], 1):
                print(f"{j}. {option}")

            while True:
                # Конструкция try - except для обработки исключений (описывала в предыдущем задании)
                try:
                    answer = int(input("Ваш ответ (введите номер): "))
                    if 1 <= answer <= len(q['options']):
                        break
                    print("Пожалуйста, выберите существующий вариант ответа")
                except ValueError:
                    print("Пожалуйста, введите число")

            self.user_answers.append(answer - 1)
            if answer - 1 == q['correct_answer']:
                self.earned_points += q['points']
            self.total_points += q['points']

    def show_results(self):
        '''метод класса, который выводит результаты викторины.'''
        print("\n=== Результаты теста ===")
        questions = self.test_data['questions']
        correct_answers = 0

        #Проходит по каждому вопросу и ответу пользователя, выводя вопрос, варианты ответов, ответ пользователя и правильный ответ
        for i, (q, user_answer) in enumerate(zip(questions, self.user_answers), 1):
            print(f"\nВопрос {i}: {q['question']}")
            print("Варианты ответов:")
            for j, option in enumerate(q['options'], 1):
                print(f"{j}. {option}")

            print(f"Ваш ответ: {q['options'][user_answer]}")
            print(f"Правильный ответ: {q['options'][q['correct_answer']]}")

            if user_answer == q['correct_answer']:
                correct_answers += 1
                print(f"✓ Верно! (+{q['points']} баллов)")
            else:
                print("✗ Неверно!")
        #Подсчитывает количество правильных ответов
        print(f"\nПравильных ответов: {correct_answers} из {len(questions)}")
        #Выводит общее количество правильных ответов, набранные и возможные баллы
        print(f"Набрано баллов: {self.earned_points} из {self.total_points}")
        #Вычисляет и выводит процент правильных ответов
        percent = (self.earned_points / self.total_points) * 100
        print(f"Результат: {percent:.1f}%")