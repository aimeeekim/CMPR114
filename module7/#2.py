def get_login_name(first, last, idnumber):
	# Get the first three leters of the first name.
	# If the name is less than 3 characters, the 
	# slice will return the entire first name
	set1 = first[0 : 3]

	# Get the first three leters of the last name.
	# If the name is less than 3 characters, the 
	# slice will return the entire last name
	set2 = last[0 : 3]

	# Get the last three leters of the student ID.
	# If the ID number is less than 3 characters, the 
	# slice will return the entire ID number.
	set3 = idnumber[-3 :]

	# put the sets of chacters toegether
	login_name = set1 + set2 + set3

	# Return the login name
	return login__name

# The valid_password function accepts a password as
# an argument and returns either true or false to
# indicate whether the password is valid. 
# A valid password must be at least 7 characters in length
# have at least one uppercase letter, one lowercase 
# letter, and one digit

def valid_password(password):
	# Set the Boolean variables toe false.
	correct_length = False
	has_uppercase = False
	has_lowercase = False
	has_digit = False

	# Begin the validation. Start by testing the password's length
	if len(password) >= 7:
		correct_length = True

		# Test each character and set the 
		# appropriate flag when a required 
		# character is found.
		for ch in password:
			if ch.isupper():
				has_uppercase = True
			if ch.islower():
				has_lowercase = True
			if ch.isdigit():
				has_digit = True
		
		# Determine whether all of the requirements
		# are met. IF they are, set is_valid to ture.
		# Otherwise, set is _valid to false.
		if correct_length and has_uppercase and has_lowercase and has_digit:
			is_valid = True
		else:
			is_valid = False
		# Return the is_valid variable.
		return is_valid
