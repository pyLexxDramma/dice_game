# Симулятор игры в кости

Симулятор игры в кости — это приложение, написанное на Python с использованием библиотеки Tkinter. Оно предоставляет возможность играть в кости, управлять игроками, просматривать статистику и сохранять прогресс игры.


## Функции

*   **Добавление игроков:** Вы можете добавить неограниченное количество игроков, вводя их имена в соответствующее поле.
*   **Удаление игроков:** Удаляйте ненужных игроков перед началом игры.
*   **Выбор количества костей:** Выберите количество костей для броска (от 1 до 5).
*   **Бросание костей:** Нажмите кнопку "Бросить кости", чтобы сделать ход.
*   **Просмотр статистики:** Посмотрите текущие очки всех игроков и общую сумму их баллов.
*   **Сохранение и загрузка игры:** Сохраняйте текущий прогресс игры и продолжайте позже.

## Использованные навыки

*   Программирование на Python
*   Работа с библиотекой Tkinter для создания графических интерфейсов
*   Использование модуля `random` для генерации случайных чисел
*   Применение модуля `pickle` для сериализации и десериализации данных
*   Обработка изображений с помощью библиотеки Pillow (PIL)
*   Создание и использование выпадающих списков с помощью модуля `ttk`
*   Написание юнит-тестов с использованием модуля `unittest`

## Структура проекта
├── dice_game.py # Основной файл запуска приложения.├── README.md # Этот файл с описанием проекта. └── images/ # Папка с изображениями граней костей. └── test_dice_game.py # Файл с юнит-тестами



## Тестирование

В проекте реализованы юнит-тесты с использованием модуля `unittest` для проверки основных функций приложения.

*   Файл с тестами: `test_dice_game.py`

Чтобы запустить тесты, выполните следующую команду в корневом каталоге проекта:

```bash
python -m unittest test_dice_game.py

