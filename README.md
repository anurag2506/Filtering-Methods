: Recommendation datasets are collections of data used to develop Recommendation systems like Movie/music/books/social-media content. These are based on personalized choices. These datasets have specific features:

1.	User data(age, preferences, demographics etc.)
For eg. A content creator can address people in the age-group of 18-22, is focused on sports and can live in the US.
2.	Items: (what is that, he provides):
For eg. He provides info, highlights of everyday Basketball games
3.	Interactions: (How he interacts with his fan-base):
For eg. Youtube, Twitch,Instagram,Twitter
4.	Frequency: (How often his interactions ae with his fan-base):
For eg. How often does his provide updates to his fan-base

And there might be several other factors

Some of the Recommendation datasets that I found include:
https://huggingface.co/datasets/sileod/movie_recommendation

 

Explanation of the Dataset:
The question column contains a list of 4 movies. The next 4 columns contain the number of people opting for each movie among the list of the movies available. The label column gives the index of the question (0,1,2,3) telling the movie with highest watch count. 
Collaborative Filtering:

Intuition:
This is a method used in user-item recommendation systems which are based on the idea “Users with similar interests will have common preferences”. 
Basically, “Similar past preferences can provide insights about future predictions”. 

To compute the similarity in preferences we have multiple methods:
1.	Cosine Similarity
2.	Pearson Correlation coefficient
3.	Euclidean Distance
4.	Jaccard Distance
5.	Manhattan Distance
6.	Spearman Rank Correlation
7.	Hamming Distance
8.	Tanimoto Coefficient

Cosine Similarity is what that is primarily used for the following reasons:
1.	Scale Invariance
2.	Simplicity and Efficiency

 <img width="452" alt="image" src="https://github.com/user-attachments/assets/dab3063f-4461-4537-aed9-73e91942ee01">

(source: Me)

How Cosine Similarity is Calculated:
  <img width="452" alt="image" src="https://github.com/user-attachments/assets/15d1546a-0684-40c1-bdc8-09c2d11ef6a9">


This is an example matrix of the ratings of 8 different shows by 3 different users and we will predict the ratings of unrated shows of user1 based on the rankings of user2 and user3. 
 
<img width="452" alt="image" src="https://github.com/user-attachments/assets/edaaec29-7ab3-4291-b982-3517b0ccafe7">

Example:
Let’s denote the similarity of user1 with user2 as u12 and u13 for the other pair. Let’s suppose we have the rating for a particular movie by both user1 and user2. To find the rating of that movie by user3 we take the weighted mean of both the users where the weights are the cosine similarities.  

Barriers in Collab Filtering
•	Cold Start problem: For initial users and items, there isn’t initial data to make predictions based on. This creates a problem of suggestions to new users and/or new items
•	Sparsity: Most of today’s users don’t rank items. They make use of them and do not give reviews which creates a very sparse item-user interaction matrix
•	Gray-Sheep problem: Several users have very unpredictable preferences and do not align with any particular group of users. They cannot be clustered with any group leading to poor recommendations for them

CONTENT-BASED FILTERING:
Content-based filtering solves a lot of these problems faced as it is not user-specific. It focusses on the item data. Works on the data that is taken from items (either explicitly i.e. rating) or (implicitly i.e. clicks). 

This method depends more on the item’s features and not on the user preferences or behaviors of other people. 

 
<img width="452" alt="image" src="https://github.com/user-attachments/assets/80180042-6311-4fc9-9c49-e86cbc14638c">



Content-based filtering solves the Cold-start problem since it doesn’t need the user’s interactions to create the recommendation matrix
It also solves the problem of niche-interest since it doesn’t focus on any item in a niche and rather focusses on the properties of the item of that niche which can be matched with properties of items in other niches as well



References:
1.	https://youtu.be/Fmtorg_dmM0?si=csfbJJKGPqCgfvZi
2.	https://www.geeksforgeeks.org/collaborative-filtering-ml/
3.	https://developers.google.com/machine-learning/recommendation/collaborative/basics
4.	https://www.kaggle.com/code/ibtesama/getting-started-with-a-movie-recommendation-system : very informative
5.	https://www.geeksforgeeks.org/ml-content-based-recommender-system/
6.	https://www.kaggle.com/code/omeroruccelik/content-based-recommendation-systems : very informative



Research Paper Recommendation Model:

The ¬¬¬¬¬model gives a list of recommendations when provided with a particular Research Paper Title. These recommendations are based on different factors like:
1.	Number of Citations
2.	The conference of the paper
3.	Year of publishing
4.	Authors
5.	References 
6.	Similarities in the Abstract of papers

The dataset is not labelled and therefore it is an unsupervised Machine Learning model.  And all the content-based recommendation models are examples of Unsupervised ML models

The model takes in an input of any Research Paper of the user’s choice and provides relevant recommendation for that paper in a JSON format to the user. 

For each recommended paper, you will get:
•	Title: Title of the recommended paper.
•	Authors: List of authors for the recommended paper.
•	Year: The year the recommended paper was published.
•	n_citations: Number of citations the recommended paper has.
![image](https://github.com/user-attachments/assets/6e9de3dc-efb1-486d-a6c6-132df32900fd)
