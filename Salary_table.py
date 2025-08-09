from dotenv import load_dotenv
from terminaltables import AsciiTable
from copy import deepcopy
from SuperJob import get_vacancies_sj, predict_rub_salaries_sj
from HeadHunter import get_vacancies_hh, predict_rub_salaries_hh

PROGRAMMING_LANGUAGES = ['JavaScript', 'Java', 'Python', 'Ruby', 'PHP', 'C++', 'C#', 'Go', 'Scala']
SALARY_TABLE = [
    ['Язык программирования', 'Вакансий найдено', 'Вакансий обработано', 'Средняя зарплата'],
]


def create_salary_table(vacancies_getter, salary_predictor, title):
    table_data = deepcopy(SALARY_TABLE)
    for programming_language in PROGRAMMING_LANGUAGES:
        vacancies = vacancies_getter(programming_language)
        predicted_salaries = salary_predictor(vacancies)
        if not predicted_salaries:
            continue
        average_salary = int(sum(predicted_salaries) / len(predicted_salaries))
        row = [
            programming_language,
            len(vacancies),
            len(predicted_salaries),
            average_salary
        ]
        table_data.append(row)
    table = AsciiTable(table_data, title)
    return table.table


def print_hh_salary_table():
    print(create_salary_table(get_vacancies_hh, predict_rub_salaries_hh, 'HeadHunter Moscow'))


def print_sj_salary_table():
    print(create_salary_table(get_vacancies_sj, predict_rub_salaries_sj, 'SuperJob Moscow'))


def main():
    load_dotenv()
    print_hh_salary_table()
    print_sj_salary_table()


if __name__ == '__main__':
    main()
