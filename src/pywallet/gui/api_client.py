import requests
from pywallet.gui.token_manager import TokenManager

class ApiClient :

    BASE_URL = "http://127.0.0.1:8000"

    @staticmethod
    def create_user(data):
        response = requests.post(
            url = f"{ApiClient.BASE_URL}/user",
            json = data
        )

        if response.status_code == 200 :
            token = TokenManager()
            response_data = response.json()
            access_token = response_data["access token"]
            refresh_token = response_data["refresh token"]
            username = response_data["username"]
            token.set_token(access_token , refresh_token , username)

        else :
            return response.status_code

        return response

    @staticmethod
    def login_user(data):
        response = requests.post(
            url = f"{ApiClient.BASE_URL}/login",
            json = data
        )

        if response.status_code == 200 :
            response_data = response.json()
            access_token = response_data["access token"]
            refresh_token = response_data['refresh token']
            username = response_data["username"]
            TokenManager.set_token(access_token , refresh_token , username)

        else :
            return response.status_code

        return response

