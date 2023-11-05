class Soldier:
    def __init__(self, name, rank, service_number):
        self.name = name
        self.__rank = rank
        self.__service_number = service_number

    def get_rank(self):
        return self.__rank

    def confirm_service_number(self):
        return self.__service_number

    def promote(self):
        if self.__rank == "рядовой":
            self.__rank = "ефрейтор"
            return f"{self.name} повышен в звании, он теперь {self.__rank}"
        else:
            return f"{self.name} не может быть повышен в звании."

    def demote(self):
        if self.__rank == "ефрейтор":
            self.__rank = "рядовой"
            return f"{self.name} понижен в звании, он теперь {self.__rank}"
        else:
            return f"{self.name} не может быть понижен в звании."

soldier1 = Soldier("Иван Сусанин", "рядовой", "12345")

print(f"Создан новый игровой персонаж типа Soldier с атрибутами: {soldier1.__dict__}")
print(f"Персонаж {soldier1.name} имеет звание {soldier1.get_rank()}")
print(soldier1.promote())
print(soldier1.demote())
