import random
from string import (
	punctuation,
	ascii_lowercase,
	ascii_uppercase,
	digits
)

MIN_LENGTH = 6
MAX_LENGTH = 20

def randpass(
	amount: 'int' = 1,
	length: 'int | tuple[int, ...]' = 6,
	useAlphas: 'bool | tuple[bool, ...]' = True,
	useDigits: 'bool | tuple[bool, ...]' = True,
	useSpecials: 'bool | tuple[bool, ...]' = True
) -> 'list[str]':
	passwords = []
	# type assertions
	assert isinstance(amount, int), "amount should be an integer"
	assert isinstance(length, (int, tuple)), "length should be an integer or a tuple of integers"
	assert isinstance(useAlphas, (bool, tuple)), "useAlphas should be a boolean or a tuple of booleans"
	assert isinstance(useDigits, (bool, tuple)), "useDigits should be a boolean or a tuple of booleans"
	assert isinstance(useSpecials, (bool, tuple)), "useSpecials should be a boolean or a tuple of booleans"
	# check constraints
	if isinstance(length, tuple):
		if any(map(lambda l: l > MAX_LENGTH, length)):
			raise ValueError(f"length contains a value that is greater than {MAX_LENGTH}")
		elif any(map(lambda l: l < MIN_LENGTH, length)):
			raise ValueError(f"length contains a value that is less than {MAX_LENGTH}")
	else:
		if length > MAX_LENGTH:
			raise ValueError(f"length greater than {MAX_LENGTH}")
		elif length < MIN_LENGTH:
			raise ValueError(f"length less than {MIN_LENGTH}")
	if amount < 1:
		raise ValueError("amount less than 1")
	# more type assertions
	if amount > 1:
		if isinstance(useAlphas, tuple) and len(length) != amount:
			raise ValueError(f"length should contain {amount} numbers")
		if isinstance(useAlphas, tuple) and len(useAlphas) != amount:
			raise ValueError(f"useAlphas should contain {amount} booleans")
		if isinstance(useDigits, tuple) and len(useDigits) != amount:
			raise ValueError(f"useDigits should contain {amount} booleans")
		if isinstance(useSpecials, tuple) and len(useSpecials) != amount:
			raise ValueError(f"useSpecials should contain {amount} booleans")
	else:
		if isinstance(length, tuple):
			raise ValueError("length should be an integer")
		if isinstance(useAlphas, tuple):
			raise ValueError("useAlphas should be a boolean")
		if isinstance(useDigits, tuple):
			raise ValueError("useDigits should be a boolean")
		if isinstance(useSpecials, tuple):
			raise ValueError("useSpecials should be a boolean")
	for p in range(amount):
		password = ""
		choices = ""
		length_of_password: int
		use_alphas: bool
		use_digits: bool
		use_specials: bool
		if isinstance(length, tuple):
			length_of_password = length[p]
		else:
			length_of_password = length
		if isinstance(useAlphas, tuple):
			use_alphas = useAlphas[p]
		else:
			use_alphas = useAlphas
		if isinstance(useDigits, tuple):
			use_digits = useDigits[p]
		else:
			use_digits = useDigits
		if isinstance(useSpecials, tuple):
			use_specials = useSpecials[p]
		else:
			use_specials = useSpecials
		if not any((use_alphas, use_digits, use_specials)):
			raise RuntimeError(f"password-{p + 1} must use alphas, digits or specials")
		if (isinstance(useAlphas, tuple) and useAlphas[p] is True) or useAlphas is True:
			password += random.choice(ascii_lowercase)
			password += random.choice(ascii_uppercase)
			choices += ascii_lowercase + ascii_uppercase
		if (isinstance(useDigits, tuple) and useDigits[p] is True) or useDigits is True:
			password += random.choice(digits)
			choices += digits
		if (isinstance(useSpecials, tuple) and useSpecials[p] is True) or useSpecials is True:
			password += random.choice(punctuation)
			choices += punctuation
		for x in range(length_of_password):
			choice = random.choice(choices)
			password += choice
			if len(password) == length_of_password:
				break
		passwords.append(password)
	return passwords