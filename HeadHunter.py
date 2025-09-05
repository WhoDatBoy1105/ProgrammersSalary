import requests
import time
from utils import get_receive_expected_salary

HH_MOSCOW_ID = 1


def get_vacancies_hh(programming_language):
    vacancies = []
    page = 0
    pages_number = 1
    programmer_id = 96

    while page < pages_number:
        payload = {
            "professional_role": programmer_id,
            "text": programming_language,
            "area": HH_MOSCOW_ID,
            "page": page,
            "per_page": 100
        }
        page_response = requests.get('https://api.hh.ru/vacancies', params=payload)
        page_response.raise_for_status()
        page_payload = page_response.json()
        pages_number = page_payload['pages']
        page += 1
        vacancies.extend(page_payload['items'])
        time.sleep(1)
    return vacancies


def predict_rub_salaries_hh(vacancies):
    expected_salaries_hh = []
    for vacancy in vacancies:
        salary = vacancy['salary']
        if salary:
            if salary['currency'] != 'RUR':
                continue
            else:
                get_receive_expected_salary(salary_from=salary['from'], salary_to=salary['to'],
                                            expected_salary=expected_salaries_hh)
    return expected_salaries_hh
