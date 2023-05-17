import abc
class YoloVersion(abc.ABC):
    def __init__(self, version_num):
        self.version = version_num
    
    
    @abc.abstractclassmethod
    def check_version(self):
        pass

    @abc.abstractclassmethod
    def get_version(self):
        return self.version
    

    

