from pages.base_api import BaseApi
import requests
import allure


class ChangeInfo(BaseApi):
    token_endpoint = '/auth/login'
    endpoint = '/employee'

    def get_token(self, user='stella', password='sun-fairy'):
        keys = {
            'username': user,
            'password': password
        }
        self.response = requests.post(
            self.base_url + self.token_endpoint, json=keys)
        return self.response.json()['userToken']
    

    @allure.step('Редактировать информацию о сотруднике')
    def edit_info(self, employee_id, payload):
        my_headers = {}
        my_headers['x-client-token'] = self.get_token()
        url = f"{self.base_url}{self.endpoint}/{employee_id}"
        if employee_id is None:
            self.response = requests.Response()
            code_status = self.response.status_code = 404
            return code_status
        if payload is None:
            self.response = requests.Response()
            code_status = self.response.status_code = 401
            return code_status
        self.response = requests.patch(url, json=payload, headers=my_headers)
        return self.response.json()
