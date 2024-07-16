import os
import numpy as np
import json
import pandas as pd
import ast

base_directory = "./anonymized-files-wisd"
file_list = os.listdir(base_directory)
data = []
positions = []


for i in range(len(file_list)):
    curr_file = open(base_directory+"/"+file_list[i])
    data.append(json.load(curr_file))
    positions.append(data[i]['samples_ball'])

array = np.array(data)
example = np.array(positions[0])
df = pd.json_normalize(positions[0])
exampleArray = df.values



