"""
This program uses Luhn Algorithm (http://en.wikipedia.org/wiki/Luhn_algorithm) and works with most credit card numbers.


1. From the rightmost digit, which is the check digit, moving left, double the value of every second digit.

2. If the result is greater than 9 (e.g., 7 * 2 = 14), then sum the digits of it (e.g., 10: 1 + 0 = 1, 14: 1 + 4 = 5).
This procedure can be alternatively described as: num - 9

3. If the total modulo 10 is equal to 0 (if the total ends in zero) then the number is valid.
"""
if __name__ == '__main__':
	number = raw_input('Enter the credit card number of check: ')\
	          .replace(' ', '')

	digits = [int(ch) for ch in number]
	digits = digits[::-1]

	# double alternate digits (step 1)
	double = [(digit * 2) if (i % 2) else digit \
            for (i, digit) in enumerate(digits)]


	# subtract 9 which >= 10 (step 2)
	summ = [num if num < 10 else num - 9 \
          for num in double]

	# step 3
	if sum(summ) % 10 == 0:
		print 'The number is valid'
	else:
		print 'The number is invalid'
