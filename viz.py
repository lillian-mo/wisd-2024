import data
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline, splprep, splev
import json

game_ids = [
        "687e2c12-dff4-4580-9226-c111366746e5",
        "af219680-da54-4e43-8ea5-3ea020f3bc2d",
        "a44f0611-618d-41dd-bb9b-089140c3f317",
        "f2f58c66-ea90-42cb-8d64-2ab98fe5c64a",
        "57d6343f-cdae-4517-acb4-ea73b838e2e9",
        "5fbf979d-ac7a-4f41-9498-2f94507ecba1",
        "bee9aa56-bfdd-4871-ace1-178db56aa19a"
    ]

be_handle = ['event','time','head']
be_head = ['event','time','handle']
be = ['time', 'vel', 'acc']
avg_headx_df = pd.DataFrame(columns=['x1', 'x2', 'x3', 'x4','x5', 'x6'])
avg_heady_df = pd.DataFrame(columns=['y1', 'y2', 'y3', 'y4','y5', 'y6'])
avg_handlex_df = pd.DataFrame(columns=['x1', 'x2', 'x3', 'x4','x5', 'x6'])
avg_handley_df = pd.DataFrame(columns=['y1', 'y2', 'y3', 'y4','y5', 'y6'])

def get_game(id):
    bhead_df = data.load_game(id, 'samples_bat')
    bhead_df = bhead_df.drop(columns=be_head)
    head_df = pd.json_normalize(bhead_df['head'].to_list())

    bhandle_df = data.load_game(id, 'samples_bat')
    bhandle_df = bhandle_df.drop(columns=be_handle)
    handle_df = pd.json_normalize(bhandle_df['handle'].to_list())
    return head_df, handle_df

def get_coords(df, colx, coly, head):
    split_df = pd.DataFrame(df['pos'].tolist(),index=df.index)
    split_df.columns = ['x','y','z']
    split_df = split_df.drop_duplicates()
    split_df = split_df.iloc[:368]
    if (head):
        avg_headx_df[colx] = split_df['x'].values
        avg_heady_df[coly] = split_df['y'].values
    else:
        avg_handlex_df[colx] = split_df['x'].values
        avg_handley_df[coly] = split_df['y'].values

# plot points
head_df, handle_df = get_game(game_ids[0])
head_df2, handle_df2 = get_game(game_ids[1])
head_df3, handle_df3 = get_game(game_ids[2])
head_df4, handle_df4 = get_game(game_ids[3])
head_df5, handle_df5 = get_game(game_ids[4])
head_df6, handle_df6 = get_game(game_ids[5])
head_df7, handle_df7 = get_game(game_ids[6])

get_coords(head_df, 'x1', 'y1', True)
get_coords(head_df2, 'x2', 'y2', True)
get_coords(head_df3, 'x3', 'y3', True)
get_coords(head_df4, 'x4', 'y4', True)
get_coords(head_df5, 'x5', 'y5', True)
get_coords(head_df6, 'x6', 'y6', True)
get_coords(head_df7, 'x7', 'y7', True)

get_coords(handle_df, 'x1', 'y1', False)
get_coords(handle_df2, 'x2', 'y2', False)
get_coords(handle_df3, 'x3', 'y3', False)
get_coords(handle_df4, 'x4', 'y4', False)
get_coords(handle_df5, 'x5', 'y5', False)
get_coords(handle_df6, 'x6', 'y6', False)
get_coords(handle_df7, 'x7', 'y7', False)

x_avg = avg_headx_df.mean(axis=1)
y_avg = avg_heady_df.mean(axis=1)

head_x = x_avg.tolist()
head_y = y_avg.tolist()

x_avg2 = avg_handlex_df.mean(axis=1)
y_avg2 = avg_handley_df.mean(axis=1)

handle_x = x_avg2.tolist()
handle_y = y_avg2.tolist()

tck, u = splprep([head_x,head_y], s=0)
new_x, new_y = splev(np.linspace(0, 1, 1000), tck)

tck2, u2 = splprep([handle_x,handle_y], s=0)
new_x2, new_y2 = splev(np.linspace(0, 1, 1000), tck2)

# base
coord = [[0, 0], [-0.708335, 0.708333], [-0.708335, 1.41667], [0.708335, 1.41667], [0.708335, 0.708333], [0, 0]]
xs, ys = zip(*coord) # split coords into x and y
plt.figure()
plt.plot(xs,ys, color='black') 

plt.plot(new_x, new_y, alpha=0.75, color='blue')
plt.plot(new_x2, new_y2, alpha=0.75, color='orange')

plt.legend(["home plate", "bat head", "bat handle"], loc="lower right")

plt.title("Bat trajectory")
plt.xlabel("x")
plt.ylabel("y")
plt.show()
