### Characters
* alphabets (lowercase and uppercase)
* numbers (0-9)
* special characters (punctuations e.g #$%*&`!)

### Constraints
* length >= 6
* length <= 20
* amount >= 1

### Types
* amount: integer (default: 1)
* length: integer, tuple of integers (default: 6)
* useAlphas: boolean, tuple of booleans (default: True)
* useDigits: boolean, tuple of booleans (default: True)
* useSpecials: boolean, tuple of booleans (default: True)
* return: list of strings

### Descriptions
* amount: number of passwords to generate
* length:
	+ as an integer: the length of the password[s]
	+ as a tuple: the length of each password e.g `(7, 8, 6, ...)`
* useAlphas:
	+ as a boolean: specify is the password[s] should contain alphabets
	+ as a tuple: specify is each password should contain alphabets e.g `(True, False, ...)`
* useDigits:
	+ as a boolean: specify is the password[s] should contain useDigits
	+ as a tuple: specify is each password should contain useDigits e.g `(True, False, ...)`
* useSpecials:
	+ as a boolean: specify is the password[s] should contain special characters
	+ as a tuple: specify is each password should contain special characters e.g `(True, False, ...)`

### Function
```py
function randpass(length, amount, useAlphas, useDigits, useSpecials)
	passwords = []
    # checks
    if length is greater than 20
    	Error
    if length is less than 6
    	Error
    if amount is less than 1
    	Error
    if amount > 1
		if length is a tuple and length of the tuple is not amount
			Error
    	if useAlphas is a tuple and length of the tuple is not amount
            Error
        if useDigits is a tuple and length of the tuple is not amount
            Error
        if useSpecials is a tuple and length of the tuple is not amount
        	Error
    else
		if length is a tuple
			Error
    	if useAlphas is a tuple
        	Error
        if useDigits is a tuple
        	Error
        if useSpecials is a tuple
        	Error
    for i in 0 to amount
        password = ""
        choices = ""
		if length is a tuple
			length_of_password = the value for this password in length
		else if length is an integer
			length_of_password = value of length
		if useAlphas is a tuple
			use_alphas = the value for this password in useAlphas
		else if useAlphas is a boolean
			use_alphas = the value of useAlphas
		if useDigits is a tuple
			use_digits = the value for this password in useDigits
		else if useDigits is a boolean
			use_digits = the value of useDigits
		if useSpecials is a tuple
			use_specials = the value for this password in useSpecials
		else if useSpecials is a boolean
			use_specials = the value of useSpecials

		if use_alphas is False and use_digits is False and use_specials is False:
			Error
        if use_alphas
        	add one lowercase alphabet to password
			add one uppercase alphabet to password
        	add all alphabets to choices
        if use_digits
			add one digit to password
        	add all digits to choices
        if use_specials
			add one special character to password
        	add all special characters to choices
        for i in 0 to length_of_password
        	choice = random choice in choices
            add choice to password
            if password length is equals to length_of_password
            	exit this loop
        # at this point it has generated a random password
        add password to passwords
    # at this point it has generated all random passwords
    return passwords
```