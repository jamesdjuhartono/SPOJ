while True:
	col = int(raw_input())

	if col == 0:
		break
	else:
		ciphertext = raw_input()
		row = len(ciphertext) / col
		plaintext = ""
		for j in range(col):
			i = j
			while i < len(ciphertext):
				plaintext += ciphertext[i]
				if i != j and i+j+1 < len(ciphertext):
					plaintext += ciphertext[i+2*j+1]
					i += 2*j+1
				i += 2*(col-j)-1
		print plaintext[:len(ciphertext)]