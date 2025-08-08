import yaml

class Config:

    url = ''
    ok = False

    @staticmethod
    def parse(path : str):
        with open(path) as stream:
            try:
                data : dict = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)

            client = data.get('client')
            if not client:
                print("No client section found in configuration file")
                return
            
            server_url = client.get('serverurl')
            if not server_url:
                print("No server url was specified")
                return
            
            Config.url = server_url
            Config.ok = True
