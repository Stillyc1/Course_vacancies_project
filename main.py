from src.head_hunter_api import HeadHunterAPI
from src.vacancy import Vacancy
from src.json_saver import JSONSaver
from src.user_interaction import filter_vacancies, get_top_vacancies, get_vacancies_by_salary, print_vacancies


# # Пример работы контструктора класса с одной вакансией
# vacancy = Vacancy("Python Developer", "<https://hh.ru/vacancy/123456>", "Требования: опыт работы от 3 лет...")


def user_interaction():
    """Функция для взаимодействия с пользователем"""

    # Создание экземпляра класса для работы с API сайтов с вакансиями
    platforms = HeadHunterAPI()

    search_query = input("Введите поисковый запрос: ")

    # Получение вакансий с hh.ru в формате JSON
    hh_vacancies = platforms.load_vacancies(search_query)

    # Преобразование набора данных из JSON в список объектов
    vacancies_add_list = Vacancy.cast_to_object_list(hh_vacancies)

    # Получение стрибута списка вакансий из класса Vacancy
    vacancies_list = Vacancy.list_vacancies()

    # print([vacancies["snippet"] for vacancies in vacancies_list])

    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
    salary_range = input("Введите диапазон зарплат: ")  # Пример: 100000 - 150000

    filtered_vacancies = filter_vacancies(vacancies_list, filter_words)

    ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary_range)

    top_vacancies = get_top_vacancies(ranged_vacancies, top_n)

    print_vacancies(top_vacancies)

    # Сохранение информации о вакансиях в файл
    json_templ = JSONSaver()

    for filtered_vacancy in top_vacancies:
        vacancy_obj = Vacancy(filtered_vacancy)
        json_templ.add_vacancy(vacancy_obj)


if __name__ == "__main__":
    user_interaction()
