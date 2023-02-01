class Initialization:
    def __init__(self, capacity: int, food: list[str]):
        if isinstance(capacity, int):
            self.capacity = capacity
            self.food = food
        else:
            print("Количество людей должно быть целым числом")


class Vegetarian(Initialization):
    def __init__(self, capacity: int, food: list[str]):
        super().__init__(capacity, food)

    def __str__(self):
        res_food = ','.join(self.food)
        return f"{self.capacity} людей предпочитают не есть мясо!" \
               f"Они предпочитают {res_food}"


