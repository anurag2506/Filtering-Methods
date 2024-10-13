import random
import pandas as pd

#Creating list of users and their respective movies:
users=["user_"+ str(i) for i in range(1,50)] #Taking the data of 50 users
movies=["movie_"+str(i) for i in range(1,50)] #Taking the data of those 50 customer movie reviews

#Instead of dummy movie names and users, we can input real users and also movies to be in the lists

data=[]
for user in users:
    for movie in random.sample(movies, 10): #Each user rates 10 random movies
        rating = random.randint(1, 5)
        data.append([user, movie, rating])

df=pd.DataFrame(data, columns=['CustomerID', 'MovieID', 'Rating'])

df.to_csv('dataset1.csv', index=False)