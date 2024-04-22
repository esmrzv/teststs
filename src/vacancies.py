class Vacancy:
    def __init__(self, area, name, url, salary, currency, requirements):
        self.area = area
        self.name = name
        self.url = url
        self.salary = self.get_product_price(salary)
        self.currency = self.currency(currency)
        self.requirements = self.get_info(requirements)
        self.salary_filtering = self.filter_list()

    @staticmethod
    def currency(currency):
        if isinstance(currency, str):
            return currency
        return 'валюта не указана'

    @staticmethod
    def get_info(value):
        if value:
            return value
        return 'информация не найдена'

    @classmethod
    def cast_to_object_list(cls, hh_vacancies):
        return_list = []
        for vacancy in hh_vacancies:
            name = vacancy['name']
            url = vacancy['apply_alternate_url']
            if vacancy['salary'] is None:
                salary = 0
                currency = 'Валюта не указана'
            else:
                salary = vacancy["salary"]  # зарплата
                currency = vacancy["salary"]["currency"]

            if vacancy['area']['name'] is None:
                area = 'город не указан'
            else:
                area = vacancy['area']['name']

            requirements = vacancy['snippet']['requirement']
            return_list.append(cls(area, name, url, salary, currency, requirements))
        return return_list

    @staticmethod
    def get_product_price(salary):
        """
        возвращает зарплату в формате 100000 или [100000, 150000]
        """

        if isinstance(salary, list) or isinstance(salary, int):
            return salary
        else:
            salary_from = salary.get('from', None)
            salary_to = salary.get('to', None)
            if salary_to is None and salary_from is None:
                return 0
            elif salary_to is None:
                return salary_from
            elif salary_from is None:
                return salary_to
            else:
                return [salary_from, salary_to]

    def __str__(self):
        if isinstance(self.salary, list):
            return (f'Вакансия: {self.name}\n'
                    f'Город: {self.area}\n'
                    f'Зарплата: {" - ".join(list(map(str, self.salary)))} {self.currency}\n'
                    f'Требования: {self.requirements}\n'
                    f'Ссылка на вакансию: {self.url}\n'
                    f'>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
        else:
            return (f'Вакансия: {self.name}\n'
                    f'Город: {self.area}\n'
                    f'Зарплата: {self.salary} {self.currency}\n'
                    f'Требования: {self.requirements.replace("<highlighttext>", "").replace("</highlighttext>", "")}\n'
                    f'Ссылка на вакансию: {self.url}\n'
                    f'>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

    @classmethod
    def vacancy_from_file(cls, hh_vacancy):
        data = []
        for vacancy in hh_vacancy:
            name = vacancy['name']
            area = vacancy['area']
            url = vacancy['url']
            salary = vacancy['salary']
            currency = vacancy['currency']
            requirements = vacancy['requirements']
            data.append(cls(name, area, url, salary, currency, requirements))
        return data

    def __gt__(self, other):  # – для оператора больше >
        if type(other) is type(self):
            return self.salary_filtering > other.salary_filtering
        return self.salary_filtering > other

    def filter_list(self):
        """
        функция высчитывает среднюю зп из вакансий у который указан диапазон зарплат для фильтрации по убыванию
        атрибут используется только для фильтрации!!!
        :self.salary: принимает: 100000 - 200000
        :return: 150000
        """
        if isinstance(self.salary, list):
            return (self.salary[0] + self.salary[-1]) / 2
        return self.salary
