import requests


class BaseApi:
    base_url = 'https://x-clients-be.onrender.com/'
    endpoint: str
    response: requests.Response

    def check_status_is(self, status):
        return self.response.status_code == status
