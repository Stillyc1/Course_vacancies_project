import json

import requests
from src.base_api import BaseSaveFile, BaseLoadVacancies


class HeadHunterAPI(BaseSaveFile, BaseLoadVacancies):

    def __init__(self, file_worker="../data/json_vacancies.json"):
        self.url = 'https://api.hh.ru/vacancies'
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': '', 'page': 0, 'per_page': 100}
        self.vacancies = []
        super().__init__(file_worker)

    def load_vacancies(self, keyword):
        self.params['text'] = keyword
        while self.params.get('page') != 20:
            response = requests.get(self.url, headers=self.headers, params=self.params)
            vacancies = response.json()['items']
            self.vacancies.extend(vacancies)
            self.params['page'] += 1

    def load_info_to_file(self):
        with open(self.file_worker, "w", encoding="utf-8") as file:
            json.dump(self.vacancies, file, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    hh = HeadHunterAPI()
    hh.load_vacancies("Python")
    hh.load_info_to_file()

