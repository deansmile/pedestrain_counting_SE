import abc
class Image(abc.ABC):
    def __init__(self, input_str, save_directory):
        self.input_str = input_str
        self.save_directory = save_directory
    
    @abc.abstractclassmethod
    def load_image(self):
        pass

    @abc.abstractclassmethod
    def resize(self, width, height):
        pass
    
    @abc.abstractclassmethod
    def save(self, file_path):
        pass