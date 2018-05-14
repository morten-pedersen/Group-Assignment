from stop_words import get_stop_words


def make_word_frequency_dict(list_of_words, use_stop_words = False):
	"""
	Find the frequency of the words in the list given in the parameter, adding them to a dictionary as keys with their
	frequency as value
	:param use_stop_words: False by default, if True, words found to be a stopword will not be counted
	:param list_of_words: the list of files
	:return: a dictionary with words as keys and frequency as values
	"""
	dictionary = {}
	if use_stop_words:  # if true, using stopwords
		stop_words = get_stop_words('english')
		for word in list_of_words:  # add the words to a dictionary as keys and their frequency as value.
			if word in dictionary and word not in stop_words:
				dictionary[word] += 1
			elif word not in dictionary and word not in stop_words:
				dictionary[word] = 1
			else:
				pass
		return dictionary
	else:  # Not using stopwords
		for word in list_of_words:  # add the words to a dictionary as keys and their frequency as value.
			if word in dictionary:
				dictionary[word] += 1
			else:
				dictionary[word] = 1
		return dictionary


def old_potentially_useful_stuff():
	# pos_word_value_total = sum(pos_words_dict.values())
	# neg_word_value_total = sum(neg_words_dict.values())
	pass
