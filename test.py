import os
import numpy as np
import json

base_directory = "./anonymized-files-wisd"
file_list = os.listdir(base_directory)
data = []


for i in range(len(file_list)):
    curr_file = open(base_directory+"/"+file_list[i])
    data.append(json.load(curr_file))

array = np.array(data)


print(array[0])





