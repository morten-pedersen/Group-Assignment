"""
This file is responsible for running and timing the different types of tests, as well as measuring accuracy.
"""
import time

import classifier


def test_classify_test_dataset():
	"""
	This will attempt to classify the test dataset
	"""
	start_time = time.time()
	classifier.train()
	number_of_reviews = classifier.negative_review_count + classifier.positive_review_count
	results = classifier.predict_reviews()
	print(results)
	print(str(results["correct_predictions"] / number_of_reviews * 100) + "% is the accuracy ")
	final_time = time.time() - start_time
	print("It took: "f'{final_time:.2f}'" seconds to run\n")


def test_classify_test_dataset_with_stopwords():
	"""
	This test will attempt to classify the test dataset while using stopwords
	"""
	start_time = time.time()
	use_stop_words = True
	classifier.train()
	number_of_reviews = classifier.negative_review_count + classifier.positive_review_count
	results = classifier.predict_reviews(use_stop_words = use_stop_words)
	print(results)
	print(str(results["correct_predictions"] / number_of_reviews * 100) + "% is the accuracy ")
	final_time = time.time() - start_time
	print("It took: "f'{final_time:.2f}'" seconds to run\n")


def test_classify_train_dataset():
	"""
	This will attempt to classify the training dataset
	"""
	start_time = time.time()
	classifier.train()
	number_of_reviews = classifier.negative_review_count + classifier.positive_review_count
	results = classifier.predict_reviews(classify_training_data = True)
	print(results)
	print(str(results["correct_predictions"] / number_of_reviews * 100) + "% is the accuracy ")
	final_time = time.time() - start_time
	print("It took: "f'{final_time:.2f}'" seconds to run\n")


def test_classify_train_dataset_with_stopwords():
	"""
	This will attempt to classify the training dataset with stop-words
	"""
	start_time = time.time()
	classifier.train()
	number_of_reviews = classifier.negative_review_count + classifier.positive_review_count
	results = classifier.predict_reviews(use_stop_words = True, classify_training_data = True)
	print(results)
	print(str(results["correct_predictions"] / number_of_reviews * 100) + "% is the accuracy ")
	final_time = time.time() - start_time
	print("It took: "f'{final_time:.2f}'" seconds to run\n")


def test_classify_train_dataset_with_testing_data():
	"""
	This will attempt to classify the training dataset, using the testing dataset to train
	"""
	start_time = time.time()
	classifier.train(use_testing_data = True)
	number_of_reviews = classifier.negative_review_count + classifier.positive_review_count
	results = classifier.predict_reviews(use_stop_words = False, classify_training_data = True)
	print(results)
	print(str(results["correct_predictions"] / number_of_reviews * 100) + "% is the accuracy ")
	final_time = time.time() - start_time
	print("It took: "f'{final_time:.2f}'" seconds to run\n")


def test_classify_train_dataset_with_testing_data_with_stopwords():
	"""
	This will attempt to classify the training dataset, using the testing dataset to train - with stop-words
	"""
	start_time = time.time()
	classifier.train(use_testing_data = True)
	number_of_reviews = classifier.negative_review_count + classifier.positive_review_count
	results = classifier.predict_reviews(use_stop_words = True, classify_training_data = True)
	print(results)
	print(str(results["correct_predictions"] / number_of_reviews * 100) + "% is the accuracy ")
	final_time = time.time() - start_time
	print("It took: "f'{final_time:.2f}'" seconds to run\n")


def test_classify_test_dataset_with_testing_data():
	"""
	This will attempt to classify the testing dataset, using the testing dataset to train
	"""
	start_time = time.time()
	classifier.train(use_testing_data = True)
	number_of_reviews = classifier.negative_review_count + classifier.positive_review_count
	results = classifier.predict_reviews(use_stop_words = False, classify_training_data = False)
	print(results)
	print(str(results["correct_predictions"] / number_of_reviews * 100) + "% is the accuracy ")
	final_time = time.time() - start_time
	print("It took: "f'{final_time:.2f}'" seconds to run\n")


def test_classify_test_dataset_with_testing_data_using_stopwords():
	"""
	This will attempt to classify the testing dataset, using the testing dataset to train - using stop-words
	"""
	start_time = time.time()
	classifier.train(use_testing_data = True)
	number_of_reviews = classifier.negative_review_count + classifier.positive_review_count
	results = classifier.predict_reviews(use_stop_words = True, classify_training_data = False)
	print(results)
	print(str(results["correct_predictions"] / number_of_reviews * 100) + "% is the accuracy ")
	final_time = time.time() - start_time
	print("It took: "f'{final_time:.2f}'" seconds to run\n")
