class Recipe:

    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients

    def print_ingredients(self):
        print(f'Необходимые ингредиенты для: {self.name}')
        for ingredient in self.ingredients:
            print(ingredient)

    def cook(self):
        print(f'Сегодня мы приготовим: {self.name}')
        print(f'Выполняем инструкцию по приготовлению блюда: {self.name}...')
        print(f'Блюдо: {self.name} готово!')

# создаем рецепт спагетти болоньезе
spaghetti = Recipe("Спагетти болоньезе", ["Спагетти", "Фарш", "Томатный соус", "Лук", "Чеснок", "Соль"])

# печатаем список продуктов для рецепта спагетти
spaghetti.print_ingredients()

# готовим спагетти
spaghetti.cook()

# создаем рецепт для кекса
cake = Recipe("Кекс", ["Мука", "Яйца", "Молоко", "Сахар", "Сливочное масло", "Соль", "Ванилин"])

# печатаем рецепт кекса
cake.print_ingredients()

# готовим кекс
cake.cook()
