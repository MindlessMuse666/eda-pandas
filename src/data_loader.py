import pandas as pd


class DataLoader:
    """
    Класс для загрузки данных.
    """
    def __init__(self, url: str):
        self.url = url
        self.data = None


    def load_data(self) -> pd.DataFrame:
        """
        Загружает данные из CSV файла по URL.

        Returns:
            pandas.DataFrame: Загруженные данные.
        """
        try:
            self.data = pd.read_csv(self.url)
            return self.data
        except Exception as e:
            print(f'Ошибка загрузки данных: {e}')
            return None