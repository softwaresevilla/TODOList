import os
from datetime import datetime
import csv
import logging
from typing import List, Optional
import requests
from src.models.todo import Todo

class ApiService:
    """
    Class for interacting with a TODOs API and saving the data into CSV files.

    Methods:
    - run: Executes the API service.
    - get_todo_data: Fetches data from the TODOs API.
    - write_file_data: Writes data into a CSV file.

    Example usage:
    api_service = ApiService()
    api_service.run()
    """

    def __init__(self, requests_module=requests):
        log_file = os.path.join('logs', datetime.now().strftime('%Y-%m-%d_%H-%M-%S.log'))
        logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        self.requests_module = requests_module

    def run(self):
        """
        Executes the API service. Fetches data from the TODOs API and saves the data into CSV files.
        """
        logging.info('Running ApiService')
        try:
            data = self.fetch_todo_data()
            if data:
                for todo in data:
                    self.write_todo_data_to_file(todo)
                logging.info(f'ApiService Finished. {len(data)} TODOs saved to CSV')
            else:
                logging.warning('No data fetched from the API')
        except Exception as e:
            logging.error(f'An error ocurred: {e}')

    def fetch_todo_data(self) -> Optional[List[Todo]]:
        """
        Fetches data from the TODOs API.

        Returns:
            list: A list of dictionaries representing the TODOs data.
        
        Raises:
            requests.exceptions.RequestException: If an error occurs during the http request
        """
        logging.info('Fetching data from TODOs API')
        try:
            r = self.requests_module.get('https://jsonplaceholder.typicode.com/todos/')
            r.raise_for_status()
            logging.info('Data fetched from API successfully')
            todo_list = [Todo.from_json(todo_data) for todo_data in r.json()]
            return todo_list
        except requests.exceptions.RequestException as e:
            logging.error(f'An error ocurred fetching data from API: {e}')
            return None
        
    def write_todo_data_to_file(self, todo: Todo) -> None:
        """
        Writes data into a CSV file.

        Args:
            todo (Todo): A Todo object representing the data of a TODO.

        Raises:
            FileNotFoundError: If the directory for storage is not found.
            csv.Error: If an error occurs during the CSV writing process.
            Exception: For any other unexpected error that may occur during the file writing process.
        """
        try:
            logging.info(f'Writing file to storage for TODO ID: {todo.id}')
            filename = f'./storage/{datetime.now().strftime("%Y_%m_%d")}_{todo.id}.csv'
            with open(filename, 'w', newline='', encoding='utf-8') as csv_file:
                writer = csv.DictWriter(csv_file, fieldnames=todo.to_dict().keys())
                writer.writeheader()
                writer.writerow(todo.to_dict())
            logging.info(f'File {filename} successfully written')
        except Exception as e:
            logging.error(f'An error occurred: {e}')
            raise
