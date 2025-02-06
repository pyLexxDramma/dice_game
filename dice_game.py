import random
import tkinter as tk
from tkinter import messagebox, ttk
import pickle
from PIL import Image, ImageTk


class DiceGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Симулятор игры в кости")

        self.players = []
        self.current_player = 0

        self.label = tk.Label(master, text="Введите имя игрока:")
        self.label.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()

        self.add_player_button = tk.Button(master, text="Добавить игрока", command=self.add_player)
        self.add_player_button.pack()

        self.remove_player_button = tk.Button(master, text="Удалить игрока", command=self.remove_player,
                                              state=tk.DISABLED)
        self.remove_player_button.pack()

        # Добавление выпадающего списка для выбора количества костей
        self.dice_count_label = tk.Label(master, text="Выберите количество костей (1-5):")
        self.dice_count_label.pack()

        self.dice_count = ttk.Combobox(master, values=[1, 2, 3, 4, 5], state='readonly')
        self.dice_count.current(0)  # Установка по умолчанию на 1
        self.dice_count.pack()

        self.roll_button = tk.Button(master, text="Бросить кости", command=self.roll_dice, state=tk.DISABLED)
        self.roll_button.pack()

        self.result_label = tk.Label(master, text="")
        self.result_label.pack()

        self.stats_button = tk.Button(master, text="Показать статистику", command=self.show_stats, state=tk.DISABLED)
        self.stats_button.pack()

        self.save_button = tk.Button(master, text="Сохранить игру", command=self.save_game, state=tk.DISABLED)
        self.save_button.pack()

        self.load_button = tk.Button(master, text="Загрузить игру", command=self.load_game)
        self.load_button.pack()

        # Загрузка изображений костей
        self.dice_images = [ImageTk.PhotoImage(Image.open(f'images/die{i}.png')) for i in range(1, 7)]
        self.dice_frame = tk.Frame(master)
        self.dice_frame.pack()

    def add_player(self):
        player_name = self.entry.get().strip()
        if player_name:
            self.players.append({"name": player_name, "scores": []})
            self.entry.delete(0, tk.END)
            messagebox.showinfo("Успех", f"Игрок {player_name} добавлен!")
            if len(self.players) > 0:
                self.roll_button.config(state=tk.NORMAL)
                self.remove_player_button.config(state=tk.NORMAL)
                self.stats_button.config(state=tk.NORMAL)
                self.save_button.config(state=tk.NORMAL)
        else:
            messagebox.showwarning("Ошибка", "Введите имя игрока.")

    def remove_player(self):
        if self.players:
            player_name = self.entry.get().strip()
            for player in self.players:
                if player["name"] == player_name:
                    self.players.remove(player)
                    self.entry.delete(0, tk.END)
                    messagebox.showinfo("Успех", f"Игрок {player_name} удален!")
                    if not self.players:
                        self.roll_button.config(state=tk.DISABLED)
                        self.remove_player_button.config(state=tk.DISABLED)
                        self.stats_button.config(state=tk.DISABLED)
                        self.save_button.config(state=tk.DISABLED)
                    return
            messagebox.showwarning("Ошибка", "Игрок не найден.")

    def roll_dice(self):
        if self.players:
            player = self.players[self.current_player]
            num_dice = self.dice_count.get()  # Получаем выбранное количество костей
            if not num_dice:
                messagebox.showwarning("Ошибка", "Выберите количество костей.")
                return

            num_dice = int(num_dice)  # Преобразуем в целое число
            roll_results = [random.randint(1, 6) for _ in range(num_dice)]
            total_score = sum(roll_results)
            player["scores"].append(total_score)

            self.result_label.config(
                text=f"{player['name']} бросил {num_dice} костей: {roll_results}, Сумма: {total_score}")
            self.show_dice_images(roll_results)

            # Переход к следующему игроку
            self.current_player = (self.current_player + 1) % len(self.players)
        else:
            messagebox.showwarning("Ошибка", "Добавьте хотя бы одного игрока.")

    def show_dice_images(self, roll_results):
        # Очистка предыдущих изображений
        for widget in self.dice_frame.winfo_children():
            widget.destroy()

        # Отображение новых изображений
        for result in roll_results:
            img_label = tk.Label(self.dice_frame, image=self.dice_images[result - 1])
            img_label.image = self.dice_images[result - 1]  # Сохраняем ссылку на изображение
            img_label.pack(side=tk.LEFT)

    def show_stats(self):
        if self.players:
            stats = ""
            for player in self.players:
                stats += f"{player['name']}: {player['scores']}, Общий счет: {sum(player['scores'])}\n"
            messagebox.showinfo("Статистика", stats)
        else:
            messagebox.showwarning("Ошибка", "Нет игроков для отображения статистики.")

    def save_game(self):
        with open('saved_game.pkl', 'wb') as f:
            pickle.dump(self.players, f)
            messagebox.showinfo("Успех", "Игра сохранена!")

    def load_game(self):
        try:
            with open('saved_game.pkl', 'rb') as f:
                self.players = pickle.load(f)
                self.current_player = 0
                messagebox.showinfo("Успех", "Игра загружена!")
                self.roll_button.config(state=tk.NORMAL)
                self.remove_player_button.config(state=tk.NORMAL)
                self.stats_button.config(state=tk.NORMAL)
                self.save_button.config(state=tk.NORMAL)
        except FileNotFoundError:
            messagebox.showwarning("Ошибка", "Файл сохранения не найден.")


if __name__ == "__main__":
    root = tk.Tk()
    game = DiceGame(root)
    root.mainloop()
