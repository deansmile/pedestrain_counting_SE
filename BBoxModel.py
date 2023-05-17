from Model import Model
from enums import COCOLabels, weights
import subprocess
import os
import ntpath
from GT_Generate import GT_Generate

def find_files_with_extension(root_dir, extension):
    file_paths = []
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith(extension):
                file_path = os.path.join(root, file)
                file_paths.append(file_path)
    return file_paths

def get_substring_before_second_backslash(string):
    first_backslash_index = string.find("\\")
    second_backslash_index = string.find("\\", first_backslash_index + 1)
    if second_backslash_index != -1:
        substring = string[:second_backslash_index]
    else:
        substring = string
    return substring

class BBoxModel(Model):
    def __init__(self, yolo_ver, classes, weight, input_dir, output_dir):
        super().__init__()
        self.ver=str(yolo_ver)
        self.classes=classes
        self.weight=weight
        self.input_dir=input_dir
        self.output_dir=output_dir

    def predict(self):
        class_id=""
        for c in self.classes:
            class_id+=(str(COCOLabels[c].value)+" ")
        command_line = f"python yolov{self.ver}/detect.py \
            --weights {weights[self.weight].value} \
            --conf 0.25 \
            --source {self.input_dir} \
            --project {self.output_dir} \
            --class {class_id} \
            --save-txt"
        output_file=open("predict_log.txt","w")
        subprocess.run(command_line, shell=True, stdout=output_file, text=True)
        output_file.close()
    
    def gf_ground_truth(self):
        f=open("predict_log.txt")
        for line in f:
            if "The image with the result is saved in" in line:
                res_path=get_substring_before_second_backslash(line[40:])
                break
        res_paths=find_files_with_extension(res_path, ".txt")
        img_paths=find_files_with_extension(self.input_dir, ".jpg")
        os.makedirs("GT", exist_ok=True)
        for ip in img_paths:
            fn=os.path.splitext(ntpath.basename(ip))[0]
            for rp in res_paths:
                if fn in rp:
                    print(rp,ip,fn)
                    GT_Generate(rp, ip, "GT", fn)
                    break
        


# model=BBoxModel(7,["PERSON"], "V7E6E", "images", "out")
# model.gf_ground_truth()