HashTagSplitter
===============

A recursive python function to break down hashtags or compound words created by putting together multiple words

My implementation of the maximum matching algorithm to split compound words or hashtags to multiple words.


Example Usage:

split_hashtag_to_words_all_possibilities("edgeofentertainment")
[['edge', 'of', 'entertainment']]

split_hashtag_to_words_all_possibilities("playtowin")
[['play', 'tow', 'in'], ['play', 'to', 'win']]

split_hashtag_to_words_all_possibilities("datascience")
[['data', 'science'], ['da', 'ta', 'science']]

split_hashtag_to_words_all_possibilities("superbowl")
[['superb', 'owl'], ['super', 'bowl'], ['sup', 'er', 'bowl']]



As can be seen from the examples, the output is totally based on the quality/vocabulary of the dictionary that is used.


TODO:

Build an n-gram model based on a corpus from nltk to order the possibilities by probability of occurence/usage and display only the top 3/5 most probable possibilities
