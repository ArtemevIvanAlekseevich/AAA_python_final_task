class Pizza():
    """
    Base class for all pizzas from our restaurant.
    _recipe keeps main pizza ingredients.
    size_dict keeps all size which our pizza can be.
    """
    size_dict = {
        'L': 30,
        'XL': 35
    }

    _recipe = {'Pizza': ['tomato sauce', 'mozzarella']}

    def __init__(self, size: str):
        if size not in Pizza.size_dict:
            raise ValueError('There isn\'t this size')
        self.size = size

    def __eq__(self, other) -> bool:
        """self == other"""
        return self.size_dict[self.size] == other.size_dict[other.size]

    def __ne__(self, other) -> bool:
        """self != other"""
        return self.size_dict[self.size] != other.size_dict[other.size]

    def __lt__(self, other) -> bool:
        """self < other"""
        return self.size_dict[self.size] < other.size_dict[other.size]

    def __le__(self, other) -> bool:
        """self <= other"""
        return self.size_dict[self.size] <= other.size_dict[other.size]

    def __gt__(self, other) -> bool:
        """self > other"""
        return self.size_dict[self.size] > other.size_dict[other.size]

    def __ge__(self, other) -> bool:
        """self >= other"""
        return self.size_dict[self.size] >= other.size_dict[other.size]

    @classmethod
    def dict(cls):
        """Prints pizza recipe"""
        print(cls._recipe)


class Margherita(Pizza):
    """
    Type of pizza with tomatoes.
    _recipe keeps pizza ingredients.
    pizza_ico is pizza emoji for menu.
    """
    _recipe = {
        'Margherita': ['tomato sauce', 'mozzarella', 'tomatoes']
    }
    pizza_ico = '🧀'

    def __init__(self, size: str):
        super().__init__(size)


class Pepperoni(Pizza):
    """
    Type of pizza with pepperoni.
    _recipe keeps pizza ingredients.
    pizza_ico is pizza emoji for menu.
    """
    _recipe = {
        'Pepperoni': ['tomato sauce', 'mozzarella', 'pepperoni']
    }
    pizza_ico = '🍕'

    def __init__(self, size: str):
        super().__init__(size)


class Hawaiian(Pizza):
    """
    Type of pizza with chicken and pineapples.
    _recipe keeps pizza ingredients.
    pizza_ico is pizza emoji for menu.
    """
    _recipe = {
        'Hawaiian': ['tomato sauce', 'mozzarella', 'chicken', 'pineapples']
    }
    pizza_ico = '🍍'

    def __init__(self, size: str):
        super().__init__(size)
