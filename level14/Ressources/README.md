# level14

This level is different, `/home/level14` is basically empty, running `find` yields no interresting results, etc.

So lets break into getflag :D.

First, let's use `ghidra` to get an idea of what the program does...

```C
/* Protection against GDB */
lVar2 = ptrace(PTRACE_TRACEME,0,1,0);
if (lVar2 < 0) {
    puts("You should not reverse this");
    uVar3 = 1;
}
/* (...) */
/* The condition that would give us the flag 14 ! */
else {
    if (_Var5 != 0xbc6) goto LAB_08048e06;
    __s = (char *)ft_des("g <t61:|4_|!@IF.-62FH&G~DCK/Ekrvvdwz?v|");
    fputs(__s,__stream);
}
```

```bash
gdb /bin/getflag
# First, hack into the condition that checks is the  program is running in GDB
(gdb) b *0x0804898e
(gdb) run
(gdb) set $eax=0
# Then, hack the condition that checks the current user ID
(gdb) b *0x08048b0a
(gdb) continue
(gdb) set $eax=3014
(gdb) continue
# -> Check flag.Here is your token : 7QiHafiNa3HVozsaXkawuYrTstxbpABHD8CPnHJ
```
