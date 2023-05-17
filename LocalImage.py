import cv2
from Image import Image

class LocalImage(Image):
    def __init__(self):
        super().__init__()    
    
    def load_image(self):
        self.image=cv2.imread(self.input_str)

    def resize(self, width, height):
        self.image=cv2.resize(self.image, (width, height))
    
    def save(self,file_path):
        cv2.imwrite(file_path, self.image)