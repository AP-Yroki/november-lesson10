class Student:

    def __init__(self, name, age, grade, scores):
        self.name = name
        self.age = age
        self.grade = grade
        self.scores = scores

    def info(self):
        print('Имя:', self.name)
        print('Возраст:', self.age)
        print('Класс:', self.grade)
        print('Оценки:', self.scores)

    def average_score(self):
        return sum(self.scores) / len(self.scores)

stubent2 = Student("Егор Данилов", 12, "5B", [5, 4, 4, 5])
stubent2.info()
print(stubent2.average_score())