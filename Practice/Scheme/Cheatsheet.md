Forked from [egregius313/scheme-help.md](https://gist.github.com/egregius313/e20246fbdb67861a05edaf7dbd0315d6)

- [Scheme Built-Ins](#basic)
- [Common Predicates](#predicates)
- [Commands We Will Define](#user-defined)

# Basic Scheme Commands <a name="basic"/>

TODO: These are not yet implemented in the sheet but are mentioned in the index:
- apply
- equal?
- length
- max
- min
- reverse

## Index

- [and](#and)
- [append](#append)
- [apply](#apply)
- [begin](#begin)
- [case](#case)
- [car](#car)
- [cadr](#cadr)
- [cdr](#cdr)
- [cdar](#cdar)
- [caddr](#caddr)
- [cond](#cond)
- [cons](#cons)
- [define](#define)
- [display](#display)
- [equal?](#equal?)
- [if](#if)
- [lambda](#lambda)
- [length](#length)
- [let](#let)
- [list](#list)
- [map](#map)
- [max](#max)
- [min](#min)
- [modulo](#modulo)
- [not](#not)
- [or](#or)
- [quotient](#quotient)
- [reverse](#reverse)
- [Comparsion Functions (=, >, <, >=, <=)](#comparison)

## and
`and` takes a variable number of arguments and returns whether all of them are true.

```scheme
; True and True and True is True
> (and #t #t #t)
#t

; True and False is False
> (and (= 0 0) (> 7 100))
#f
```

**Note**: `and` expands into a series of `if` branches when the compiler reads the code.
It cannot be used as a function with functions like [map](#map), [filter](#filter) and [reduce](#reduce).

## append
Takes two or more lists and returns the result of concatenating those lists together.

```scheme
> (append '(1 2 3) '(4 5 6))
'(1 2 3 4 5 6)

> ; Append multiple lists together
> (append '(a b) '(c) '(d e f g) '(h i))
'(a b c d e f g h i)
```

## begin
`begin` is a macro that allows you to execute multiple expressions in sequence.

```scheme
  (if (> n 0)
      (begin
        (display-n x (- n 1))
        (display x)
        )
      )
```

## case

`case` is a [macro](#macro) which provides similar/identical functionality to switch/case in
C-style languages.

```scheme
> (define (message-for-grade grade)
     (case grade
        ('(A) "Excellent!")
        ('(B) "Not bad! Keep up the good work.")
        ('(C) "There's always a curve.")
        ('(D) "Did you study?")
        ('(F) "Maybe this just isn't your thing")))
> (message-for-grade 'B)
"Not bad! Keep up the good work."
```

## car

`car` returns the first element of a list.

```scheme
> (car (list 1 2 3))
1
```

## cadr

`cadr` returns the second element of a list.

```scheme
> (cadr (list 1 2 3))
2
```

## cdr

`cdr` returns the rest of the list after the first element.

```scheme
> (cdr (list 1 2 3))
'(2 3)
```

## cdar

`cdar` returns the rest of the list after the first element of the first element.

```scheme
> (cdar (list (list 1 2 3) (list 4 5 6)))
'(2 3)
```

## caddr

`caddr` returns the third element of a list.

```scheme
> (caddr (list 1 2 3))
3
```

## cond

`cond` is a nice [macro](#macro) that helps abstract away heavily nested `if` expressions. It's used like
how Python's `elif` keyword is used to avoid nested if statements.

It is somewhere in between [if](#if) and [case](#case) in terms of functionality.

```scheme
;; Compare two numbers `x` and `y`, returns:
;;    0  if they are equal
;;    1  if `x` is greater than `y`
;;   -1  if `x` is less than `y`
;;
> (define (compare x y)
    (cond
      ((> x y) 1)
      ((< x y) -1)
      (else 0)))

;; 5 > 3, so 1
> (compare 5 3)
1
```

## cons

```scheme
(cons element list)
```
Add an element to the beginning of a list.

```scheme
> (cons 1 '(2 3))
'(1 2 3)
```

## define

`define` is the way to set variables and to define functions.

```scheme
(define name value)

(define (fn-name args ...)
   ... function body ...)
```

`define` is the way to set variables and to define functions.

```scheme
; Define a variable "a" with the value 10
> (define a 10)
> a
10

; Define a function that returns twice the length of the list "numbers"
> (define (double-len numbers)
     (* 2 (length numbers)))

> (double-length '(a b c d))
8
```

`define`

## display

```scheme
(display string)
```
`display` is the equivalent of `print` in Python or `System.out.println` in
Java except it does not print the new line by default (you need to add `\n` to
the end of the string literal for the new line).

```scheme
;; The "\n" is for the newline
> (display "Hello, World!\n")
Hello, World!
```

## equal?

```scheme
(equal? x y)
```
`equal?` returns whether or not two values are equal or not. It is generally better to use
`equal?` than `=` because `=` can only check numeric values, and `equal?` uses more advanced
definitions of equality.

```scheme
> (equal? 2 2)
#t
> (equal? '(2 3) '(5 6))
#f

> (= '(1 2 3) '(1 2 3))
#f
> (equal? '(1 2 3) '(1 2 3))
#t
```

## if

```scheme
(if condition then else)
```
Equivalent of an if statement. If the condition is true, evaluates to the `then`
branch, otherwise evaluates to the `else` clause

```scheme
> (if (= 2 (/ 4 2))
    (display "They're equal\n")
    (display "They're not equal\n"))
They're equal

; You can nest if expressions
> (define (compare x y)
    (if (> x y)
      1
      (if (< x y)
        -1
        0)))

;; 10 > 2 ==> 1
> (compare 10 2)
1
```

## lambda

```scheme
(lambda (args ...) ... function body ...)
```
`lambda` creates in-line functions. It is especially useful when used with
functions like map, filter, and reduce

```scheme
> ; Here we pass a function that adds 2 to a number
> (define (add-2-to-each lst)
    (map (lambda (x) (+ x 2)) lst))

> (add-2-to-each '(1 20 13 401 5 108 71))
'(3 22 15 403 7 110 73)
```
## length

`length` returns the length of a list.

```scheme
> (length '(1 2 3 4 5))
5
```

## let

The `let` expression is used to create local variables. It is similar to `define` except that the variable is only accessible within the `let` expression.

```scheme
> (let ((x 10)
        (y 20))
    (+ x y))

30

;Here let is used to store the result of a (quotient 13 4) in a variable named result

> (let ((result (quotient 13 4)))
    (display result)
    (display "\n"))
```


## list

```scheme
(list v ...)
```
`list` takes multiple values and returns a linked list containing those

```scheme
> (list 1 'a 2.3 3 4.5e+3)
'(1 a 2.3 3 4.5e+3)
```

These are all functions that can be used to manipulate lists:
* [car](#car)
* [cadr](#cadr)
* [cdr](#cdr)
* [cdar](#cdar)
* [caddr](#caddr)
* [cons](#cons)

## map

```scheme
(map proc list)
```
`map` takes a function and a list and returns a new list of the function
applied to

```scheme
> ; (abs x) - the absolute value of x
> (map abs '(-1 2 -3 4 5 -6))
'(1 2 3 4 5 6)
```

## modulo

`modulo` is the equivalent of the `%` operator in Java and Python. It returns the quotient or remainder from n divided by d, with the sign of d.

```scheme
(modulo 13 4) ;1
(modulo -13 4) ;3
(modulo 13 -4) ;-3
(modulo -13 -4) ;-1
```
## not

`not` takes one argument and returns the opposite of it.

```scheme
; Not False is True
> (not #f)
#t

```

## or

`or` takes zero or more arguments and returns if any of them are true.

```
; False or True is True
> (or (equal? '(1 2) 'a) (> 34 5))
#t

; No arguments means none of them are true.
> (or)
#f
```

**Note**: `or` expands into a series of `if` branches when the compiler reads the code.
It cannot be used as a function with functions like [map](#map), [filter](#filter) and [reduce](#reduce).

## quotient

`quotient` is the whole number equivalent of the `/`. It returns the quotient of n divided by d, truncated towards zero.

```scheme

(quotient 13 4) ;3
(quotient -13 4) ;-3
(quotient 13 -4) ;-3
(quotient -13 -4) ;3
```

## Comparison Functions

**Note**: Regular comparison functions only work on numbers (integers and floats).

| Symbol | Sample Usage   |
|--------|----------------|
| =      | `(= 1 1)`      |
| >      | `(> 100 3)`    |
| >=     | `(>= 10 2)`    |
| <      | `(< 5 7)`      |
| <=     | `(<= 4.5 6.7)` |

### equal?

See [equal?](#equal_function)

# Functions We Will Define <a name="user-defined"/>

- [filter](#filter)
- [reduce](#reduce)
- [Cartesian/Cross Product](#cross-product)
- [Set functions](#set-functions)

## filter

```scheme
(filter pred lst)
```
`filter` is a powerful function for processing data. It takes a list and returns
a new list only containing

## reduce

```scheme
(reduce f init lst)
```
`reduce` is a core function in functional programming. It is useful for aggregation functions
(functions that compute based on a collection of values rather than a single value), such as
`sum`, `product`, and the union of sets.

```scheme
; For each element in the list, ignore the value and increment the length by 1
> (define (length lst)
    (reduce (lambda (len _) (+ len 1)) 0 lst))

> ; The sum of '(1 2 3 4 5 6 7) is the same as
> ; (+ (+ (+ (+ (+ (+ (+ 0 1) 2) 3) 4) 5) 6) 7)
> (define (sum numbers)
    (reduce + 0 numbers))
```

## cross-product

```scheme
(cross-product s t)
```
`cross-product` takes two sets A and B and returns `{(a, b) | a in A, b in B}`

## Set functions

### element?

```scheme
(element? item list)
```

Takes an item and a list and returns whether or not the element is present in the list

```scheme
> (element? 5 '(1 2 3 4 5))
#t

> (element? 'lieb '(buildings we still have))
#f
```

### intersection

```scheme
(intersection s t)
```

Given two sets, returns the set of elements which are in BOTH sets.

```scheme
> (intersection '(1 2 3) '(4 3 2))
'(2 3)
> (intersection '(r i p) '(l i e b))
'(i)
> (intersection '() '())
'()
```

### make-set

```scheme
(make-set list)
```

Takes a list and removes all duplicate elements.

```scheme
> (make-set '(0 0 0))
'(0)
> (make-set '(1 2 3 2 4 5))
'(1 2 3 4 5)
```

**Note**: There are multiple ways to implement `make-set` and some of them don't preserve the
order of the set (which when working with sets is not necessary)

### set-equal?

```scheme
(set-equal? s t)
```

Determines whether two sets are equivalent (i.e. A = B => every element in A
is in B and every element in B is in A)

```scheme
> (set-equal? '() '())
#t

> (set-equal? '(a b c) '(a b c))
#t

> (set-equal? '(1 2 3 4) '(4 3 1 2))
#t

> (set-equal? '(1 2 3) '(1 2 4))
#f
```

### subset?

```scheme
(subset? s t)
```

Returns true if `s` is a subset of `t`. I.e., if every element of `s` is in `t`.

```scheme
> (subset? '() '())
#t
> (subset? '(1 2 3) '(1 2 3 4 5))
#t
> (subset? '(115 284 385) '(115 146 284 135 385 392))
#t
> (subset? '(-2 0 2) '(-1 1 3))
#f
> (subset? '(-1 1 2) '(-1 1 3 5 7))
#f
```

### union

```scheme
(union s t)
```

Given two sets, return a list representing the set which contains all of the elements
from each set EXACTLY once.

```scheme
> (union '(1 2 3) '(4 5 6))
'(1 2 3 4 5 6)

> (union '(1 2 3) '(1 2))
'(1 2)

> (union '(1 1 1) ())
'(1)
```


# Predicates

A predicate is a function/procedure/method that returns a boolean (true/false) value
based on its inputs. Here is a list of common predicates built into the Racket module
[eopl](http://docs.racket-lang.org/eopl/) that we use as the language for all of our labs.

| Predicate       | Description                      |
|:----------------|:---------------------------------|
| `(boolean? x)`  | `x` is a boolean (`#t` or `#f`)  |
| `(even? x)`     | `x` is an even number            |
| `(integer? x)`  | `x` is an integer (whole number) |
| `(list? x)`     | `x` is a list                    |
| `(negative? x)` | `x` is negative (`x < 0`)        |
| `(null? x)`     | `x == null` OR `x == '()`        |
| `(number? x)`   | `x` is a number                  |
| `(odd? x)`      | `x` is an odd number             |
| `(positive? x)` | `x` is positive (`x > 0`)        |
| `(string? x)`   | `x` is a string                  |
| `(symbol? x)`   | `x` is a symbol                  |
| `(zero? x)`     | `x == 0`                         |

For more information on any of the commands built-in to EOPL, see
https://docs.racket-lang.org/eopl/

<!-- Written by Edward Minnix (eminnix@stevens.edu)
            and Sam Kraus (skraus@stevens.edu) -->