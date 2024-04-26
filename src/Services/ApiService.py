from sys import stderr
from datetime import datetime
import csv
import requests

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

    def __init__(self):
        pass

    def run(self):
        """
        Executes the API service. Fetches data from the TODOs API and saves the data into CSV files.
        """
        print('Running ApiService', file=stderr)
        data = self.fetch_todo_data()
        for todo in data:
            self.write_todo_data_to_file(todo)
        print('ApiService Finished')

    def fetch_todo_data(self):
        """
        Fetches data from the TODOs API.

        Returns:
            list: A list of dictionaries representing the TODOs data.
        """
        print('Get data from TODOs API')
        r = requests.get('https://jsonplaceholder.typicode.com/todos/')
        if (r.status_code == 200):
            print('Success')
            return r.json()
        else:
            return None
        
    def write_todo_data_to_file(self, data):
        """
        Writes data into a CSV file.

        Args:
            data (dict): A dictionary representing the data of a TODO.

        """
        print("Writing file to storage for TODO ID: %s" % (data['id']))
        filename = './storage/{}_{}.csv'.format(datetime.now().strftime('%Y_%m_%d'), data['id'])
        with open(filename, 'w', newline='', encoding='utf-8') as csv_file:
            escritor_csv = csv.DictWriter(csv_file, fieldnames=data.keys())
            escritor_csv.writeheader()
            escritor_csv.writerow(data)
