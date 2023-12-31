Forked from [egregius313/scheme-help.md](https://gist.github.com/egregius313/e20246fbdb67861a05edaf7dbd0315d6)

- [Scheme Built-Ins](#basic)
- [Common Predicates](#predicates)
- [Commands We Will Define](#user-defined)

# Scheme


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

## ADT

ADT, or Abstract Data Type, is a data structure that is defined by its behavior that is similar to a class in an object oriented programming language. Creating an ADT in Scheme can be done in two ways, representing the data as lists or are as records. Lets see how we define a person using both the thechniques. First we will define a person using a list.

```scheme
#lang r7rs
(define-library
  (Hoofdstuk1 person_1)
  (export new person? name surname)
  (import
    (scheme base)
    (scheme cxr)
    (prefix (scheme write) io:)
    )
  (begin
    (define person-tag 'person)

    (define (new name surname)
      (list person-tag name surname)
      )

    (define (person? any)
      (and (pair? any)
        (eq? (car any) person-tag))
      )

    (define (name p)
      (cadr p))

    (define (surname p)
      (caddr p))
    )
  )
```

Here you see that we need to define a tag, this is a symbol that is used to identify the type of the list. This is needed because lists are not typed, so we need to add a tag to the list to identify the type. We also need to define a constructor, this is a function that takes the fields of the type as arguments and returns a new instance of the type. We also need to define a predicate, this is a function that takes an instance of the type and returns true if it is an instance of the type, and false otherwise. And lastly we need to define the selectors, these are functions that take an instance of the type and return the value of the field. We can use the ADT as follows.

```scheme
(import (scheme write)
  (scheme base)
  (prefix(Hoofdstuk1 person_1) person:))

(define fred (person:new "Fred" "De Man"))

(display fred)                (newline)
(display (person:person? fred)) (newline)
(display (person:name fred))    (newline)
(display (person:surname fred)) (newline)
```

In the following example we use `define-library` to define a library, this is syntax added with the R7RS standaed, and allows you to define a library with multiple functions. In the first part of the `degine-library` we define the functions that we want to export, these are the functions externally available for use. This is the interface of the library. In the second part we define the functions that we want to import, this is usually the scheme libraries, but it can be any other library you wish. After that we place a `(begin ...)` statement, this allows us to define multiple functions in the same library.

```scheme
(define-library
  (Hoofdstuk1 person)
  (export new person? name surname age age! salary salary! display)
  (import
    (scheme base)
    (prefix (scheme write) io:)
    )
  (begin
    (define-record-type person
      (new n sn a s)
      person?
      (n name)
      (sn surname)
      (a age age!)
      (s salary salary!))

    (define (display p)
      (io:display (name p))
      (io:display " ")
      (io:display (surname p))
      (io:display " ")
      (io:display (age p))
      (io:display " ")
      (io:display (salary p))
      (io:display "\n")
      )
    )
  )
```
Here a `define-record-type` is used. This is a macro that allows us to define a new data type. The first argument is the name of the type, the second is the constructor, the third is the predicate, and the rest are the fields.

The constructor is a function that takes the fields as arguments and returns a new instance of the type. The predicate is a function that takes an instance of the type and returns true if it is an instance of the type, and false otherwise. The fields are the fields of the type, and the last part is the mutator functions. These are functions that take an instance of the type and a new value for the field, and return a new instance of the type with the field changed.

Using the code above a total of 8 fucntions: constructor, predicate, mutators, or setter, and selectors, or getters, are created. The constructor is called `new`, the predicate is called `person?`, the setters are called `age!` and `salary!`, and the selectors are called `name`, `surname`, `age`, and `salary`. The `display` function is also defined, but this is not part of the ADT. Below we can see how to use the functions defined in the ADT.

```scheme
(import (scheme write)
  (scheme base)
  (prefix(Hoofdstuk1 person_2) person:))

(define fred (person:new "Fred" "De Man" 20 2500))

(person:display fred)
(display (person:person? fred)) (newline) > #t
(display (person:name fred))    (newline) > Fred
(display (person:surname fred)) (newline) > De Man

(person:age! fred (+(person:age fred) 1))
(display (person:age fred))     (newline) > 21

(define (opslag p a)
  (person:salary! p (+(person:salary p) a))
  )

(opslag fred 500)

(display (person:salary fred))  (newline) > 3000
```

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

## caddr

`caddr` returns the third element of a list.

```scheme
> (caddr (list 1 2 3))
3
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

When using R7RS Scheme, you need to import the `display` function from the `write` library. This is done by adding `(import (scheme write))` to the top of your file. 

`display` is the equivalent of `print` in Python or `System.out.println` in
Java except it does not print the new line by default (you need to add `\n` to
the end of the string literal for the new line).

```scheme
(display string)
```

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

The `let` expression is used to create local variables. It is similar to `define` except that the variable is only accessible within the `let` expression. The let expresion is syntactic sugar for a lambda expression. The following two expressions are equivalent.

```scheme
> (let ((x 10)
        (y 20))
    (+ x y))

> 30

> (let ((result (quotient 13 4)))
    (display result)
    (display "\n"))
```

a `Let` can aslo me named, so it can be reused with diffrent expresions. This can comenlly be used to write more elegant iterating function. 

```scheme
(define (fac n)
  (let fac-loop
    ((result 1)
      (factor n))
    (if (= factor 0)
      result
      (fac-loop (* result factor) (- factor 1)))))
```



```scheme
> (define (test a b)
  (let ((a 5)
        (c (+ a 2)))
    (display a)
    (display b)
    (display c)))

(test 1 2)
; 523

> (define (test a  b)
  ((lambda (a c)
     (display a)
     (display b)
     (display c))
    5 (+ a 2)))

(test 5 7)
; 523
```
## let*

The `let*` expression is similar to `let` except that the variables are defined sequentially. This means that the variables can reference each other. This is useful when you need to define a variable that depends on another variable.

```scheme
> (let* ((x 10)
         (y (+ x 2)))
    (+ x y))

22
```

Where `let` is syntactic sugar for a lambda expression, `let*` is syntactic sugar for nested lambda expressions. The following two expressions are equivalent.

```scheme
> (define (test a b)
  (let* ((a 5)
         (c (+ a 2)))
    (display a)
    (display b)
    (display c)))

(test 1 2)
; 527

> (define (test a  b)
  ((lambda (a)
     ((lambda (c)
        (display a)
        (display b)
        (display c))
      (+ a 2)))
    5))

(test 1 2)
; 527
```

## letrec

The `letrec` expression is used to create recursive functions using lambda expressions.


```scheme
> (define (test n) 
    (letrec ((fact (lambda (n)
                     (if (= n 0)
                         1
                         (* n (fact (- n 1)))))))
    (fact 5)))

> (test 5)
120
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
* [append](#append)
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

## mcons

The `mcons` function is used to create mutable lists. Mutable lists are lists that can be modified after they are created. This is useful when you need to create a list that will be modified later. 

```scheme
(mcons element list)
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

## vector or make-vector

`make-vector` can be used two ways. The first way is to create a vector of a certain size. The second way is to create a vector filled with certain values.

```scheme
(make-vector 10)
#(0 0 0 0 0 0 0 0 0 0)

(make-vector 10 1)
#(1 1 1 1 1 1 1 1 1 1)
```

a vector can also be created using the `vector` function. This function takes any number of arguments and returns a vector containing those arguments.

Vectors in scheme are immutable. This means that once they are created, they cannot be modified. They are also destructivy, this means that every time a vector is modified, a new vector is created, and the old one destroyed(beceause they are immultable). This is different from lists, which are mutable and non-destructive. 

```scheme
(vector 1 2 3 4 5)
#(1 2 3 4 5)

(vector "apple" "banana" "orange")
#("apple" "banana" "orange")
```

## vector-length

`vector-length` returns the length of a vector. In the memory it will save the length of the vector so it can be accessed in O(1) time. VERY FAST!

```scheme
> (define v0 (vector 1 "twee" 3.0))
> v0
#(1 "twee" 3.0)
> (vector-length v0)
3
```

## vector-ref

`vector-ref` returns the value at a certain index in a vector. The given index must be less than the length of the vector, and starts counting at 0, like any other array. And unlike python, negative indexes are not allowed, this will throw an error.

```scheme
> (define v0 (vector 1 "twee" 3.0))
> v0
#(1 "twee" 3.0)
> (vector-ref v0 1)
"twee"

```

## vector-set!

`vector-set!` sets the value at a certain index in a vector.

```scheme
> (define v0 (vector 1 "twee" 3.0))
> v0
#(1 "twee" 3.0)
> (vector-set! v0 1 "two")
> v0
#(1 "two" 3.0)
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


## Type checking functions

* vector?
* list?
* number?
* pair?
* string?

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