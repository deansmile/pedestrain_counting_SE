import yaml
class data_loader:
    @staticmethod
    def yaml_load(file_name):
        with open(file_name, 'r') as file:
            try:
                return yaml.safe_load(file)
            except:
                raise ValueError(file_name)