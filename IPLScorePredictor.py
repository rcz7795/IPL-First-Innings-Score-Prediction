import pickle
import json
import numpy as np
from os import path

teams_values = None
venue_values = None
over_values = None
wickets_values = None
model = None

def load_saved_attributes():

    global teams_values
    global venue_values
    global over_values
    global wickets_values
    global model

    with open("columns.json", "r") as f:
        resp = json.load(f)
        teams_values = resp["teams_columns"]
        venue_values = resp["venue"]
        over_values = resp["overs"]
        wickets_values = resp["wickets"]

    model = pickle.load(open("cricket_score_predictor.pickle", "rb"))

def get_team_names():
    return teams_values

def get_venue_values():
    return venue_values

def get_over_values():
    return over_values

def get_wickets_values():
    return wickets_values

def predict_cricket_price(team1, team2, venue, over, wickets, score, runs_in_last4, wickets_in_last4):
    try:
        team1_index = teams_values.index(team1)
        team2_index = teams_values.index(team2)
        venue_index = venue_values.index(venue)
    except:
        team1_index = -1
        team2_index = -1
        venue_index = -1

    team1_array = np.zeros(len(teams_values))
    if team1_index >= 0:
        team1_array[team1_index] = 1

    team2_array = np.zeros(len(teams_values))
    if team2_index >= 0:
        team2_array[team2_index] = 1

    venue_array = np.zeros(len(venue_values))
    if venue_index >= 0:
        venue_array[venue_index] = 1

    team1_array = team1_array[:-1]
    team2_array = team2_array[:-1]
    venue_array = venue_array[:-1]
    sample = np.concatenate((venue_array, team1_array, team2_array, np.array([over, wickets, score, runs_in_last4, wickets_in_last4])))

    return model.predict(sample.reshape(1,-1))[0]


if __name__ == '__main__':
    load_saved_attributes()
else:
    load_saved_attributes()
