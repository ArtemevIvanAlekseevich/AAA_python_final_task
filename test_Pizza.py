import pytest

import Pizza


def test_size_L():
    """Test that we can create pizza with size 'L'"""
    pizza = Pizza.Margherita('L')
    assert pizza.size == 'L'


def test_size_XL():
    """Test that we can create pizza with size 'XL'"""
    pizza = Pizza.Hawaiian('XL')
    assert pizza.size == 'XL'


def test_size_erro():
    """
    Test that we cannot create pizza with size
    which there isn't in size_dict
    """
    exception = ValueError
    with pytest.raises(exception):
        Pizza.Pepperoni('S')


def test_eq():
    """Test that we can use '=='"""
    b = Pizza.Hawaiian('L')
    a = Pizza.Pepperoni('L')
    assert a == b


def test_ne():
    """Test that we can use '!='"""
    a = Pizza.Hawaiian('L')
    b = Pizza.Pizza('XL')
    assert a != b


def test_lt():
    """Test that we can use '<'"""
    a = Pizza.Pepperoni('L')
    b = Pizza.Hawaiian('XL')
    assert a < b


def test_le():
    """Test that we can use '<='"""
    a = Pizza.Pepperoni('XL')
    b = Pizza.Pizza('L')
    c = Pizza.Margherita('XL')
    assert a <= c
    assert b <= a


def test_gt():
    """Test that we can use '>'"""
    a = Pizza.Margherita('L')
    b = Pizza.Margherita('XL')
    assert b > a


def test_ge():
    """Test that we can use '>='"""
    a = Pizza.Pizza('L')
    b = Pizza.Pizza('L')
    c = Pizza.Hawaiian('XL')
    assert b >= a
    assert c >= b


def test_change_size():
    """Test that we can change pizza size"""
    a = Pizza.Pizza('L')
    b = Pizza.Pizza('XL')
    assert a != b
    a.size = 'XL'
    assert a == b


def test_dict(capsys):
    """Test dict method"""
    recipe_margherita = ("{'Margherita': ['tomato sauce', 'mozzarella', "
                         "'tomatoes']}\n")
    Pizza.Margherita.dict()
    captured = capsys.readouterr()
    assert captured.out == recipe_margherita

    recipe_pizza = "{'Pizza': ['tomato sauce', 'mozzarella']}\n"
    Pizza.Pizza.dict()
    captured = capsys.readouterr()
    assert captured.out == recipe_pizza

    recipe_hawaiian = ("{'Hawaiian': ['tomato sauce', 'mozzarella', "
                       "'chicken', 'pineapples']}\n")
    Pizza.Hawaiian.dict()
    captured = capsys.readouterr()
    assert captured.out == recipe_hawaiian

    recipe_pepperoni = ("{'Pepperoni': ['tomato sauce', 'mozzarella', "
                        "'pepperoni']}\n")
    Pizza.Pepperoni.dict()
    captured = capsys.readouterr()
    assert captured.out == recipe_pepperoni


if __name__ == '__main__':
    pytest.main(['test_Pizza.py', '-v'])
