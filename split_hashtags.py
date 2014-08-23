
import nltk
from nltk.corpus import words, brown

word_dictionary = list(set(words.words()))

for alphabet in "bcdefghjklmnopqrstuvwxyz":
	word_dictionary.remove(alphabet)

def split_hashtag_to_words_all_possibilities(hashtag):
	all_possibilities = []
	
	split_posibility = [hashtag[:i] in word_dictionary for i in reversed(range(len(hashtag)+1))]
	possible_split_positions = [i for i, x in enumerate(split_posibility) if x == True]
	
	for split_pos in possible_split_positions:
		split_words = []
		word_1, word_2 = hashtag[:len(hashtag)-split_pos], hashtag[len(hashtag)-split_pos:]
		
		if word_2 in word_dictionary:
			split_words.append(word_1)
			split_words.append(word_2)
			all_possibilities.append(split_words)

			another_round = split_hashtag_to_words_all_possibilities(word_2)
				
			if len(another_round) > 0:
				all_possibilities = all_possibilities + [[a1] + a2 for a1, a2, in zip([word_1]*len(another_round), another_round)]
		else:
			another_round = split_hashtag_to_words_all_possibilities(word_2)
			
			if len(another_round) > 0:
				all_possibilities = all_possibilities + [[a1] + a2 for a1, a2, in zip([word_1]*len(another_round), another_round)]
	
	return all_possibilities