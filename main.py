from src.hh_ip import HeadHunterAPI
from src.functions import Functions
from src.vacancies import Vacancy


def main():
    # Создание экземпляра класса для работы с API сайтов с вакансиями
    hh_api = HeadHunterAPI()
    function = Functions()
    # Получение вакансий с hh.ru в формате JSON
    hh_vacancies = hh_api.load_vacancies(function.search_query())

    vacancies_list = Vacancy.cast_to_object_list(hh_vacancies)
    function.for_the_user(vacancies_list)


if __name__ == '__main__':
    main()
