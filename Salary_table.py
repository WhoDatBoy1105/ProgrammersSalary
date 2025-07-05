from terminaltables import AsciiTable
from SuperJob import get_a_vacancies_sj, predict_rub_salary_sj
from HeadHunter import get_a_vacancies_hh, predict_rub_salary_hh

programming_languages = ['JavaScript', 'Java', 'Python', 'Ruby', 'PHP', 'C++', 'C#', 'Go', 'Scala']
table_data = [
    ['Язык программирования', 'Вакансий найдено', 'Вакансий обработано', 'Средняя зарплата', ],
]


def get_average_salary_hh():
    for programming_language in programming_languages:
        vacancies = get_a_vacancies_hh(programming_language)
        expected_salary_hh = predict_rub_salary_hh(vacancies)
        if len(expected_salary_hh) == 0:
            pass
        else:
            average_salary = [programming_language, len(vacancies),
                              len(expected_salary_hh),
                              int(sum(expected_salary_hh) / len(expected_salary_hh))
                              ]
            table_data.append(average_salary)
    table = AsciiTable(table_data, 'HeadHunter Moscow')
    print(table.table)


def get_average_salary_sj():
    for programming_language in programming_languages:
        vacancies = get_a_vacancies_sj(programming_language)
        expected_salary_sj = predict_rub_salary_sj(vacancies)
        if len(expected_salary_sj) == 0:
            pass
        else:
            average_salary = [programming_language, len(vacancies),
                              len(expected_salary_sj),
                              int(sum(expected_salary_sj) / len(expected_salary_sj))
                              ]
            table_data.append(average_salary)
    table = AsciiTable(table_data, 'SuperJob Moscow')
    print(table.table)


def main():
    get_average_salary_sj()


if __name__ == '__main__':
    main()
