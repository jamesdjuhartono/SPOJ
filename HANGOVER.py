val = float(raw_input())
while val != 0.00:
	curr = 0.0
	count = 2
	cards = 0

	while curr <= val:
		curr += (1.0/count)
		count += 1
		cards += 1

	print "%d card(s)" % cards
	val = float(raw_input())