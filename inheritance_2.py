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

    def __eq__(self, other: (int, MeatEater, Vegetarian)):
        if isinstance(other, int):
            return other == self.capacity
        elif issubclass(other, Initialization):
            return self.capacity == other.capacity
        else:
            return f"Невозможно сравнить количество сладкоежек с {other}."

    def __lt__(self, other):
        if isinstance(other, int):
            return self.capacity < other
        elif isinstance(other, (MeatEater, Vegetarian)):
            return self.capacity < other.capacity
        else:
            return f"Невозможно сравнить количество сладкоежек в {other}."

    def __gt__(self, other):
        if isinstance(other, int):
            return self.capacity > other
        elif isinstance(other, (MeatEater, Vegetarian)):
            return self.capacity > other.capacity
        else:
            return f"Невозможно сравнить сладкоежек с {other}."


if __name__ == '__main__':
    v_first = Vegetarian(10_000, ["Орехи", "овощи", "фрукты"])
    print(v_first)
    v_second = Vegetarian([23], ["nothing"])
    m_first = MeatEater(15_000, ["Жареную картошку", "рыба"])
    print(m_first)
    s_first = SweetTooth(30_000, ["Мороженное", "Чипсы", "Шоколад"])
    print(s_first)
    print(s_first > v_first)
    print(30000 == s_first)
    print(s_first == 25000)
    print(100_000 < s_first)
    print(100 < s_first)
