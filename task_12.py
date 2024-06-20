class Dessert:
    def __init__(self, name = None, calories = None):
        self.__name = name
        self.__calories = calories

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def calories(self):
        return self.__calories
    @calories.setter
    def calories(self, calories):
        self.__calories = calories

    def is_healthy(self):
        return isinstance(self.__calories, (int, float)) and self.__calories < 200


    def is_delicious(self):
        return True

class JellyBean(Dessert):

    def __init__(self, name = None, calories = None, flavor = None):
        super().__init__(name, calories)
        self.__flavor = flavor

    @property
    def flavor(self):
        return self.__flavor
    @flavor.setter
    def flavor(self, flavor):
        self.__flavor = flavor

    def is_delicious(self):
        if self.__flavor == 'black licorice':
            return False
        return True