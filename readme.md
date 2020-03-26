# PrettyMath

Print formulas the pretty way inside your terminal.

### Dependencies
- python
- python-sympy

### Usage
- `-h` prints help
- `-u` and `--use_unicode` change output to unicode
- `...` all following strings are treated as expressions

### Examples
```bash
$ ./prettymath.py "a*b+x"
a*b + x
```
```bash
$ ./prettymath.py "a*b+x" "Integral(x**2,x)"
	a*b + x
  /
 |
 |  2
 | x  dx
 |
/
```
```bash
./prettymath.py "Limit(1/x, x, 0)"
	 1
 lim -
x->0+x
```
```bash
./prettymath.py -u "Limit(1/x, x, 0)"
	 1
 lim ─
x─→0⁺x
```
```bash
./prettymath.py "Sum(k**-2, (k, 1, n))"
  n
____
\   `
 \    1
  \   --
  /    2
 /    k
/___,
k = 1
```
```bash
./prettymath.py -u "Sum(k**-2, (k, 1, n))"
  n
 ____
 ╲
  ╲   1
   ╲  ──
   ╱   2
  ╱   k
 ╱
 ‾‾‾‾
k = 1
```
