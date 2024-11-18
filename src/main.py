class ChainSaw:
    def __init__(self, name="DniproM", power=150, rotation_speed=250, category="Tool"):
        self.__name = name
        self.__power = power
        self.__rotation_speed = rotation_speed
        self._category = category  

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

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, category):
        self._category = category

    # redefined methods

    def __str__(self):
        return f"chainsaw: {self.__name}, power: {self.__power} W, " \
               f"rotation speed: {self.__rotation_speed} rotations per second, " \
               f"category: {self._category}"

    def __repr__(self):
        return f"chainsaw (name='{self.__name}', power={self.__power}, " \
               f"rotation_speed={self.__rotation_speed}, category={self._category})"

    # destructor

    def __del__(self):
        print(f"Delete element: {self.__name}")


def main():
    default_chain_saw = ChainSaw()
    sctill_chain_saw = ChainSaw('Sctill', 122, 345, "Forest Tool")
    husqvarna_chain_saw = ChainSaw('Husqvarna', 200, 300, "Home Tool")

    print(default_chain_saw)
    print(sctill_chain_saw)
    print(husqvarna_chain_saw)

    print(repr(default_chain_saw))
    print(repr(sctill_chain_saw))
    print(repr(husqvarna_chain_saw))

if __name__ == "__main__":
    main()

