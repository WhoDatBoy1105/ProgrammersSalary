from terminaltables import AsciiTable
from copy import deepcopy
from SuperJob import get_vacancies_sj, predict_rub_salaries_sj
from HeadHunter import get_vacancies_hh, predict_rub_salaries_hh

PROGRAMMING_LANGUAGES = ['JavaScript', 'Java', 'Python', 'Ruby', 'PHP', 'C++', 'C#', 'Go', 'Scala']
SALARY_TABLE = [
    ['Язык программирования', 'Вакансий найдено', 'Вакансий обработано', 'Средняя зарплата', ],
]


def get_average_salary_hh():
    table_data_hh = deepcopy(SALARY_TABLE)
    table_hh = AsciiTable(table_data_hh, 'HeadHunter Moscow')
    for programming_language in PROGRAMMING_LANGUAGES:
        vacancies = get_vacancies_hh(programming_language)
        expected_salary_hh = predict_rub_salaries_hh(vacancies)
        if len(expected_salary_hh) == 0:
            pass
        else:
            average_salary_hh = [programming_language, len(vacancies),
                                 len(expected_salary_hh),
                                 int(sum(expected_salary_hh) / len(expected_salary_hh))
                                 ]
            table_data_hh.append(average_salary_hh)
    print(table_hh.table)


def get_average_salary_sj():
    table_data_sj = deepcopy(SALARY_TABLE)
    table_sj = AsciiTable(table_data_sj, 'SuperJob Moscow')
    for programming_language in PROGRAMMING_LANGUAGES:
        vacancies = get_vacancies_sj(programming_language)
        expected_salary_sj = predict_rub_salaries_sj(vacancies)
        if len(expected_salary_sj) == 0:
            pass
        else:
            average_salary_sj = [programming_language, len(vacancies),
                                 len(expected_salary_sj),
                                 int(sum(expected_salary_sj) / len(expected_salary_sj))
                                 ]

            table_data_sj.append(average_salary_sj)
    print(table_sj.table)


def main():
    get_average_salary_hh()
    get_average_salary_sj()


if __name__ == '__main__':
    main()
