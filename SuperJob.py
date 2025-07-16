import os
import requests
from dotenv import load_dotenv


def get_vacancies_sj(programming_language):
    vacancies = []
    id_moscow = 4
    programmer_id = 48
    load_dotenv()
    headers = {
        "X-Api-App-Id": os.getenv("SUPER_JOB_TOKEN"),
    }
    params = {
        't': id_moscow,
        'catalogues': programmer_id,
        'keyword': programming_language,
        'count': 100
    }
    page_response = requests.get('https://api.superjob.ru/2.0/vacancies/', headers=headers, params=params)
    page_response.raise_for_status()
    page_payload = page_response.json()
    vacancies.extend(page_payload['objects'])
    return vacancies


def predict_rub_salary_sj(vacancies):
    expected_salary_sj = []
    for vacancy in vacancies:
        salary = vacancy
        if salary is not None:
            if salary['currency'] != 'rub':
                pass
            else:
                if salary['payment_from'] and salary['payment_to'] is not None:
                    average_salary = (salary['payment_from'] + salary['payment_to']) / 2
                    expected_salary_sj.append(average_salary)
                elif salary['payment_from'] is not None:
                    average_salary = salary['payment_from'] * 1.2
                    expected_salary_sj.append(average_salary)
                elif salary['payment_to'] is not None:
                    average_salary = salary['payment_to'] * 0.8
                    expected_salary_sj.append(average_salary)
                else:
                    pass
    return expected_salary_sj
