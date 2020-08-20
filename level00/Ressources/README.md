# level00

```bash
# Find the UID of user `flag00`
cat /etc/passwd | grep flag00
# Find all the files this user owns
find / -uid 3000 2>/dev/null
# Turns out it's only 1 file, let's see what's inside:
cat /rofs/usr/sbin/john
# -> cdiiddwpgswtgt
# Decode the string (Caesar encoding, +15)
# -> nottoohardhere
```

x24ti5gi3x0ol2eh4esiuxias
