# level08

```bash
~$ ln -s ~/token /tmp/file
~$ ./level08 /tmp/file
quif5eloekouj29ke0vouxean
```

## Explanation

Opening the `./level08` executable in ghidra shows:

```C
pcVar1 = strstr(argv[1],"token");
if (pcVar1 != (char *)0x0) {
    printf("You may not access \'%s\'\n",argv[1]);
    exit(1);
}
```
