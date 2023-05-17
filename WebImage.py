import cv2
from Image import Image
import urllib.request
import numpy as np

class WebImage(Image):
    def __init__(self):
        super().__init__()    
    
    def load_image(self):
        response = urllib.request.urlopen(self.input_str)
        image_data = response.read()
        self.image = cv2.imdecode(np.frombuffer(image_data, np.uint8), cv2.IMREAD_COLOR)

    def resize(self, width, height):
        self.image=cv2.resize(self.image, (width, height))
    
    def save(self,file_path):
        cv2.imwrite(file_path, self.image)

