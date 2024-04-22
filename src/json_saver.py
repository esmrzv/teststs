import json

from src.vacancies import Vacancy
from abc import ABC, abstractmethod


class FileWorker(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def read_vacancies(self):
        pass

    @abstractmethod
    def add_vacancy(self, vacancies):
        pass

    @abstractmethod
    def delete_vacancy(self):
        pass


class JSONworker(FileWorker):
    def __init__(self, path):
        self.path = path

    def add_vacancy(self, vacancies):
        with open(self.path, 'w', encoding='utf8') as file:
            get_add = []
            for vacancy in vacancies:
                get_add.append(vacancy.__dict__)
            json.dump(get_add, file, ensure_ascii=False, indent=4)
        print('Вакансии сохранены в файл')

    def read_vacancies(self):
        """
        считывает вакансии из файла и преобразует их в список объектов
        """
        with open(self.path, "r", encoding='utf-8') as file:
            new_list = json.load(file)
            vacancies = Vacancy.vacancy_from_file(new_list)
            return vacancies

    def delete_vacancy(self):
        with open(self.path, 'w', encoding='utf8') as file:
            file.truncate(0)
