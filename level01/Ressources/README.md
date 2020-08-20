# level01

```bash
cat /etc/passwd | grep flag01
# flag01:42hDRfypTqqnw:3001:3001::/home/flag/flag01:/bin/bash

# 42hDRfypTqqnw is the password, encrypted
# let's use john the ripper to decode it:
echo '42hDRfypTqqnw' > pass
john pass --show
# -> abcdefg
```
