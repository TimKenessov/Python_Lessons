import requests
from pages.base_api import BaseApi


class NewEmployee(BaseApi):
    token_endpoint = '/auth/login'
    employee_endpoint = '/employee'
    
    def get_token(self, user = 'stella', password = 'sun-fairy'):
        keys = {
        'username': user,
        'password': password
        }
        self.response = requests.post(self.base_url + self.token_endpoint, keys)
        return self.response.json()['userToken']
    
    
    def add_new_employee(self, payload):
        my_headers = {}
        my_headers['x-client-token'] = self.get_token()
        self.response = requests.post(self.base_url + self.employee_endpoint, json=payload, headers=my_headers)
        return self.response.json()
    