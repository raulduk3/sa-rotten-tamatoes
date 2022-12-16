# Sentiment Analysis of Rotten Tomato Reviews

Richard Álvarez

Kenyon IPHS 200.02 Programming Humanity (https://programminghumanity.wordpress.com/) 

<p align="center">
    <img width="66%" style='padding:5%;' src="https://github.com/morty-c137-prime/sa-rotten-tamatoes/blob/e91eae58afdbd45a73a481bcca25cad079d91e71/R%C3%81%20iphs200_programming_humanity_final_poster_standard.pptx%20(2).jpg?raw=true">
</p>

<p align="center">
    <img width="30%" style='padding:5%;' src="https://github.com/morty-c137-prime/sa-rotten-tamatoes/blob/eb20c4f218ef07d235c4791f79ce16a680e6792b/image2.jpg?raw=true">
    <img width="200" height="200" src="https://raw.githubusercontent.com/morty-c137-prime/sa-rotten-tamatoes/98e053ba0009783f0d50225cc5900725f20b0eb6/image1.jpg?raw=true">
    <img width="30%" style='padding:5%;' src="https://github.com/morty-c137-prime/sa-rotten-tamatoes/blob/eb20c4f218ef07d235c4791f79ce16a680e6792b/image3.jpg?raw=true">
</p>

### Abstract

In this project, the sentiment of user reviews on the movie review website Rotten Tomatoes was analyzed. The goal was to gain insight into the psychology of movie consumers and to evaluate the reliability of user reviews on Rotten Tomatoes.

Rotten Tomatoes provide a short comment/review and an indicator of the film’s ‘freshness’ (either fresh or rotten). The sentiment of the reviews was analyzed by employing a qualitative approach; the reviews were filtered for common stop words and tokenized for sentiment analysis using the VADER tool and the NLTK library.

This project found that approximately 73% of the reviews were consistent across sentiment analysis and ‘freshness’, which suggests both that VADER is a strong tool for sentiment analysis and that people on Rotten Tomatoes are mostly reliable.

### Introduction

Sentiment analysis has gained significant traction in the realm of film review evaluation in recent years due to its capability to enable the automatic analysis of large amounts of review data. This can provide valuable insights for film studios, critics, and moviegoers. However, the reliability and accuracy of sentiment analysis tools and methods remain a topic of ongoing research.

Movie reviews are a critical aspect of the film-viewing experience, offering insight into the quality of a film and aiding individuals in their decision-making process. Rotten Tomatoes is a popular platform that aggregates movie reviews from various sources and assigns an overall rating for each film. This project investigates the sentiment of user reviews on Rotten Tomatoes to gain a deeper understanding of the psychology of movie consumers.

By comparing sentiment scores computed using VADER to the user-provided 'freshness' score, this project offers insight into the reliability of the user to provide consistent messaging across their reviews. Ensuring more consistent reviews are filtered to users would be beneficial for Rotten Tomatoes in their pursuit of providing authentic and useful film reviews for moviegoers.

Overall, this project aims to contribute to the expanding body of research on sentiment analysis in the realm of film reviews and to offer valuable insights for film studios, critics, and moviegoers.

### Methodology

The dataset of reviews provided by Rotten Tomatoes was downloaded as a .csv file and then loaded into Python using the Pandas library as a DataFrame. The dataset contains an equal number of 'fresh' and 'rotten' reviews. These reviews were then processed by removing common stop words and performing sentiment analysis using tokenization. The mean of the compound sentiment scores for each sentence of the user's text response was compared to the user-provided 'freshness' score to determine whether the sentiment of the review aligned with the 'freshness' score. Neutral reviews were considered to be consistent with both 'fresh' and 'rotten' reviews because a neutral score from VADER indicates that the review does not have a positive or negative bias. 

A violin plot was also generated to visualize the distribution of sentiment scores for each 'freshness' category.

Code for this project available on GitHub
https://github.com/morty-c137-prime/sa-rotten-tamatoes

### Results

Overall, approximately 73% of the reviews were consistent across sentiment analysis and ‘freshness’, which suggests both that VADER is a strong tool for sentiment analysis and that people on Rotten Tomatoes are mostly reliable. This project provides insight into the sentiment of user reviews on Rotten Tomatoes and suggests that the website could potentially improve the reliability of its reviews by filtering for more consistent reviews. However, it should be noted that this project only analyzed a single dataset from a specific time period, and further research would be necessary to fully understand the sentiment of user reviews on Rotten Tomatoes.

To visualize the distribution of sentiment scores for each 'freshness' category, a violin plot was created. This plot showed that the sentiment scores for 'fresh' reviews were generally more positive than the sentiment scores for 'rotten' reviews. However, there was some overlap between the two categories, indicating that there were some 'fresh' reviews with negative sentiment scores and some 'rotten' reviews with positive sentiment scores.

These results suggest that the sentiment of user reviews on Rotten Tomatoes is generally in agreement with the user's 'freshness' score, but there are also some inconsistencies. This provides insight into the psychology of movie consumers and suggests that the website could potentially improve the reliability of its reviews by filtering for more consistent reviews.

### Conclusion

Overall, approximately 73% of the reviews were consistent across sentiment analysis and ‘freshness’, which suggests both that VADER is a strong tool for sentiment analysis and that people on Rotten Tomatoes are mostly reliable. This study provides insight into the sentiment of user reviews on Rotten Tomatoes and suggests that the website could potentially improve the reliability of its reviews by filtering for more consistent reviews. However, it should be noted that this study only analyzed a single dataset from a specific time period, and further research would be necessary to fully understand the sentiment of user reviews on Rotten Tomatoes.

To visualize the distribution of sentiment scores for each 'freshness' category, a violin plot was created. This plot showed that the sentiment scores for both 'fresh' and ‘rotten’ reviews were generally positive. It also showed that ’rotten’ reviews are less aligned sentimentally than ‘fresh’ reviews. However, this does not account for the fact that reviews might use positive while still expressing the film is worth giving a ‘rotten’ rating. Moreover, there was some overlap between the two categories, indicating that there were some 'fresh' reviews with negative sentiment scores and some 'rotten' reviews with positive sentiment scores.

These results suggest that the sentiment of user reviews on Rotten Tomatoes is generally in agreement with the user's 'freshness' score, but there are also some inconsistencies. This provides insight into the psychology of movie consumers and suggests that the website could potentially improve the reliability of its reviews by filtering for more consistent reviews.

### Future and Ethics Statement

This project has implications for the movie industry, as it can be used to better understand the sentiment of movie reviews and how it relates to the user’s opinion of the movie. This project has implications for the movie industry, as it can be used to better understand the sentiment of movie reviews and how it relates to the user’s opinion of the movie. Furthermore, this project has implications for the ethical use of sentiment analysis, as it can be used to detect potential bias in reviews and ensure that reviews are authentic and accurate.

### Reference/Acknowledgements 

Hutto, C.J. & Gilbert, E.E. (2014). VADER: A Parsimonious Rule-based Model for Sentiment Analysis of Social Media Text. Eighth International Conference on Weblogs and Social Media (ICWSM-14). Ann Arbor, MI, June 2014.

Chun, Jon. "SentimentArcs: A Novel Method for Self-Supervised Sentiment Analysis of Time Series Shows SOTA Transformers Can Struggle Finding Narrative Arcs." arXiv preprint arXiv:2110.09454 (2021).