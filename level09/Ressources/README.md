# level09

```bash
level09@SnowCrash:~$ ls -l
total 12
-rwsr-sr-x 1 flag09 level09 7640 Mar  5  2016 level09
----r--r-- 1 flag09 level09   26 Mar  5  2016 token

level09@SnowCrash:~$ cat -e token
f4kmm6p|=M-^B^?pM-^BnM-^CM-^BDBM-^CDu{^?M-^LM-^I$

level09@SnowCrash:~$ ./level09 aaaaaaaaaaaa
abcdefghijkl
```

We have an encoder and an encoded token, let's try to reverse engineer the encoder and try that on the token !

The encoding is easy, it increments every char by its position in the string.
 _________________________________________
 | a(+0) | a(+1) | a(+2) | a(+3) | a(+4) |
 |---------------------------------------|
 |   a       b       c       d       e   |
 |_______________________________________|

Use `decrypt.py` on `token` -> `f3iji1ju5yuevaus41q1afiuq`
