import os
import requests
from utils import get_receive_expected_salary

SJ_MOSCOW_ID = 4
SJ_PROGRAMMING_ID = 48


def get_vacancies_sj(programming_language):
    headers = {
        "X-Api-App-Id": os.getenv("SUPER_JOB_TOKEN"),
    }
    params = {
        't': SJ_MOSCOW_ID,  # id Москвы
        'catalogues': SJ_PROGRAMMING_ID,  # Каталог "Программисты"
        'keyword': programming_language,
        'count': 100
    }
    response = requests.get('https://api.superjob.ru/2.0/vacancies/', headers=headers, params=params)
    response.raise_for_status()
    payload = response.json()
    return payload['objects']  # сразу возвращаем список вакансий


def predict_rub_salaries_sj(vacancies):
    expected_salaries = []
    for vacancy in vacancies:
        if vacancy.get('currency') != 'rub':
            continue
        salary_from = vacancy['payment_from']
        salary_to = vacancy['payment_to']
        get_receive_expected_salary(salary_from, salary_to, expected_salaries)
    return expected_salaries
