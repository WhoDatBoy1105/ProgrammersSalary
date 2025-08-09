import os
import requests
from dotenv import load_dotenv
from utils import get_receive_expected_salary


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


def predict_rub_salaries_sj(vacancies):
    expected_salary_sj = []
    for vacancy in vacancies:
        salary = vacancy
        if salary:
            if salary['currency'] != 'rub':
                continue
            else:
                get_receive_expected_salary(salary_from=salary['payment_from'], salary_to=salary['payment_to'],
                                            expected_salary=expected_salary_sj)
    return expected_salary_sj
