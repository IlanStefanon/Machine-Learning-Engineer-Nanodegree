	# Get the features and labels from the Boston housing data
	X, y = city_data.data, city_data.target

	###################################
	### Step 3. YOUR CODE GOES HERE ###
	###################################
	X_train, X_test, y_train, y_test  = cross_validation.train_test_split( X, y, test_size=0.1, random_state=0)

	return X_train, y_train, X_test, y_test