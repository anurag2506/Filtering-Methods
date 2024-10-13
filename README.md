<b>COLLABORATIVE FILTERING METHODS VS CONTENT-BASED FILTERING METHODS</B>

Recommendation datasets are collections of data used to develop Recommendation systems like Movie/music/books/social-media content. These are based on personalized choices. These datasets have specific features:

1.	User data(age, preferences, demographics etc.)
For eg. A content creator can address people in the age-group of 18-22, is focused on sports and can live in the US.
2.	Items: (what is that, he provides):
For eg. He provides info, highlights of everyday Basketball games
3.	Interactions: (How he interacts with his fan-base):
For eg. Youtube, Twitch,Instagram,Twitter
4.	Frequency: (How often his interactions ae with his fan-base):
For eg. How often does his provide updates to his fan-base

And there might be several other factors
<br>
Some of the Recommendation datasets that I found include:
https://huggingface.co/datasets/sileod/movie_recommendation
<img width="452" alt="image" src="https://github.com/user-attachments/assets/b05fe845-ff0e-4dae-b5f6-521a8774ad8c">

 

Explanation of the Dataset:
The question column contains a list of 4 movies. The next 4 columns contain the number of people opting for each movie among the list of the movies available. The label column gives the index of the question (0,1,2,3) telling the movie with highest watch count. 

<b>Collaborative Filtering:</b>
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
<br><br>
Cosine Similarity is what that is primarily used for the following reasons:
1.	Scale Invariance
2.	Simplicity and Efficiency

 <img width="452" alt="image" src="https://github.com/user-attachments/assets/dab3063f-4461-4537-aed9-73e91942ee01">
<br>
(source: Me)

How Cosine Similarity is Calculated:<br>
  <img width="452" alt="image" src="https://github.com/user-attachments/assets/15d1546a-0684-40c1-bdc8-09c2d11ef6a9">
<br>

This is an example matrix of the ratings of 8 different shows by 3 different users and we will predict the ratings of unrated shows of user1 based on the rankings of user2 and user3. 
 
<img width="452" alt="image" src="https://github.com/user-attachments/assets/edaaec29-7ab3-4291-b982-3517b0ccafe7">

Example:
Let’s denote the similarity of user1 with user2 as u12 and u13 for the other pair. Let’s suppose we have the rating for a particular movie by both user1 and user2. To find the rating of that movie by user3 we take the weighted mean of both the users where the weights are the cosine similarities.  
<br> <br>
Barriers in Collab Filtering<br>
•	Cold Start problem: For initial users and items, there isn’t initial data to make predictions based on. This creates a problem of suggestions to new users and/or new items
•	Sparsity: Most of today’s users don’t rank items. They make use of them and do not give reviews which creates a very sparse item-user interaction matrix
•	Gray-Sheep problem: Several users have very unpredictable preferences and do not align with any particular group of users. They cannot be clustered with any group leading to poor recommendations for them
<br><br>
<b>CONTENT-BASED FILTERING:</b><br><br>
Content-based filtering solves a lot of these problems faced as it is not user-specific. It focusses on the item data. Works on the data that is taken from items (either explicitly i.e. rating) or (implicitly i.e. clicks). 

This method depends more on the item’s features and not on the user preferences or behaviors of other people. 

 
<img width="452" alt="image" src="https://github.com/user-attachments/assets/80180042-6311-4fc9-9c49-e86cbc14638c">



Content-based filtering solves the Cold-start problem since it doesn’t need the user’s interactions to create the recommendation matrix
It also solves the problem of niche-interest since it doesn’t focus on any item in a niche and rather focusses on the properties of the item of that niche which can be matched with properties of items in other niches as well


<br><br>
References:
1.	https://youtu.be/Fmtorg_dmM0?si=csfbJJKGPqCgfvZi
2.	https://www.geeksforgeeks.org/collaborative-filtering-ml/
3.	https://developers.google.com/machine-learning/recommendation/collaborative/basics
4.	https://www.kaggle.com/code/ibtesama/getting-started-with-a-movie-recommendation-system : very informative
5.	https://www.geeksforgeeks.org/ml-content-based-recommender-system/
6.	https://www.kaggle.com/code/omeroruccelik/content-based-recommendation-systems : very informative

<br>

<b>Research Paper Recommendation Model:</b><br><br>

The model gives a list of recommendations when provided with a particular Research Paper Title. These recommendations are based on different factors like:
1.	Number of Citations
2.	The conference of the paper
3.	Year of publishing
4.	Authors
5.	References 
6.	Similarities in the Abstract of papers

The dataset is not labelled and therefore it is an unsupervised Machine Learning model.  And all the content-based recommendation models are examples of Unsupervised ML models

The model takes in an input of any Research Paper of the user’s choice and provides relevant recommendation for that paper in a JSON format to the user. 

For each recommended paper, you will get:
1.	Title: Title of the recommended paper.<br>
2. Authors: List of authors for the recommended paper.<br>
3. Year: The year the recommended paper was published.<br>
4. n_citations: Number of citations the recommended paper has.<br>
5. The Venue of the Conference where it was published
<br><br><br>
The Reference Papers that I found useful:
1. <a href="https://ijiet.com/wp-content/uploads/2016/12/20.pdf">Paper-1</a> <br>
2. <a href="https://jazindia.com/index.php/jaz/article/view/4158/3646">Paper-2</a>


