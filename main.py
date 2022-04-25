import random

import numpy as np
from spotifyapi import SpotifyAPI as sp
from matplotlib import pyplot as plt
from turtle import *
from time import *
import colorsys

note_dict = {
    0: "C",
    1: "C#",
    2: "D", 
    3: "D#",
    4: "E",
    5: "F",
    6: "F#",
    7: "G",
    8: "G#",
    9: "A",
    10: "A#",
    11: "B"
}
color_dict = {
    "C": "#28ff00",
    "C#": "#00ffe8",
    "D": "#007cff",
    "D#": "#0500ff",
    "E": "#4500ea",
    "F": "#57009e",
    "F#": "#740000",
    "G": "#b30000",
    "G#": "#ee0000",
    "A": "#ff6300",
    "A#": "#ffec00",
    "B": "#99ff00"
}
new_color_dict = {
    "C": "#FF0000",
    "C#": "#7f00ff",
    "D": "#FFFF00",
    "D#": "#ffe9d1",
    "E": "#87ceeb",
    "F": "#850101",
    "F#": "#0096FF",
    "G": "#FFA500",
    "G#": "#C8A2C8",
    "A": "#32CD32",
    "A#": "#F33A6A",
    "B": "#79b4c9"
}

# convert hex code to rgb
for x in new_color_dict.items():
    h = x[1].lstrip('#')
    new_color_dict[x[0]] = tuple(int(h[i:i+2], 16) for i in (0, 2, 4))

# get track IDs for the input songs and artists
track_id = sp.get_track_id('Ni**as in Paris', 'Jay-Z')
segments = sp.get_audio_features(track_id)["segments"]

duration = []   # duration of each section

rand_color = [] # random color for each 5 second interval

loudness_start = [] # color for each section

fade_colors = [] # color for each section

for x in segments:
    duration.append(x['duration'])


# append a random color to rand_color for every 5 seconds till the end of the song
for x in range(0, int(sum(duration))):
    if x % 5 == 0:
        rand_color.append(random.choice(list(new_color_dict.values())))

# decrease intensity of color dependent on the loudness_max of the section
duration_passed = 0
color = None
for i,section in enumerate(segments):
    # count = 0
    # duration_passed += section['duration']
    # if duration_passed > 5:
    #     duration_passed = 0
    #     count += 1
    #     color = rand_color[count]
    # color = random.choice(list(new_color_dict.values()))
    color = rand_color[12]
    color = colorsys.rgb_to_hsv(color[0], color[1], color[2])
    color = list(color)
    color[-1] = color[-1]*(section['loudness_max']*-1/80)
    fade_colors.append(colorsys.hsv_to_rgb(color[0], color[1], color[2]))

plt.scatter(range(len(segments)), [x[-1] for x in fade_colors])
plt.show()

# ## change color of turtle screen
# screen = Screen()
# screen.colormode(255)
# # change color of screen with dominant colors as time step of the song
# for x in range(len(fade_colors)):
#     fade_color = fade_colors[x]
#     screen.bgcolor(int(fade_color[0]), int(fade_color[1]), int(fade_color[2]))
#     sleep(duration[x])