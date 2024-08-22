import json

import requests

from src.base_api import BaseLoadVacancies, BaseSaveFile


class HeadHunterAPI(BaseSaveFile, BaseLoadVacancies):
    """Класс получает информацию о вакансиях с сайта HeadHunter"""

    def __init__(self, file_worker: str = "../data/json_vacancies.json"):
        """Конструктор обьекта запроса инфо через API сервис"""

        self.__url = "https://api.hh.ru/vacancies"
        self.__headers = {"User-Agent": "HH-User-Agent"}
        self.__params = {"text": "", "page": 0, "per_page": 100}
        self.__vacancies = []  # конечный список, в который складываются вакансии list[dict]
        super().__init__(file_worker)

    def load_vacancies(self, keyword: str):
        """Метод загрузки данных вакансий из API сервиса"""

        self.__params["text"] = keyword
        while self.__params.get("page") != 20:
            response = requests.get(self.__url, headers=self.__headers, params=self.__params)
            vacancies = response.json()["items"]
            self.__vacancies.extend(vacancies)
            self.__params["page"] += 1

        return self.__vacancies

    def load_info_to_file(self):
        """Метод сохранения информации о вакансиях в файл формата json"""

        with open(self.file_worker, "w", encoding="utf-8") as file:
            json.dump(self.__vacancies, file, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    hh = HeadHunterAPI()
    hh.load_vacancies("Разработчик")
    hh.load_info_to_file()
