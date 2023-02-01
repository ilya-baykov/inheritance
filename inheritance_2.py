class Initialization:
    def __init__(self, capacity: int, food: list[str]):
        if isinstance(capacity, int):
            self.capacity = capacity
            self.food = ','.join(food)
        else:
            print("Количество людей должно быть целым числом")


class Vegetarian(Initialization):
    def __init__(self, capacity: int, food: list[str]):
        super().__init__(capacity, food)

    def __str__(self):
        return f"{self.capacity} людей предпочитают не есть мясо!" \
               f"Они предпочитают {self.food}"


class MeatEater(Initialization):
    def __init__(self, capacity: int, food: list[str]):
        super().__init__(capacity, food)

    def __str__(self):
        return f"{self.capacity} мясоедов в Москве! Помимо мясо они едят еще и {self.food}"
