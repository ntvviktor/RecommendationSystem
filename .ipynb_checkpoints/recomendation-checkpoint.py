import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.utils import shuffle
from datetime import datetime
# from sortedcontainers import SortedList

with open('user2movie.json', 'rb') as f:
  user2movie = pickle.load(f)

with open('movie2user.json', 'rb') as f:
  movie2user = pickle.load(f)

with open('usermovie2rating.json', 'rb') as f:
  usermovie2rating = pickle.load(f)

with open('usermovie2rating_test.json', 'rb') as f:
  usermovie2rating_test = pickle.load(f)
  
print(usermovie2rating_test)

number_of_users = np.max(list(user2movie.keys())) + 1
# the test set may contain movies the train set doesn't have data on
m1 = np.max(list(movie2user.keys()))
m2 = np.max([m for (u, m), r in usermovie2rating_test.items()])
number_of_movies = max(m1, m2) + 1
print("Number of users: ", number_of_users, "\nNumber of movies:", number_of_movies)

if number_of_users > 10000:
  print("N =", number_of_users, "are you sure you want to continue?")
  print("Comment out these lines if so...")
  exit()


# Implementation of 

for user, movies in user2movie.items():

    avg_r_i = 0
    for m in movies:
        avg_r_i += usermovie2rating[tuple(user, m)]
        
    