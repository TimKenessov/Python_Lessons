import requests
from pages.base_api import BaseApi
import allure


class EmployeeObject(BaseApi):
    endpoint = '/employee'

    @allure.step('API. Получить список сотрудников по ID компании')
    def get_employee(self, company_id):
        params = {'company': company_id}
        self.response = requests.get(
            self.base_url + self.endpoint,
            params=params
        )
        request = self.response.json()
        return request
    
    @allure.step('API. Получить сотрудника по ID')
    def get_employee_by_id(self, employee_id):
        url = f"{self.base_url}{self.endpoint}/{employee_id}"
        self.response = requests.get(url)
        return self.response.json()
