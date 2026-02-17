# **TITLE: "Tweet Sentiment Classification with Multinomial Naive Bayes”**


## **Problem and dataset**
This project performs tweet‑level sentiment classification, predicting whether a tweet is negative, neutral, or positive from its text.

​
The dataset is the “Tweet Sentiment Extraction” dataset, which contains about 27k tweets with sentiment labels and spans, from which I use the tweet text and overall sentiment label for classification.

Dataset:https://www.kaggle.com/datasets/yasserh/twitter-tweets-sentiment-dataset

## **Approach**
1.Load and explore the tweets (shape, sample rows, sentiment distribution).


2.Clean and normalize text (lowercasing, removing punctuation, basic token cleanup, stemming/lemmatization if used).

3.Split data into train/validation/test sets with stratification on sentiment.

4.Convert text to TF‑IDF features (unigrams and bigrams, limited vocabulary size, English stopwords removed).

5.Train a Multinomial Naive Bayes classifier as the baseline model.

6.Perform hyperparameter tuning using GridSearchCV over TF‑IDF and Naive Bayes parameters (e.g., n‑gram range, max_features, alpha).

7.Evaluate on validation and test sets using accuracy, precision, recall, macro F1, and confusion matrix.

## **Key Results**
Accuracy:0.67

Macro F1‑score:0.621
