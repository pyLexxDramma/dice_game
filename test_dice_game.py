import unittest
from unittest.mock import patch
import tkinter as tk
from dice_game import DiceGame  # Замените на фактическое имя Вашего файла


class TestDiceGame(unittest.TestCase):
    def setUp(self):
        # Создаем экземпляр Tkinter
        self.root = tk.Tk()
        self.game = DiceGame(self.root)  # Создаем экземпляр игры

    def tearDown(self):
        self.root.destroy()  # Закрываем окно после тестов

    def test_add_player(self):
        self.game.entry.insert(0, "Player 1")
        self.game.add_player()
        self.assertEqual(len(self.game.players), 1)  # Проверяем, что игрок добавлен

    def test_remove_player(self):
        self.game.entry.insert(0, "Player 1")
        self.game.add_player()
        self.game.entry.insert(0, "Player 1")
        self.game.remove_player()
        self.assertEqual(len(self.game.players), 0)  # Проверяем, что игрок удален

    def test_roll_dice(self):
        self.game.entry.insert(0, "Player 1")
        self.game.add_player()
        self.game.roll_dice()
        self.assertGreater(len(self.game.players[0]['scores']), 0)  # Проверяем, что игрок бросил кости и есть результат

    @patch('dice_game.messagebox.showinfo')
    def test_show_stats(self, mock_showinfo):
        self.game.entry.insert(0, "Player 1")
        self.game.add_player()
        self.game.roll_dice()  # Убедимся, что игрок бросил кости
        self.game.show_stats()  # Вызываем метод без получения значения

        calls = [
            unittest.mock.call('Успех', 'Игрок Player 1 добавлен!'),  # Игнорируем первый вызов
            unittest.mock.call('Статистика', 'Player 1: [6], Общий счет: 6\n')  # Проверяем второй вызов
        ]

        mock_showinfo.assert_has_calls(calls)  # Проверяем последовательность вызовов


if __name__ == "__main__":
    unittest.main()