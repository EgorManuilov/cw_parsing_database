import os

from config import config
from src.db_manager import DBManager
from src.utils import get_hh_employers, get_hh_vacancies, create_database, save_data_to_database


def main():
    employer_ids = ['2748',  # Ростелеком
                    '1740',  # Яндекс
                    '1057',  # Касперский
                    '78638',  # Тинькофф
                    '3776',  # МТС
                    '15478',  # VK
                    '1942330',  # Пятерочка
                    '49357',  # Магнит
                    '2343',  # Спортмастер
                    '39305']  # Газпром

    params = config()

    url_queries = os.path.join("src", "queries.sql")

    employer_data = get_hh_employers(employer_ids)
    vacancies_data = get_hh_vacancies(employer_ids)
    create_database('headhunter', params)
    save_data_to_database(employer_data, vacancies_data, 'headhunter', params)
    db_manager = DBManager('headhunter', params, url_queries)

    while True:
        select = input(
            "1 - Получить список всех компаний и количество вакансий у каждой компании\n"
            "2 - Получить список всех вакансий с указанием названий компании и вакансии, зарплаты, ссылки на вакансию\n"
            "3 - Получить среднюю зарплату по вакансиям\n"
            "4 - Получает список всех вакансий, у которых зарплата выше средней по всем вакансиям\n"
            "5 - Получить список всех вакансий, в названии которых содержатся ключевое слово\n"
            "0 - Для выхода\n"
        )

        if select == "0":
            break
        elif select == "1":
            db_manager.get_companies_and_vacancies_count()
        elif select == "2":
            db_manager.get_all_vacancies()
        elif select == "3":
            db_manager.get_avg_salary()
        elif select == "4":
            db_manager.get_vacancies_with_higher_salary()
        elif select == "5":
            key_word = input("Введите ключевое слово\n")
            db_manager.get_vacancies_with_keyword(key_word)


if __name__ == '__main__':
    main()
