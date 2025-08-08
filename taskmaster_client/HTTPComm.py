import requests
from requests.exceptions import RequestException

#Class that handles HTTP Comm for the client, sends HTTP requests to server

class HTTPComm:

    def __init__(self, port):

        #ip and port configuration i believe it will have to be parsed from config file
        self.url = f'http://localhost:{port}/'

        #We try one get request at startup to check server is up
        try:
            response = requests.get(self.url)
            response.raise_for_status()
            self.http_status = 'OK'
            print(f"Response status code: {response.status_code}")

        except requests.exceptions.HTTPError as e:
            print(f"HTTP error occurred: {e}")
            print(f"Status code: {e.response.status_code}")
            self.http_status = 'KO'

        except RequestException as e:
            print(f"Request failed: {e}")
            self.http_status = 'KO'

    def send(self, action: str, process: str = ''):
        #We set the url of the http request. 
        #If action is not bound to a process (status and reload), then url goes like this -> eg: http://localhost:8000/status/
        #But if it is bound to a process (start, stop, restart) -> http://localhost:8000/start/nginx/
        url = self.url + action + '/' + process

        #blocking behaviour, as I believe it should be
        response = requests.post(url)

        print(response.text)