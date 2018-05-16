import testing

test_sentence = "i liked the movie.it was very good!anyone else wish it lasted longer?I sure did,but it's fine."

import data_handler

print(test_sentence)
new_test_sentence = []
data_handler.remove_characters(final_list_of_words = new_test_sentence, path = None, text = test_sentence)
print(new_test_sentence)
