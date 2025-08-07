import requests

class HTTPComm:
    
    def __init__(self, port):
        url ='http://localhost:8000'
        response = requests.get(url)

        if response.status_code == 200:
            print('Server available')
            self.http_status = 'OK'
        else:
            print('something went wrong: ' + str(response.status_code))
            self.http_status = 'KO'