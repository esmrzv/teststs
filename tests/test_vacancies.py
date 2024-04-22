import pytest
from src.vacancies import Vacancy

content = [{'area': {"name": 'Москва'},
            'name': 'разработчик',
            'apply_alternate_url': 'ссылка',
            "salary": {"from": 70000, "to": 74000, "currency": "RUR"},
            "snippet": {"requirement": "Способен работать в команде."}
            }]


@pytest.fixture()
def vacancy():
    return Vacancy.cast_to_object_list(content)


def test_vacancies(vacancy):
    assert vacancy[0].area == 'Москва'
    assert vacancy[0].name == 'разработчик'

    assert vacancy[0].url == 'ссылка'
    assert vacancy[0].salary == [70000, 74000]
    assert vacancy[0].currency == 'RUR'
    assert vacancy[0].requirements == 'Способен работать в команде.'


content2 = [{
    'name': "Москва",
    'area': 'Москва',
    'url': 'https://hh.ru/applicant/vacancy_response?vacancyId=94354526',
    "salary": [
        100000,
        150000
    ],
    'currency': "RUR",
    'requirements': 'Способен работать в команде.'
}]


@pytest.fixture()
def vacancy_2():
    return Vacancy.vacancy_from_file(content2)


def test_vacancy_2(vacancy_2):
    assert vacancy_2[0].area == 'Москва'
    assert vacancy_2[0].name == 'Москва'
    assert vacancy_2[0].url == 'https://hh.ru/applicant/vacancy_response?vacancyId=94354526'
    assert vacancy_2[0].salary == [100000, 150000]
    assert vacancy_2[0].currency == 'RUR'
    assert vacancy_2[0].requirements == 'Способен работать в команде.'
