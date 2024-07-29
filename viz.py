import data
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline, splprep, splev
import json

game_ids = [
        # "687e2c12-dff4-4580-9226-c111366746e5",
        "af219680-da54-4e43-8ea5-3ea020f3bc2d"
        # "a44f0611-618d-41dd-bb9b-089140c3f317",
        # "f2f58c66-ea90-42cb-8d64-2ab98fe5c64a",
        # "57d6343f-cdae-4517-acb4-ea73b838e2e9",
        # "5fbf979d-ac7a-4f41-9498-2f94507ecba1",
        # "bee9aa56-bfdd-4871-ace1-178db56aa19a"
    ]

be_handle = ['event','time','head']
be_head = ['event','time','handle']

# ball_df = data.mult_games(game_ids, 'samples_ball')
bat_df = data.mult_games(game_ids, 'samples_bat')
bat_df = bat_df.drop(columns=be_head)

# data = {'pos': [-3.8662697464311457, -0.5036555447348817, 5.502688510955257]}
# def extract_pos(entry):
#     dict_entry = ast.literal_eval(entry)
#     return dict_entry['pos']
# new_df = pd.DataFrame.from_dict(data,orient='index')


# bitch = "{'pos': [-3.8662697464311457, -0.5036555447348817, 5.502688510955257]}"

bat_df.to_csv('wtf.csv')

# bat_df.to_csv('wtf.csv')
# print(bat_df)

# def get_coords(df, type):
#     if (type == 'handle'):
#         df = df.drop(columns=be_handle)
#     elif (type == 'head'):
#         df = df.drop(columns=be_head)
#     elif (type == 'pos'):
#         categories = df.columns.values.tolist()
#         categories.pop(1)
#         df = df.drop(columns=categories)

#     split_df = pd.DataFrame(df[type].tolist(),index=df.index)
#     print(split_df)
#     return 0
    # split_df.columns = ['x','y','z']
    # split_df = split_df.drop_duplicates()

    # x, y, z = (split_df[coord].to_numpy() for coord in split_df.columns)
    # tck, u = splprep([x,y], s=0)
    # new_x, new_y = splev(np.linspace(0, 1, 1000), tck)
    
    # return new_x, new_y

# base
# coord = [[6, 50], [8, 50], [8, 40], [7, 30], [6, 40], [6, 50]]
# xs, ys = zip(*coord) # split coords into x and y
# plt.figure()

# plot points
# plt.scatter(x,y, s=0.5, color='red')
# plt.plot(x, y, color='red', alpha=0.5)

# ball_x, ball_y = get_coords(ball_df)
# get_coords(bat_df, 'head')
# plt.plot(bat_x, bat_y, alpha=0.75)
# plt.plot(bat_x, bat_y, alpha=0.75, color='orange')


# plt.title("Ball trajectory")
# plt.xlabel("X")
# plt.ylabel("Y")
# plt.show()



'''
# sample data points
x = np.array([1, 2, 3, 4, 5, 6, 7, 8])
y = np.array([20, 30, 5, 12, 39, 48, 50, 3])
z = np.array([0, 10, 8, 2, 5, 6, 7, 9])

y2 = np.array([10, 2, 8, 4, 4, 20, 32, 9])
 
smooth_line = make_interp_spline(x, y)
smooth_line2 = make_interp_spline(x, y2)
 
# Returns evenly spaced numbers
# over a specified interval.
x_coords = np.linspace(x.min(), x.max(), 500)
y_coords = smooth_line(x_coords)
y2_coords = smooth_line2(x_coords)


# 2D graph

# base
coord = [[6, 50], [8, 50], [8, 40], [7, 30], [6, 40], [6, 50]]
xs, ys = zip(*coord) # split coords into x and y
plt.figure()
plt.plot(xs,ys) 

# plot points
plt.plot(x_coords, y_coords)
plt.plot(x_coords, y2_coords)

plt.title("Bat trajectory")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()


# # Creating an empty canvas(figure)
# fig = plt.figure()
 
# # Creating an empty 3D axes of the plot
# ax = fig.add_subplot(projection='3d')
 
# # label axes
# ax.set_xlabel('x')
# ax.set_ylabel('y')
# ax.set_zlabel('z')
 
# # zdir='z' fixes all the points to zs=0 and
# # (x,y) points are plotted in the x-y axis
# # of the graph
# ax.plot(x_coords, y_coords, zs=0, zdir='z')
# ax.plot(x_coords, y2_coords, zs=0, zdir='z')
 
# plt.show()
'''