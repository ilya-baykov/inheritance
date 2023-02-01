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
        return f"{self.capacity} людей предпочитают не есть мясо! " \
               f"Они предпочитают {self.food}."


class MeatEater(Initialization):
    def __init__(self, capacity: int, food: list[str]):
        super().__init__(capacity, food)

    def __str__(self):
        return f"{self.capacity} мясоедов в Москве! Помимо мясо они едят еще и {self.food}."


class SweetTooth(Initialization):
    def __init__(self, capacity: int, food: list[str]):
        super().__init__(capacity, food)

    def __str__(self):
        return f"Сладкоежик в Москве {self.capacity}. Их самая любимая еда {self.food}."

    @classmethod
    def __verify_data(cls, other):
        if isinstance(other, int):
            return other
        elif isinstance(other, (MeatEater, Vegetarian)):
            return other.capacity
        else:
            return f"Невозможно сравнить количество сладкоежек с {other}."

    def __eq__(self, other: (int, MeatEater, Vegetarian)):
        return self.capacity == self.__verify_data(other)

    def __lt__(self, other):
        return self.capacity < self.__verify_data(other)

    def __gt__(self, other):
        return self.capacity > self.__verify_data(other)
