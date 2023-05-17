import numpy as np
import cv2
import matplotlib.pyplot as plt
import os 
from scipy.ndimage import gaussian_filter

# The following 4 things should be passed FROM the second GUI
txt_directory = "C:/Users/acer/Desktop/Test/exp2/labels/image1.txt"
image_directory = "C:/Users/acer/Desktop/sandbox-rgbi/yolov7/inference/images/image1.jpg"
output_directory = "C:/Users/acer/Desktop/Test"
output_image_name = "output_image2"



def denormalize_box(x, y, w, h, image_width, image_height):
    x_new = float(x)
    y_new = float(y)
    w_new = float(w)
    h_new = float(h)
    # Denormalize the coordinates
    denorm_x = int(x_new * image_width)
    denorm_y = int(y_new * image_height)
    denorm_w = int(w_new * image_width)
    denorm_h = int(h_new * image_height)

    # Calculate the top-left corner coordinates
    x1 = int(denorm_x - (denorm_w / 2))
    y1 = int(denorm_y - (denorm_h / 2))

    # Calculate the bottom-right corner coordinates
    x2 = int(denorm_x + (denorm_w / 2))
    y2 = int(denorm_y + (denorm_h / 2))

    return x1, y1, x2, y2

def GT_Generate(txt_directory, image_directory, output_directory, output_image_name):
    txt_path = txt_directory
    with open(txt_path, "r") as f:
        annotations = f.readlines()

    img=cv2.imread(image_directory,0)
    img=img.astype(np.float32, copy=False)
    ht=img.shape[0]
    wd=img.shape[1]
    Coordinates=[]
    Main_Zeros=np.zeros((ht,wd),dtype=np.float32)

    # Create then canvas
    height, width = ht, wd
    image = np.ones((height, width, 3), dtype=np.uint8) * 255

    for ann in annotations:
        ann_parts = ann.strip().split(" ")
        if len(ann_parts) != 5:
            print(f"Invalid annotation format in {txt_path}: {ann}")
        else:
            a, x, y, w, h = ann_parts
            x1, y1, x2, y2 = denormalize_box(x, y, w, h, wd, ht)
            cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
            Coordinates.append([x1,y1,x2-x1,y2-y1,1/((x2-x1)*(y2-y1))])

    for bbox_left, bbox_top, bbox_w, bbox_h, bbox_weight in Coordinates:
        for i in range(int(bbox_left),int(bbox_left+bbox_w)):
            for j in range(int(bbox_top),int(bbox_top+bbox_h)):
                Main_Zeros[j, i] += bbox_weight
    den = gaussian_filter(Main_Zeros,sigma=6,truncate=6*6)

    normalized_array = (den - den.min()) * (255 / (den.max() - den.min()))

    plt.imshow(normalized_array, cmap='gray', vmin=0, vmax=255)
    plt.axis('off')
    # save the image in certain output path
    # A Ground Truth Image will be generated!!!!!!!
    plt.savefig(output_directory + "/" + output_image_name + ".jpg", format = 'jpg', bbox_inches='tight',pad_inches=0)
    # plt.show()
