class ChainSaw():
    # приватні
    __name = None
    __power = None
    __rotation_speed = None

    # публічні
    weight = 15
    category = "Instrument"

    def __init__(self, name="DniproM", power=150, rotation_speed=250, weight=15, category="Tool"):
        self.__name = name
        self.__power = power
        self.__rotation_speed = rotation_speed
        self.weight = weight
        self.category = category

    # геттери

    def get_name(self):
        return self.__name

    def get_power(self):
        return self.__power

    def get_rotation_speed(self):
        return self.__rotation_speed

    def get_weight(self):
        return self.weight

    def get_category(self):
        return self.category

    # cеттери

    def set_name(self, name):
        self.__name = name

    def set_power(self, power):
        self.__power = power

    def set_rotation_speed(self, rotation_speed):
        self.__rotation_speed = rotation_speed

    def set_weight(self, weight):
        self.weight = weight

    def set_category(self, category):
        self.category = category

    # перевизн методи

    def __str__(self):
        return f"chainsaw: {self.__name}, power: {self.__power} W, rotation speed: {self.__rotation_speed} rotations per second"

    def __repr__(self):
        return f"chainsaw (name='{self.__name}', power={self.__power}, rotation_speed={self.__rotation_speed})"

    # дестркктори

    def __del__(self):
        print(f"Delete element: {self.__name}")



def main():
    chainsaw_1 = ChainSaw()
    chainsaw_2 = ChainSaw("Stihl", 300, 450, 25, "Forest Tool")
    chainsaw_3 = ChainSaw("Chainsaw2", 100, 150, 12, "Home Tool")

    # виведення за допомогою __str__
    print(chainsaw_1)
    print(chainsaw_2)
    print(chainsaw_3)


    # виведення за допомогою __repr__
    print(repr(chainsaw_1))
    print(repr(chainsaw_2))
    print(repr(chainsaw_3))

main()


    
    
    







