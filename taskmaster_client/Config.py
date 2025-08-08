import yaml

class Config:

    url = ''
    ok = False

    @staticmethod
    def parse(path : str):
        try:
            with open(path) as stream:
                try:
                    data : dict = yaml.safe_load(stream)
                except yaml.YAMLError as exc:
                    print(exc)
        except FileNotFoundError as exc:
            print(f"Configuration file not found: {path}")
            return
        except Exception as e:
            print(f"Unexpected error while opening config file: {e}")
            return
                

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
     
