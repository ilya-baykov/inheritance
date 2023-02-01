class Transport:
    def __init__(self, brand, max_speed, kind=None):
        self.brand = brand
        self.max_speed = max_speed
        self.kind = kind

    def __str__(self):
        return f"Тип транспорта {self.kind} марки {self.brand} может развить скорость " \
               f"{self.max_speed}км/ч"


class Car(Transport):
    def __init__(self, brand, max_speed, mileage, gasoline_residue, kind="Car"):
        super().__init__(brand, max_speed, kind)
        self.mileage = mileage
        self.__gasoline_residue = gasoline_residue

    @property
    def gasoline(self):
        return f"Осталось бензина на {self.__gasoline_residue}км"

    @gasoline.setter
    def gasoline(self, value: int):
        if isinstance(value, int):
            self.__gasoline_residue = value
            print(f"Объем топлива увеличен на {value}л и составляет"
                  f" {self.__gasoline_residue}л")
        else:
            print("Ошибка заправки автомобиля")


class Boat(Transport):
    def __init__(self, brand, max_speed, owners_name, kind="Boat"):
        super().__init__(brand, max_speed, kind)
        self.owners_name = owners_name

    def __str__(self):
        return f"Этой лодкой марки {self.brand} владеет {self.owners_name}"


class Plane(Transport):
    def __init__(self, brand, max_speed, capacity, kind="Plane"):
        super().__init__(brand, max_speed, kind)
        self.capacity = capacity

    def __str__(self):
        return f"Самолёт марки {self.brand} вмещает в себя " \
               f"{self.capacity} людей"
