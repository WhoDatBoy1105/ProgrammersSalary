import requests
import time
from utils import get_receive_expected_salary

SJ_MOSCOW_ID = 4
SJ_PROGRAMMING_ID = 48


def get_vacancies_sj(programming_language, super_job_token):
    headers = {
        "X-Api-App-Id": super_job_token,
    }
    params = {
        't': SJ_MOSCOW_ID,
        'catalogues': SJ_PROGRAMMING_ID,
        'keyword': programming_language,
        'count': 100,
        'page': 0
    }

    vacancies = []
    page = 0
    more = True

    while more:
        params['page'] = page
        response = requests.get('https://api.superjob.ru/2.0/vacancies/', headers=headers, params=params)
        response.raise_for_status()
        payload = response.json()

        vacancies.extend(payload['objects'])
        more = payload['more']
        page += 1

        time.sleep(0.2)

    return vacancies


def predict_rub_salaries_sj(vacancies):
    expected_salaries = []
    for vacancy in vacancies:
        if vacancy.get('currency') != 'rub':
            continue
        salary_from = vacancy['payment_from']
        salary_to = vacancy['payment_to']
        get_receive_expected_salary(salary_from, salary_to, expected_salaries)
    return expected_salaries
