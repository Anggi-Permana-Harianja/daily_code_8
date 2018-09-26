def bar(n):
	result = set([ ])

	#base case
	if n == 0:
		return set([""])
	if n == 1:
		result = set("")

	#recursive case
	for i in range(n):
		left_size = i
		right_size = n - i - 1

		left_result = bar(left_size)
		right_result = bar(right_size)

		for left in left_result:
			for right in right_result:
				current_result = '(' + left + ')' + right
				result.add(current_result)

	return result


print(bar(1)) #--> {'()'}
print(bar(2)) #--> {'(())', '()()'}
print(bar(3)) #--> {'((()))', '()(())', '(()())', '()()()', '(())()'}