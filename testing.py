import time
import classifier as predict


def test_predict_test_dataset():
	"""
	This will attempt to classify the test dataset
	:return:
	"""
	start_time = time.time()
	predict.train()
	number_of_reviews = predict.negative_review_count + predict.positive_review_count
	results = predict.predict_test_reviews()
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
	predict.train()
	number_of_reviews = predict.negative_review_count + predict.positive_review_count
	results = predict.predict_test_reviews(use_stop_words = use_stop_words)
	print(results)
	print(str(results["correct_predictions"] / number_of_reviews * (100)) + "% is the accuracy ")
	final_time = time.time() - start_time
	print("It took: "f'{final_time:.2f}'" seconds to run\n")
