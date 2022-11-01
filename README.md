# Pizza Projeck
### Основные файлы (сам проект)
#### Pizza
Реализовал базовый класс Pizza для всех пицц, потому что все пиццы имеют одинаковые методы и размеры. 
##### Про сравнение
Логика реализована в базовом классе, с помощью магических методов. Они основанны на перевод размера пиццы из строкового формата в численный (например, из простого 'XL' в диаметр) с помощью словаря ```size_dict```. Сделал так для того, чтобы если потребуется добавить новый размер, нужно было обновить только этот словарь и ничего не сломается. 
##### Методы и атрибуты
Метод ```dict``` выводить рецепт пиццы в виде словаря. Доступен для всех пицц.
Атрибут ```_recipe``` хранит рецепт пиццы в виде словаря. Есть как у Pizza так и у его потомков. 
Атрибут ```pizza_ico``` есть только у потомков, хранит иконку для пиццы.

#### cli
С помощью модуля click реализовал работу cli в консоли.
##### Методы и атрибуты
Мeтоды ```bake```, ```delivery_```, ```pickup``` просто выводят соответствующий процесс. Данные методы вызываются только в методе ```order```. К методу ```delivery_``` добавлено нижнее подчеркивание, чтобы обращаться к нему в методе ```order```, так как у ```order``` есть флаг ```--delivery```. 

Метод ```get_menu``` возвращает словарь с рецептами всех пицц кроме Pizza. Основан на обходе словаря ```Pizza.__dict__``` и сравнении каждого значения из пары ключ-значение с типом ```type```. Сделал так, чтобы в случае добавления новой пиццы не изменять код в cli.py. По сути данный метод является вспомогательным для методов ```menu``` и ```order```.

Метод ```menu``` выводит доступное меню. Работа основана на методе ```get_menu```. Для обращения в терминале нужно использовать команду ```python cli.py menu```.
Пример работы:
```
python cli.py menu
- Margherita 🧀: tomato sauce, mozzarella, tomatoes
- Pepperoni 🍕: tomato sauce, mozzarella, pepperoni
- Hawaiian 🍍: tomato sauce, mozzarella, chicken, pineapples
```

Метод ```order``` позволяет осуществлять заказ через терминал. На вход принимает один аргумент: пиццу из меню. Если добавить пиццу, отсутствующую в меню, выведет сообщение ```We don't have item "argument" on the menu``` и закончит работу, без поднятия ошибки. Так же можно добавить флаг ```--delivery```, который отвечает за наличие доставки в заказе. Если его нет заказ не будут доставлять, и он будет ждать вас в ресторане.
Пример работы с доставкой (с флагом ```--delivery```):
```
python cli.py order pepperoni --delivery
Your Pepperoni is being baked
Stage: bake, Time: 8c
👨🍳 baked in 8с!
Your Pepperoni is being deliveried
Stage: delivery, Time: 6c
🛵 deliveried in 6с!
Your оrder is done
```
Пример работы без доставки (без флага):
```
python cli.py order Hawaiian
Your Hawaiian is being baked
Stage: bake, Time: 6c
👨🍳 baked in 6с!
Your Hawaiian is ready 
Stage: pickup, Time: 6c
🏠 picked up in 6с!
Your оrder is done
```
Пример при заказе не существующей пиццы:
```
python cli.py order Sicilian
We don't have item "Sicilian" on the menu
```

Декоратор ```log``` выводит динамический таймер времени работы функции (в нашем случае стадии приготовления заказа) в виде ```Stage: {func.__name__}, Time: {time}c ```. Время берётся на рандом (``` time = randint(1, 9)```), секунда длиться 0.2c (```sleep(0.2)```) для ускорения работы. Так же принимает на вход аргумент вида ```'some text {} some text'``` и пишет время обработки данной стадии заказа в конце этой стадии вместо ```'{}'```. 

Пример работы ```order``` без декорирования ```bake```, ```delivery_```, ```pickup```:
```
python cli.py order Hawaiian
Your Hawaiian is being baked
Your Hawaiian is ready
Your оrder is done
```
Пример работы того же запроса с декорированием:
```
python cli.py order Hawaiian
Your Hawaiian is being baked
Stage: bake, Time: 6c
👨🍳 baked in 6с!
Your Hawaiian is ready 
Stage: pickup, Time: 6c
🏠 picked up in 6с!
Your оrder is done
```

### Тестирование
Тестирование проводилось с помощью ```pytest```. Всего было написано 18 тестов про каждый будет написано ниже. 
#### Проверка линтерами
Решил начать с того, что пакет ```click``` в cli не проходил проверку без 'заглушки'. Понадобилось установить ```types-click```:
```
pip install types-click
```
#### Тестирование логики без вывода в терминал
Это все тестовые функции из файла test_Pizza, кроме ```test_dict```, который тестирует ```Pizza.dict()```. Данные тесты написанны с помощью ```assert```, без какой-либо хитрости. Так работают 10 тестов.

#### Проверка логики с ```print```
Тестирование функций с выводом в терминал, но не работающих на прямую с ```click```, реализовано с помощью метода ```pytest``` [capsys](https://docs.pytest.org/en/7.1.x/how-to/capture-stdout-stderr.html).

#### Проверка логики ```click```
Тестирование функций с выводом в терминал, работающих на прямую с ```click```, реализовано с помощью метода ```click``` [CliRunner](https://click.palletsprojects.com/en/8.1.x/testing/).

#### Запуск тестов в терлинале
Тестирование Pizza осуществляется с помощью файла test_Pizza. Первая команда создаст HTML отчет в директории htmlcov. Вторая запишет результат работы тестов в test_coverage/Pizza_cov.txt: 
```
python -m pytest -v test_Pizza.py --cov=Pizza --cov-report html 
python -m pytest -v test_Pizza.py --cov=Pizza > ./test_coverage/Pizza_cov.txt
```
Тестирование cli осуществляется с помощью файла test_cli. Первая команда создаст HTML отчет в директории htmlcov. Вторая запишет результат работы тестов в test_coverage/cli_cov.txt: 
```
python -m pytest -v test_cli.py --cov=cli --cov-report html
python -m pytest -v test_cli.py --cov=cli > ./test_coverage/cli_cov.txt
```

