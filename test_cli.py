import re

import pytest
import cli
from click.testing import CliRunner


def test_bake(capsys):
    text = 'Your pizza is being baked\n'
    cli.bake('pizza')
    output = capsys.readouterr()
    time = output.out[-4]
    for i in range(int(time)+1):
        text += f'Stage: bake, Time: {i}c\r'
    text += f'\n\r👨‍🍳 baked in {time}с!\n'
    assert output.out == text


def test_delivery(capsys):
    text = 'Your pizza is being deliveried\n'
    cli.delivery_('pizza')
    output = capsys.readouterr()
    time = output.out[-4]
    for i in range(int(time)+1):
        text += f'Stage: delivery, Time: {i}c\r'
    text += f'\n\r🛵 deliveried in {time}с!\n'
    assert output.out == text


def test_pickup(capsys):
    text = 'Your pizza is ready\n'
    cli.pickup('pizza')
    output = capsys.readouterr()
    time = output.out[-4]
    for i in range(int(time)+1):
        text += f'Stage: pickup, Time: {i}c\r'
    text += f'\n\r🏠 picked up in {time}с!\n'
    assert output.out == text


def test_order_with_delivery():
    runner = CliRunner()
    result = runner.invoke(cli.order, ['Margherita', '--delivery'])
    output = result.output
    re_time_bake = r'bake, Time: \d'
    re_time_delivery = r'delivery, Time: \d'

    re.findall(re_time_bake, output)

    text_bake = 'Your Margherita is being baked\n'
    time_bake = re.findall(re_time_bake, output)[-1][-1]
    for i in range(int(time_bake)+1):
        text_bake += f'Stage: bake, Time: {i}c\r'
    text_bake += f'\n\r👨‍🍳 baked in {time_bake}с!\n'

    text_delivery = 'Your Margherita is being deliveried\n'
    time_delivery = re.findall(re_time_delivery, output)[-1][-1]
    for i in range(int(time_delivery)+1):
        text_delivery += f'Stage: delivery, Time: {i}c\r'
    text_delivery += f'\n\r🛵 deliveried in {time_delivery}с!\n'

    text_order = 'Your оrder is done\n'
    text = text_bake + text_delivery + text_order

    assert result.exit_code == 0
    assert output == text


def test_order_without_delivery(capsys):
    runner = CliRunner()
    result = runner.invoke(cli.order, ['Margherita'])

    output = result.output
    re_time_bake = r'bake, Time: \d'
    re_time_delivery = r'pickup, Time: \d'

    re.findall(re_time_bake, output)

    text_bake = 'Your Margherita is being baked\n'
    time_bake = re.findall(re_time_bake, output)[-1][-1]
    for i in range(int(time_bake)+1):
        text_bake += f'Stage: bake, Time: {i}c\r'
    text_bake += f'\n\r👨‍🍳 baked in {time_bake}с!\n'

    text_pickup = 'Your Margherita is ready\n'
    time_pickup = re.findall(re_time_delivery, output)[-1][-1]
    for i in range(int(time_pickup)+1):
        text_pickup += f'Stage: pickup, Time: {i}c\r'
    text_pickup += f'\n\r🏠 picked up in {time_pickup}с!\n'

    text_order = 'Your оrder is done\n'
    text = text_bake + text_pickup + text_order
    assert result.exit_code == 0
    assert output == text


def test_order_unexist_pizza():
    runner = CliRunner()
    result = runner.invoke(cli.order, ['pizza', '--delivery'])
    text = 'We don\'t have item "Pizza" on the menu\n'
    assert result.exit_code == 0
    assert result.output == text


def test_menu():
    text = (
        '- Margherita 🧀: tomato sauce, mozzarella, tomatoes\n'
        '- Pepperoni 🍕: tomato sauce, mozzarella, pepperoni\n'
        '- Hawaiian 🍍: tomato sauce, mozzarella, chicken, pineapples\n'
    )
    runner = CliRunner()
    result = runner.invoke(cli.menu, [])
    assert result.exit_code == 0
    assert result.output == text


if __name__ == '__main__':
    pytest.main(['test_cli.py', '-v'])
