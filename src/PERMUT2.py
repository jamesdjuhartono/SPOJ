while True:
	size = int(raw_input())
	if size == 0:
		break

	nums = map(int, raw_input().split())
	ambiguous = True
	for index, val in enumerate(nums):
		if index+1 != nums[val-1]:
			ambiguous = False
			break
	print ambiguous and "ambiguous" or "not ambiguous"