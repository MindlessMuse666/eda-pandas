import pandas as pd


class DataAnalyzer:
    """
    Класс для анализа данных.
    """
    def __init__(self, data: pd.DataFrame):
        self.data = data


    def get_data_info(self):
        """
        Выводит общую информацию о данных, 
        включая типы данных и наличие пропущенных значений.
        """
        print('Информация о данных:')
        print(self.data.info())


    def get_statistical_summary(self):
        """
        Выводит основные статистические характеристики числовых данных.
        """
        print(
            '\nОсновные статистические характеристики:\n',
            self.data.describe()
        )
        

    def get_unique_sex_count(self):
        """
        Выводит количество уникальных значений в столбце 'Sex'.
        """
        print(
            '\nКоличество уникальных значений в столбце \"sex\":\n',
            self.data['sex'].value_counts()
        )


    def get_missing_values(self):
        """
        Оценивает количество пропущенных значений в каждом столбце.
        """
        print(
            '\nКоличество пропущенных значений в каждом столбце:\n',
            self.data.isnull().sum()
        )


    def handle_missing_values(self, strategy='mean'):
        """
        Обрабатывает пропущенные значения в данных.

        Args:
            strategy (str): Стратегия обработки пропущенных значений ('mean', 'median', 'drop').
        """
        if strategy == 'mean':
            for column in self.data.select_dtypes(include=['number']).columns:
                self.data[column] = self.data[column].fillna(self.data[column].mean())
        elif strategy == 'median':
             for column in self.data.select_dtypes(include=['number']).columns:
                self.data[column] = self.data[column].fillna(self.data[column].median())
        elif strategy == 'drop':
            self.data = self.data.dropna()
        else:
            raise ValueError('\nНекорректная стратегия. Выберите \"mean\", \"median\", или \"drop\".')

        print('\nОбработка пропущенных значений завершена.')


    def group_by_pclass_and_get_mean_age(self):
        """
        Группирует данные по классу пассажира и определяет средний возраст в каждой группе.

        Returns:
            pandas.DataFrame: Сгруппированные данные по классу пассажира.
        """
        grouped_data = self.data.groupby('pclass')['age'].mean()
        
        print(
            'Средний возраст пассажиров каждого класса:\n',
            grouped_data
        )
        
        return grouped_data


    def create_survival_pivot_table(self):
        """
        Создает сводную таблицу, отображающую среднюю выживаемость для каждого класса и пола.

        Returns:
            pandas.DataFrame: Сводная таблица.
        """
        pivot_table = self.data.pivot_table(index='pclass', columns='sex', values='survived', aggfunc='mean')
        
        print(
            'Таблица средней выживаемости для каждого класса и пола:\n',
            pivot_table
        )
        
        return pivot_table
