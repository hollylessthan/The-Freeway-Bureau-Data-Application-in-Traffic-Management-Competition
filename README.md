# The-Freeway-Bureau-Data-Application-in-Traffic-Management-Competition

In 2019 summer, I partnered with a classmate for The Freeway Bureau Data Application in Traffic Management Competition, in which we were tasked with improving freeway safety through analyzing billions of data in Taiwan car accident- related deaths, road violation data, and traffic data on the freeways from 2013 to 2018. 
I viewed car accidents as a matter of people, cars, and roads, and divided the project into two parts. 
My classmate observed the relationship between perpetrator road violation behavior and car accidents, using Apriori and K-means algorithms that I guided her through in Weka. 
I analyzed the association between environmental factors on roads and the probability of car accidents.


I first defined environmental factors as the number of vehicles and average speed an hour before accidents happened, aiming to determine whether these two factors would affect the occurrence of car accidents. 
As the data provided by the Freeway Bureau didn’t contain these two columns, I calculated them myself from the traffic data, extracting a dataset containing all Taiwanese electronic toll collection data in the past six years. 
Since it was my first time dealing with such a huge, real-world dataset and under time constraints, I decided to sample the data from January 2015 to April 2015, a time range with three major holidays for traveling on roads. 
Nonetheless, my laptop was unable to store and process 2TB of data, so I loaded the data in sequence and split it into smaller files for processing. 
As a result of organization issues such as different formats of numbers in a column or different record formats in different years, I checked the calculations each time to see if any error existed, and then revised the code again. 
After much time spent pre-processing, I found that the number of vehicles and average speeds were not directly correlated to the occurrence of car accidents, an extremely frustrating result.


Refusing to give up just yet, I shifted my attention to a broad set of environmental factors including lights, road type, accident locations, and accident times, and focused on environmental factors affecting the occurrence of car accidents caused by specific reasons. 
To make the results more meaningful, I searched for online sources to approximate the analytical process of other data scientists. 
I observed my data carefully and made adjustments, such as using Pandas package in Python to transform categorical data into numerical data. 
I then used six methods from Scikit-learn package in Python to cautiously conduct feature selections, including both the statistical methods, such as Chi-square and Pearson correlation, and machine learning methods, such as recursive feature elimination, Lasso, random forest, and light GBM. 
Afterward, I used Tableau to further examine the data of selected features and visualize the data distributions.


Eventually, I found some significant results that I then integrated with that of our team’s to give suggestions to the judges. We proposed that the Freeway Bureau provide different ways of implementation and training for different groups of drivers. 
Moreover, car accidents caused by specific reasons are strongly associated with specific environmental factors, so we clustered the data to present possible early-warning methods for future car accidents. 
Our findings were recognized by the director of the Freeway Bureau, and we won fourth place out of 59 teams.


This project taught me that checking data properties and defining a clear goal without assumptions are important before jumping into the data analysis process. 
By checking the data type, format, and order in every time series first, we can save lots of time in going back to revise the code. 
In addition, trying feature selection methods to select impactful features instead of defining them intuitively without a knowledge base is more likely to produce useful results. 
This research was also a good experience in identifying an appropriate method, analytical procedures, and other areas for improvement, so that I am more prepared to deal with real-world problems effectively and efficiently in the future.
