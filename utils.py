def get_receive_expected_salary(salary_from, salary_to, expected_salary):
    average_salary = None
    if salary_from and salary_to:
        average_salary = (salary_from + salary_to) / 2
    elif salary_from:
        average_salary = salary_from * 1.2
    elif salary_to:
        average_salary = salary_to * 0.8

    if average_salary is not None:
        expected_salary.append(average_salary)
