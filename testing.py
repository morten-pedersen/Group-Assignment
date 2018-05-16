import time
import classifier


def test_predict_test_dataset():
	"""
	This will attempt to classify the test dataset
	:return:
	"""
	start_time = time.time()
	classifier.train()
	number_of_reviews = classifier.negative_review_count + classifier.positive_review_count
	results = classifier.predict_reviews()
	print(results)
	print(str(results["correct_predictions"] / number_of_reviews * (100)) + "% is the accuracy ")
	final_time = time.time() - start_time
	print("It took: "f'{final_time:.2f}'" seconds to run\n")


def test_predict_test_dataset_with_stopwords():
	"""
	This test will attempt to classify the test dataset while using stopwords
	"""
	start_time = time.time()
	use_stop_words = True
	classifier.train()
	number_of_reviews = classifier.negative_review_count + classifier.positive_review_count
	results = classifier.predict_reviews(use_stop_words = use_stop_words)
	print(results)
	print(str(results["correct_predictions"] / number_of_reviews * (100)) + "% is the accuracy ")
	final_time = time.time() - start_time
	print("It took: "f'{final_time:.2f}'" seconds to run\n")


def test_predict_train_dataset():
	"""
	This will attempt to classify the test dataset
	:return:
	"""
	start_time = time.time()
	classifier.train()
	number_of_reviews = classifier.negative_review_count + classifier.positive_review_count
	results = classifier.predict_reviews(predict_training_data = True)
	print(results)
	print(str(results["correct_predictions"] / number_of_reviews * (100)) + "% is the accuracy ")
	final_time = time.time() - start_time
	print("It took: "f'{final_time:.2f}'" seconds to run\n")


def test_predict_train_dataset_with_stopwords():
	"""
	This will attempt to classify the test dataset
	:return:
	"""
	start_time = time.time()
	classifier.train()
	number_of_reviews = classifier.negative_review_count + classifier.positive_review_count
	results = classifier.predict_reviews(use_stop_words = True, predict_training_data = True)
	print(results)
	print(str(results["correct_predictions"] / number_of_reviews * (100)) + "% is the accuracy ")
	final_time = time.time() - start_time
	print("It took: "f'{final_time:.2f}'" seconds to run\n")

def test_predict_train_dataset_with_testing_data():
	start_time = time.time()
	classifier.train(use_testing_data = True)
	number_of_reviews = classifier.negative_review_count + classifier.positive_review_count
	results = classifier.predict_reviews(use_stop_words = False, predict_training_data = True)
	print(results)
	print(str(results["correct_predictions"] / number_of_reviews * (100)) + "% is the accuracy ")
	final_time = time.time() - start_time
	print("It took: "f'{final_time:.2f}'" seconds to run\n")

def test_predict_train_dataset_with_testing_data_with_stopwords():
	start_time = time.time()
	classifier.train(use_testing_data = True)
	number_of_reviews = classifier.negative_review_count + classifier.positive_review_count
	results = classifier.predict_reviews(use_stop_words = True, predict_training_data = True)
	print(results)
	print(str(results["correct_predictions"] / number_of_reviews * (100)) + "% is the accuracy ")
	final_time = time.time() - start_time
	print("It took: "f'{final_time:.2f}'" seconds to run\n")

def test_predict_test_dataset_with_testing_data():
	start_time = time.time()
	classifier.train(use_testing_data = True)
	number_of_reviews = classifier.negative_review_count + classifier.positive_review_count
	results = classifier.predict_reviews(use_stop_words = False, predict_training_data = False)
	print(results)
	print(str(results["correct_predictions"] / number_of_reviews * (100)) + "% is the accuracy ")
	final_time = time.time() - start_time
	print("It took: "f'{final_time:.2f}'" seconds to run\n")

def test_predict_test_dataset_with_testing_data_using_stopwords():
	start_time = time.time()
	classifier.train(use_testing_data = True)
	number_of_reviews = classifier.negative_review_count + classifier.positive_review_count
	results = classifier.predict_reviews(use_stop_words = True, predict_training_data = False)
	print(results)
	print(str(results["correct_predictions"] / number_of_reviews * (100)) + "% is the accuracy ")
	final_time = time.time() - start_time
	print("It took: "f'{final_time:.2f}'" seconds to run\n")