import abc
class Model(abc.ABC):
    def __init__(self):
        pass    

    @abc.abstractclassmethod
    def predict(self):
        pass
    

    