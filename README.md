# sa-rotten-tamatoes
Sentiment Analysis of Rotten Tomato Reviews

<p align="center">
    <img width="66%" style='padding:5%;' src="https://github.com/morty-c137-prime/sa-rotten-tamatoes/blob/e91eae58afdbd45a73a481bcca25cad079d91e71/R%C3%81%20iphs200_programming_humanity_final_poster_standard.pptx%20(2).jpg?raw=true">
</p>

<p align="center">
    <img width="30%" style='padding:5%;' src="https://github.com/morty-c137-prime/sa-rotten-tamatoes/blob/eb20c4f218ef07d235c4791f79ce16a680e6792b/image2.jpg?raw=true">
    <img width="200" height="200" src="https://raw.githubusercontent.com/morty-c137-prime/sa-rotten-tamatoes/98e053ba0009783f0d50225cc5900725f20b0eb6/image1.jpg?raw=true">
    <img width="30%" style='padding:5%;' src="https://github.com/morty-c137-prime/sa-rotten-tamatoes/blob/eb20c4f218ef07d235c4791f79ce16a680e6792b/image3.jpg?raw=true">
</p>

Abstract

In this project, the sentiment of user reviews on the movie review website Rotten Tomatoes was analyzed. The goal was to gain insight into the psychology of movie consumers and to evaluate the reliability of user reviews on Rotten Tomatoes. Rotten Tomatoes provide a short comment/review and an indicator of the film’s ‘freshness’ (either fresh or rotten). The sentiment of the reviews was analyzed by employing a qualitative approach; the reviews were filtered for common stop words and tokenized for sentiment analysis using the VADER tool and the NLTK library.

Introduction

The use of sentiment analysis in the field of movie reviews has gained popularity in recent years, as it allows for the automatic evaluation of large amounts of review data. This can provide valuable insights for movie studios, film critics, and moviegoers alike. However, the accuracy and reliability of sentiment analysis tools and techniques is still an active area of research.

Movie reviews are an important part of the movie-going experience. Reviews can provide insight into the quality of a movie and can help people decide which movies to watch. Rotten Tomatoes is a popular website that aggregates movie reviews from various sources and provides an overall rating for each movie. This study examines the sentiment of user reviews on Rotten Tomatoes in order to gain insight into the psychology of movie consumers.

By comparing sentiment scores calculated using VADER to the user’s provided ‘freshness’ score, insight is provided regarding the user’s reliability to provide consistent messaging across their reviews. If Rotten Tomato aims to provide authentic and useful film reviews for moviegoers, it would be in their interest to make sure more consistent reviews are filtered to their users.

Overall, this study aims to contribute to the growing body of research on sentiment analysis in the field of movie reviews and to provide valuable insights for movie studios, film critics, and moviegoers.

Methodology

The dataset of reviews provided by Rotten Tomatoes was downloaded as a .csv file and then loaded into Python using the Pandas library as a DataFrame. The dataset contains an equal number of 'fresh' and 'rotten' reviews. These reviews were then processed by removing common stop words and performing sentiment analysis using tokenization. The mean of the compound sentiment scores for each sentence of the user's text response was compared to the user-provided 'freshness' score to determine whether the sentiment of the review aligned with the 'freshness' score. Neutral reviews were considered to be consistent with both 'fresh' and 'rotten' reviews because a neutral score from VADER indicates that the review does not have a positive or negative bias.

A violin plot was also generated to visualize the distribution of sentiment scores for each 'freshness' category.

Results

Overall, approximately 73% of the reviews were consistent across sentiment analysis and ‘freshness’, which suggests both that VADER is a strong tool for sentiment analysis and that people on Rotten Tomatoes are mostly reliable. This study provides insight into the sentiment of user reviews on Rotten Tomatoes and suggests that the website could potentially improve the reliability of its reviews by filtering for more consistent reviews. However, it should be noted that this study only analyzed a single dataset from a specific time period, and further research would be necessary to fully understand the sentiment of user reviews on Rotten Tomatoes.

To visualize the distribution of sentiment scores for each 'freshness' category, a violin plot was created. This plot showed that the sentiment scores for both 'fresh' and ‘rotten’ reviews were generally positive. It also showed that ’rotten’ reviews are less aligned sentimentally than ‘fresh’ reviews. However, this does not account for the fact that reviews might use positive while still expressing the film is worth giving a ‘rotten’ rating. Moreover, there was some overlap between the two categories, indicating that there were some 'fresh' reviews with negative sentiment scores and some 'rotten' reviews with positive sentiment scores.

These results suggest that the sentiment of user reviews on Rotten Tomatoes is generally in agreement with the user's 'freshness' score, but there are also some inconsistencies. This provides insight into the psychology of movie consumers and suggests that the website could potentially improve the reliability of its reviews by filtering for more consistent reviews.

Conclusion

In conclusion, this study examined the sentiment of user reviews on the movie review website Rotten Tomatoes using the VADER tool and the NLTK library. The results showed that 66.15% of the reviews had sentiment scores that agreed with the user's provided 'freshness' score. A violin plot was also created to visualize the distribution of sentiment scores for each 'freshness' category.

The results suggest that the sentiment of user reviews on Rotten Tomatoes is generally in agreement with the user's 'freshness' score. This provides insight into the psychology of movie consumers and suggests that the website could potentially improve the reliability of its reviews by filtering for more consistent reviews.

It is important to recognize that sentiment analysis is not a perfect science and that there may be biases and limitations in the VADER tool and the NLTK library that could affect the results of this study. Therefore, it is important to interpret the results of this study with caution and to consider the potential limitations of the methodology.

As a future direction, it would be interesting to analyze the sentiment of reviews over time to see if there are any trends or changes in the sentiment of reviews on Rotten Tomatoes. Additionally, it would be valuable to compare the results of this study to other movie review websites to see if the sentiment of reviews is similar or different across platforms.


Future and Ethics Statement

This project has implications for the movie industry, as it can be used to better understand the sentiment of movie reviews and how it relates to the user’s opinion of the movie. Furthermore, this project has implications for the ethical use of sentiment analysis, as it can be used to detect potential bias in reviews and ensure that reviews are authentic and accurate.

Reference/Acknowledgements 

Hutto, C.J. & Gilbert, E.E. (2014). VADER: A Parsimonious Rule-based Model for Sentiment Analysis of Social Media Text. Eighth International Conference on Weblogs and Social Media (ICWSM-14). Ann Arbor, MI, June 2014.

Chun, Jon. "SentimentArcs: A Novel Method for Self-Supervised Sentiment Analysis of Time Series Shows SOTA Transformers Can Struggle Finding Narrative Arcs." arXiv preprint arXiv:2110.09454 (2021).