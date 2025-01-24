from data_loader import DataLoader
from data_analyzer import DataAnalyzer
from data_visualizer import DataVisualizer
from os import system, name


if __name__ == '__main__':
    url = 'https://github.com/mwaskom/seaborn-data/blob/master/titanic.csv?raw=true'

    # Загрузка данных
    data_loader = DataLoader(url)
    data = data_loader.load_data()

    if data is not None:
        # Создание экземпляров классов для анализа и визуализации данных
        data_analyzer = DataAnalyzer(data.copy())
        data_visualizer = DataVisualizer(data.copy())
        
        # Отчищаем консоль перед выводом
        system('cls' if name == 'nt' else 'clear')

        # Вывод основной информации о данных
        data_analyzer.get_data_info()

        # Вывод статистических характеристик
        data_analyzer.get_statistical_summary()

        # Вывод количества уникальных значений в столбце Sex
        data_analyzer.get_unique_sex_count()
        
        # Вывод количества пропущенных значений
        data_analyzer.get_missing_values()
    
        # Обработка пропущенных значений (заполнение средним значением)
        data_analyzer.handle_missing_values(strategy='mean')

        # Визуализация данных
        data_visualizer.plot_age_histogram()
        data_visualizer.plot_age_fare_scatter()

        # Группировка данных по классу пассажира и определение среднего возраста
        data_analyzer.group_by_pclass_and_get_mean_age()

        # Создание сводной таблицы
        data_analyzer.create_survival_pivot_table()

        # Выполнение дополнительных исследований (выживаемость в зависимости от кол-ва родственников на борту)
        print('Выживаемость в зависимости от количества родственников на борту:')
        family_survival = data.copy()
        family_survival['FamilySize'] = family_survival['sibsp'] + family_survival['parch'] + 1
        print(family_survival.groupby('FamilySize')['survived'].mean())

        # Формулирование гипотез
        print("\nГипотезы:")
        print('1. У пассажиров более высокого класса (1-го и 2-го) больше шансов выжить.')
        print('2. У женщин больше шансов выжить, чем у мужчин.')
        print('3. У пассажиров с большими семьями меньше шансов выжить.')
        print('4. Существует положительная корреляция между стоимостью билета и вероятностью выживания.')