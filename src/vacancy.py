class Vacancy:
    """Класс создания вакансии с параметрами"""
    __list_vacancies: list = []
    __slots__ = ("__name", "__url", "__snippet", "__salary")

    def __init__(
        self,
        name: str = "не указан",
        url: str = "не указан",
        snippet: str = "не указан",
        salary: str | None | dict = None,
    ):
        """Констркутор инициализации обьекта класса Vacancy (вакансия работника)"""
        self.__name = name
        self.__url = url
        self.__snippet = snippet

        if salary is not None:
            self.__salary = salary
            if type(salary) is str:
                salary_split = salary.split(" ")
                self.__salary = {"from": int(salary_split[0]), "to": int(salary_split[2])}
        else:
            self.__salary = {"from": 0, "to": 0}

        dict_vacancy = {"name": self.__name, "url": self.__url, "salary": self.__salary, "snippet": self.__snippet}
        self.__list_vacancies.append(dict_vacancy)

    def __ge__(self: __name__, other: __name__):
        """Метод сравнения вакансий по зарплате (верхний порог)"""
        return self.__salary["to"] >= other.__salary["to"]

    @classmethod
    def cast_to_object_list(cls, list_vacancies):
        """Метод добавления вакансий из списка вакансий"""
        for vacancies in list_vacancies:
            cls(
                name=vacancies["name"],
                url=vacancies["url"],
                salary=vacancies["salary"],
                snippet=vacancies["snippet"]["requirement"],
            )
        return cls.__list_vacancies

    @classmethod
    def filtered_salary(cls, from_salary: int = 0, to_salary: int = float("inf")):
        """Метод фильтрации вакансий по зарплате (от и до вилка)"""
        for vacancies in cls.__list_vacancies:
            if vacancies["salary"]["from"] >= from_salary and vacancies["salary"]["to"] <= to_salary:
                print(vacancies)

    @classmethod
    def list_vacancies(cls):
        return cls.__list_vacancies

    @property
    def name(self):
        return self.__name

    @property
    def url(self):
        return self.__url

    @property
    def salary(self):
        return self.__salary

    @property
    def snippet(self):
        return self.__snippet


if __name__ == "__main__":
    rob1 = Vacancy("Python Developer", "<https://hh.ru/vacancy/123456>", "Требования: опыт работы от 3 лет...")
    rob2 = Vacancy(
        "Python Developer", "<https://hh.ru/vacancy/123456>", "Требования: опыт работы от 3 лет...", "100000 - 150000"
    )
    rob3 = Vacancy(
        "Python Developer", "<https://hh.ru/vacancy/123456>", "Требования: опыт работы от 3 лет...", "110000 - 160000"
    )
    rob4 = Vacancy(
        "Python Developer", "<https://hh.ru/vacancy/123456>", "Требования: опыт работы от 3 лет...", "120000 - 170000"
    )
    rob5 = Vacancy(
        "Python Developer", "<https://hh.ru/vacancy/123456>", "Требования: опыт работы от 3 лет...", "130000 - 180000"
    )
    rob6 = Vacancy(
        "Python Developer", "<https://hh.ru/vacancy/123456>", "Требования: опыт работы от 3 лет...", "140000 - 190000"
    )
    rob7 = Vacancy(
        "Python Developer", "<https://hh.ru/vacancy/123456>", "Требования: опыт работы от 3 лет...", "150000 - 200000"
    )
    # rob8 = Vacancy("Python Developer", "<https://hh.ru/vacancy/123456>", "Требования: опыт работы от 3 лет...",
    #                "160000")
    rob9 = Vacancy(
        "Python Developer", "<https://hh.ru/vacancy/123456>", "Требования: опыт работы от 3 лет...", "0 - 220000"
    )

    print(Vacancy.list_vacancies)

    Vacancy.filtered_salary(0, 160000)

    print(Vacancy.__ge__(rob3, rob4))
