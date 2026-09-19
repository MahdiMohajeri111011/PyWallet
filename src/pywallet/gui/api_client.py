import requests

class ApiClient :

    BASE_URL = "http://127.0.0.1:8000"

    @staticmethod
    def create_user(data):
        respone = requests.post(
            url = f"{ApiClient.BASE_URL}/user",
            json = data
        )

        return respone

    @staticmethod
    def login_user(data):
        response = requests.post(
            url = f"{ApiClient.BASE_URL}/login",
            json = data
        )

        return response

