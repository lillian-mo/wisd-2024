import os
import numpy as np
import json
import pandas as pd
from pandas import DataFrame

base_directory = "./anonymized-files-wisd"
file_list = os.listdir(base_directory)
data = []
frames = []
categories = []
positions = []

def load_game(games:str, type:str) -> DataFrame:
	for i in range(len(file_list)):
		curr_file = open(base_directory+"/"+file_list[i])
		data.append(json.load(curr_file))

	df = pd.json_normalize(data) # main dataframe

	## list of unnecessary columns
	categories = df.columns.values.tolist()
	categories.remove(type)
	categories.remove('events')

	df = df.drop(columns=categories) # drop columns

	## list of eventIds
	he_df = pd.json_normalize(df['events'].explode().to_list()) # hit events dataframe

	events_categories = he_df.columns.values.tolist() # list of unnecessary columns
	events_categories.remove('eventId') 
	he_df = he_df.drop(columns=events_categories) # drop columns
	hit_events = he_df['eventId'].tolist()

	if hit_events.index(games):
		positions.append(hit_events.index(games))
	
	return pd.DataFrame(df[type].iloc[positions[0]])
	

def mult_games(games:list, type:str) -> DataFrame:
	for i in range(len(file_list)):
		curr_file = open(base_directory+"/"+file_list[i])
		data.append(json.load(curr_file))

	df = pd.json_normalize(data) # main dataframe

	## list of unnecessary columns
	categories = df.columns.values.tolist()
	categories.remove(type)
	categories.remove('events')

	df = df.drop(columns=categories) # drop columns

	## list of eventIds
	he_df = pd.json_normalize(df['events'].explode().to_list()) # hit events dataframe

	events_categories = he_df.columns.values.tolist() # list of unnecessary columns
	events_categories.remove('eventId') 
	he_df = he_df.drop(columns=events_categories) # drop columns
	hit_events = he_df['eventId'].tolist()

	for i in range(len(hit_events)):
		if hit_events[i] in games:
			positions.append(i)

	# test = pd.DataFrame(df[type].iloc[positions[0]])
	# test.to_csv('wtf.csv')
 
	for i in range(len(positions)):
		temp_df = pd.DataFrame(df[type].iloc[positions[i]])
		frames.append(temp_df)

	merged_df = pd.concat(frames)
	return merged_df
