class ChainSaw:
    def __init__(self, name="DniproM", power=150, rotation_speed=250, category="Tool"):
        self.__name = name
        self.__power = power
        self.__rotation_speed = rotation_speed
        self.category = category  

    # getters / setters

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def power(self):
        return self.__power
    
    @power.setter
    def power(self, power):
        self.__power = power

    @property
    def rotation_speed(self):
        return self.__rotation_speed
    
    @rotation_speed.setter
    def rotation_speed(self, rotation_speed):
        self.__rotation_speed = rotation_speed

    # redefined methods

    def __str__(self):
        return f"chainsaw: {self.__name}, power: {self.__power} W, rotation speed: {self.__rotation_speed} rotations per second, category: {self.category}"

    def __repr__(self):
        return f"chainsaw (name='{self.__name}', power={self.__power}, rotation_speed={self.__rotation_speed}, category={self.category})"

    # destructor

    def __del__(self):
        print(f"Delete element: {self.__name}")


def main():
    ch1 = ChainSaw()
    ch2 = ChainSaw('Sctill', 122, 345, "Forest Tool")
    ch3 = ChainSaw('Husqvarna', 200, 300, "Home Tool")

    print(ch1)
    print(ch2)
    print(ch3)

    print(repr(ch1))
    print(repr(ch2))
    print(repr(ch3))

if __name__ == "__main__":
    main()

