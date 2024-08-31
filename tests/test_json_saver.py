from src.json_saver import JSONSaver


def test_init_json_saver():
    init_json_saver = JSONSaver()
    assert init_json_saver.file_saver == "data/filtered_vacancies.json"


def test_add_vacancy_json_saver(test_add_vacancy, test_read_file):
    test_vacancy = test_add_vacancy

    json_saver = JSONSaver("../data/test_add_vacancy.json")
    json_saver.add_vacancy(test_vacancy)
    # json_saver.delete_vacancy(test_vacancy)
    with open("../data/test_add_vacancy.json", encoding="utf-8") as file:
        expected = test_read_file
        assert expected == file.read()


def test_delete_vacancy_json_saver(test_add_vacancy):
    test_vacancy = test_add_vacancy

    json_saver = JSONSaver("../data/test_add_vacancy.json")
    json_saver.add_vacancy(test_vacancy)
    json_saver.delete_vacancy(test_vacancy)

    with open("../data/test_add_vacancy.json", encoding="utf-8") as file:
        expected = '[]'
        assert expected == file.read()
