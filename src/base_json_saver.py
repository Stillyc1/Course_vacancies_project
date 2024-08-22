from abc import ABC, abstractmethod


class BaseJsonSaver:

    @staticmethod
    @abstractmethod
    def add_vacancy(vacancies):
        pass

    @abstractmethod
    def delete_vacancy(self, vacancies):
        pass
