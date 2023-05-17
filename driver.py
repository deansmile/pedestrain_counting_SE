import subprocess
import shutil
import os

from data_loader import data_loader
yml_inputs = data_loader.yaml_load("data.yml")

class_id = yml_inputs['class_id']
image_size = yml_inputs['image_size']
input_dir = yml_inputs['input_dir']
output_dir = yml_inputs['output_dir']
yolo_dir = yml_inputs['yolo_dir']
yolo_ver = yml_inputs['yolo_ver']

# change the path format of input values
input_dir = input_dir.replace('\\','/')
output_dir = output_dir.replace('\\','/')
yolo_dir = yolo_dir.replace('\\','/')


#command = "python yolov7/detect.py --weights C:\\Users\\acer\\Desktop\\2023\\yolov7-main\\yolov7.pt --conf 0.25 --img-size 640 --source C:\\Users\\acer\\Desktop\\2023\\yolov7-main\\inference\\images\\image1.jpg --class 0 --save-txt"
#cmd_str = r"{}".format(command)
# part_one = "python src/yolov7/detect.py --weights " + yolo_dir
# part_two = " --conf 0.25 --img-size " + str(image_size)
# part_three = " --source " + input_dir
# part_four =  " --class " + str(class_id) + " --save-txt"
command_line = f"python src/yolo{yolo_ver}/detect.py \
    --weights {yolo_dir} \
    --conf 0.25 \
    --img-size {image_size} \
    --source {input_dir} \
    --project {output_dir} \
    --class {class_id} \
    --save-txt"
subprocess.run(command_line, shell=True)
# root_src_dir = r'runs\detect' 
# root_dst_dir = output_dir

# # The for loop below is used to move the files in the source folder to a destined folder
# for src_dir, dirs, files in os.walk(root_src_dir):
#     dst_dir = src_dir.replace(root_src_dir, root_dst_dir, 1)
#     if not os.path.exists(dst_dir):
#         os.makedirs(dst_dir)
#     for file_ in files:
#         src_file = os.path.join(src_dir, file_)
#         dst_file = os.path.join(dst_dir, file_)
#         if os.path.exists(dst_file):
#             # in case of the src and dst are the same file
#             if os.path.samefile(src_file, dst_file):
#                 continue
#             os.remove(dst_file)
#         shutil.move(src_file, dst_dir)