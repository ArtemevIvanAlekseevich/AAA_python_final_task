from random import randint
from time import sleep
from typing import Callable

import click

import Pizza


def log(msg_text: str = '') -> Callable:
    """
    Prints stage of cooking and time of each stage.
    Also you can add massage at the end with using msg_text
    with '{}' to print total time in {}.
    .
    """
    def wrapper(func: Callable) -> Callable:
        def inner_wrapper(*args, **kwargs):
            time = randint(1, 9)
            func(*args, **kwargs)
            time_msg = f'Stage: {func.__name__.strip("_")}, Time:'
            for i in range(time+1):
                print(time_msg, f'{i}c', end='\r')
                sleep(0.2)
            print('\n\r', end='')
            sleep(0.5)
            if msg_text:
                print(msg_text.format(time))
        return inner_wrapper
    return wrapper


@click.group()
def cli():
    pass


@log('👨‍🍳 baked in {}с!')
def bake(pizza) -> None:
    """Bakes pizza"""
    print(f'Your {pizza} is being baked')


@log('🛵 deliveried in {}с!')
def delivery_(pizza) -> None:
    """Deliveries pizza"""
    print(f'Your {pizza} is being deliveried')


@log('🏠 picked up in {}с!')
def pickup(pizza) -> None:
    """Pickup pizza"""
    print(f'Your {pizza} is ready')


@cli.command()
@click.option('--delivery', default=False, is_flag=True)
@click.argument('pizza', nargs=1)
def order(pizza: str, delivery: bool) -> None:
    """
    Bake and delivery/pickup pizza.
    Has 2 argument:
    pizza should be from menu,
    --delivery is flag which shows you need delivery or no.
    """
    pizza_menu = get_menu()
    pizza = pizza.title()
    if pizza in pizza_menu:
        bake(pizza)
        if delivery:
            delivery_(pizza)
        else:
            pickup(pizza)
        print('Your оrder is done')
    else:
        print(f'We don\'t have item "{pizza}" on the menu')


@cli.command()
def menu() -> None:
    """
    Prints menu.
    Menu is  result get_menu function.
    """
    pizza_menu = get_menu()
    for pizza_name, pizza_obj in pizza_menu.items():
        print(f'- {pizza_name} {pizza_obj.pizza_ico}: ', end='')
        print(*pizza_obj._recipe[pizza_name], sep=', ')


def get_menu() -> dict:
    """Returns all pizzas without base class Pizza from Pizza.py"""
    pizza_menu = dict()
    blocked_classes = {'Pizza'}
    for pizza, pizza_obj in Pizza.__dict__.items():
        if isinstance(pizza_obj, type) and pizza not in blocked_classes:
            pizza_menu[pizza] = pizza_obj
    return pizza_menu


if __name__ == '__main__':
    cli()
