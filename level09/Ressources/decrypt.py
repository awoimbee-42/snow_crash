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
			continue # For some reason, the last char (at pos 25) is broken
		decrypted.append(chr(c - i))
	print(''.join(decrypted))
