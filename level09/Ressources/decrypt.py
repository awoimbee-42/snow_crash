#!/bin/env python3

import sys

if len(sys.argv) != 2:
	print("usage: decrypt.py <token_file>")
	sys.exit()

with open(sys.argv[1], 'rb') as tf:
	encrypted = tf.read()
	decrypted = [];
	for i, c in enumerate(encrypted):
		if i == 25:
			print(f"For some reason, char {c} at pos {i} is broken")
			continue
		decrypted.append(chr(c - i))
	print(''.join(decrypted))
