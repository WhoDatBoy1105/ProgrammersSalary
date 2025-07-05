import requests
import time

programming_languages = ['JavaScript', 'Java', 'Python', 'Ruby', 'PHP', 'C++', 'C#', 'Go', 'Scala']
table_data = [
    ['Язык программирования', 'Вакансий найдено', 'Вакансий обработано', 'Средняя зарплата', ],
]


def get_a_vacancies_hh(programming_language):
    vacancies = []
    page = 0
    pages_number = 1

    while page < pages_number:
        payload = {"professional_role": 96,
                   "text": programming_language,
                   "area": 1,
                   "page": page,
                   "per_page": 100
                   }
        page_response = requests.get('https://api.hh.ru/vacancies', params=payload)
        page_response.raise_for_status()
        page_payload = page_response.json()
        pages_number = page_payload['pages']
        page += 1
        vacancies.append(page_payload['items'])
        time.sleep(1)
    vacancies = sum(vacancies, [])
    return vacancies


def predict_rub_salary_hh(vacancies):
    expected_salary_hh = []
    for vacancy in vacancies:
        salary = vacancy['salary']
        if salary is not None:
            if salary['currency'] != 'RUR':
                pass
            else:
                if salary['from'] and salary['to'] is not None:
                    average_salary = (salary['from'] + salary['to']) / 2
                    expected_salary_hh.append(average_salary)
                elif salary['from'] is not None:
                    average_salary = salary['from'] * 1.2
                    expected_salary_hh.append(average_salary)
                elif salary['to'] is not None:
                    average_salary = salary['to'] * 0.8
                    expected_salary_hh.append(average_salary)
                else:
                    pass
    return expected_salary_hh
