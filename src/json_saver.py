import json

from src.base_json_saver import BaseJsonSaver
from src.vacancy import Vacancy


class JSONSaver(BaseJsonSaver):

    @staticmethod
    def add_vacancy(vacancies: Vacancy):
        with open("../data/filtered_vacancies.json", "a", encoding="utf-8") as file:

            dict_vacancy = {
                "name": vacancies.name,
                "url": vacancies.url,
                "salary": vacancies.salary,
                "snippet": vacancies.snippet}
            json.dump(dict_vacancy, file, ensure_ascii=False, indent=4)

    def delete_vacancy(self, vacancies):
        pass


if __name__ == "__main__":
    vacancys = Vacancy("Python Developer", "<https://hh.ru/vacancy/123456>", "Требования: опыт работы от 3 лет...")

    json_saver = JSONSaver()
    json_saver.add_vacancy(vacancys)
    json_saver.delete_vacancy(vacancys)
