import json

from src.base_json_saver import BaseJsonSaver
from src.vacancy import Vacancy


class JSONSaver(BaseJsonSaver):
    """Класс для сохранения, добавления и изменения вакансий в json-файле"""

    def __init__(self, file_saver: str = "data/filtered_vacancies.json"):
        """Констркутор, инициализирует путь до файла (для работы с ним)"""
        self.file_saver = file_saver

    def add_vacancy(self, vacancies: Vacancy | list):
        """Метод добавления вакансий в файл json"""
        with open(self.file_saver, "r+", encoding="utf-8") as file:
            try:
                json.load(file)
            except json.JSONDecodeError:
                file.write("[]")

        with open(self.file_saver, "r+", encoding="utf-8") as file:
            json_file_vacancies = json.load(file)

            dict_vacancy = {
                "name": vacancies.name,
                "url": vacancies.url,
                "salary": vacancies.salary,
                "snippet": vacancies.snippet,
            }

            if dict_vacancy not in json_file_vacancies:
                json_file_vacancies.append(dict_vacancy)

        with open(self.file_saver, "w", encoding="utf-8") as file:
            json.dump(json_file_vacancies, file, ensure_ascii=False, indent=4)

    def delete_vacancy(self, vacancies: Vacancy):
        """Метод удаления вакансий из файла json"""
        with open(self.file_saver, "r+", encoding="utf-8") as file:
            json_file_vacancies = json.load(file)

            dict_vacancy = {
                "name": vacancies.name,
                "url": vacancies.url,
                "salary": vacancies.salary,
                "snippet": vacancies.snippet,
            }

            if dict_vacancy in json_file_vacancies:
                json_file_vacancies.remove(dict_vacancy)

        with open(self.file_saver, "w", encoding="utf-8") as file:
            json.dump(json_file_vacancies, file, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    vacancys = Vacancy("Python Developer", "<https://hh.ru/vacancy/123456>", "Требования: опыт работы от 3 лет...")

    json_saver = JSONSaver("../data/filtered_vacancies.json")
    json_saver.add_vacancy(vacancys)
    json_saver.delete_vacancy(vacancys)
