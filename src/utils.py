

def filter_by_salary(vacancies):
    """
    Фильтруем зарплаты по диапазону

    """
    salary_range = input("Введите диапазон зарплат: (Пример: 100000 - 150000)")
    sorted_list = []
    list_salary_range = salary_range.split(' ')
    min_salary = int(list_salary_range[0])
    max_salary = int(list_salary_range[-1])
    for i in vacancies:
        if isinstance(i.salary, int):
            if min_salary <= i.salary <= max_salary:
                sorted_list.append(i)
        elif isinstance(i.salary, list):
            min_i, max_i = i.salary
            if min_salary <= min_i <= max_salary or min_salary <= max_i <= max_salary:
                sorted_list.append(i)
            elif min_i <= max_salary and min_salary <= max_i:
                sorted_list.append(i)
    print('\nВакансии отфильтрованы\n')
    return sorted_list


def sorted_by_salary(vacancies) -> object:
    """
    сортировка вакансий по зарплате
    """
    return sorted(vacancies, reverse=True)




