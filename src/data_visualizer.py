import matplotlib.pyplot as plt
import pandas as pd


class DataVisualizer:
    """
    Класс для визуализации данных.
    """
    def __init__(self, data: pd.DataFrame):
        self.data = data


    def plot_age_histogram(self):
        """
        Строит гистограмму возрастов пассажиров.
        """
        plt.figure(figsize=(10, 6), num='Гистограмма распределения пассажиров по возрасту')
        plt.hist(self.data['age'].dropna(), bins=30, color='skyblue', edgecolor='black')
        plt.title('Распределение пассажиров по возрасту', pad=20)
        plt.xlabel('Возраст')
        plt.ylabel('Частота')
        plt.grid(axis='y', alpha=0.75)
        plt.show()


    def plot_age_fare_scatter(self):
        """
        Строит диаграмму рассеяния для сравнения возраста и цены билета.
        """
        plt.figure(figsize=(10, 6), num='Диаграмма рассеяния сравнения возраста и цены билета')
        plt.scatter(self.data['age'], self.data['fare'], color='coral', alpha=0.6)
        plt.title('Возраст в зависимости от цены билета', pad=20)
        plt.xlabel('Возраст')
        plt.ylabel('Цена билета')
        plt.grid(True)
        plt.show()