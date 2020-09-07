# level13

Decompilation shows:

```C
  _Var1 = getuid();
  if (_Var1 != 0x1092) {
    _Var1 = getuid();
    printf("UID %d started us but we we expect %d\n",_Var1,0x1092);
                    /* WARNING: Subroutine does not return */
    exit(1);
  }
  uVar2 = ft_des("boe]!ai0FB@.:|L6l@A?>qJ}I");
  printf("your token is %s\n",uVar2);
```

So the answer is:

```bash
gdb ./level13
(gdb) disas main
(gdb) b *0x0804859a
(gdb) run
(gdb) set $eax=0x1092
(gdb) continue
# your token is 2A31L79asukciNyi8uppkEuSx
```
