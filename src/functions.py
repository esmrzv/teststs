import os.path

from config import ROOT_DIR
from src.utils import sorted_by_salary, filter_by_salary
from src.json_saver import JSONworker


class Functions:
    def __init__(self):
        pass

    @staticmethod
    def search_query():
        query = input('Введите запрос для поиска вакансии: ')
        return query

    @staticmethod
    def get_top_vacancies_by_salary(vacancies):
        answer = int(input('Какое количество вакансий вам выдать?: '))
        sorted_vacancies = sorted_by_salary(vacancies)
        for vacancy in sorted_vacancies[0: answer]:
            print(vacancy)

    @staticmethod
    def get_vacancies_with_keyword(vacancies):
        keywords = input("Введите ключевое слово: ").split()
        reserve_list_v = vacancies
        for word in keywords:
            list_vacancies = []
            for i in vacancies:
                if word.lower() in i.requirements.lower():
                    list_vacancies.append(i)
            if len(list_vacancies) == 0:
                print('Вакансии с такими ключевыми словами не найдены!')
                return reserve_list_v
            else:
                vacancies = list_vacancies
            return vacancies


    @staticmethod
    def for_the_user(vacancies):
        while True:
            print(f'Кнопки навигации:\n'
                  f'1. Вывести вакансии на экран\n'
                  f'2. Фильтрация вакансии по ключевому слову\n'
                  f'3. Фильтрация вакансии по заработной плате\n'
                  f'4. Фильтрация зарплаты по убыванию\n'
                  f'5. Вывод top/N вакансий\n'
                  f'6. сохранить информацию о вакансиях в файл\n'
                  f'7. считатать данные из файла\n'
                  f'8. удалить все данные в файле\n'
                  f'нажите "стоп" для завершения')
            ans = input()
            if ans in ('stop', "стоп"):
                break
            try:
                answer = int(ans)
                if answer == 1:
                    for i in vacancies:
                        print(i)
                elif answer == 2:
                    vacancies = Functions.get_vacancies_with_keyword(vacancies)
                elif answer == 3:
                    vacancies = filter_by_salary(vacancies)
                elif answer == 4:
                    vacancies = sorted_by_salary(vacancies)
                elif answer == 5:
                    Functions.get_top_vacancies_by_salary(vacancies)
                elif answer == 6:
                    file_name = input('Ведите название файла для добавления: ')
                    path = os.path.join(ROOT_DIR, 'data', file_name + '.' + str('json'))
                    json_saver = JSONworker(path)
                    json_saver.add_vacancy(vacancies)
                elif answer == 7:
                    file_name = input('Введите название файла для считывания данные из файла: ')
                    path = os.path.join(ROOT_DIR, 'data', file_name + '.' + str('json'))
                    json_saver = JSONworker(path)
                    json_saver.read_vacancies()
                elif answer == 8:
                    file_name = input('Введите название файла для удаления данных: ')
                    path = os.path.join(ROOT_DIR, 'data', file_name + '.' + str('json'))
                    json_saver = JSONworker(path)
                    json_saver.delete_vacancy()
            except ValueError:
                print('Введите цифры от 1-9')







