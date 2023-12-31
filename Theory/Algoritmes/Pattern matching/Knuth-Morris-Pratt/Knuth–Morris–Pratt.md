# Knuth–Morris–Pratt algorithm

The Knuth–Morris–Pratt algorithm is a string searching algorithm that uses a shift table to determine the next index in the text to compare with the pattern. This shift table is created using the Knuth–Morris–Pratt table algorithm. In large parts this algorithm is the same as the QuickSearch, and bruteforce algorithms. The difference is the last path of the algorithm. When there is a mismatch between the text and the pattern, the Knuth–Morris–Pratt algorithm will not start comparing the next character in the text with the first character in the pattern. Instead, it will use the shift table to determine the next index in the text to compare with the pattern. This will result in a time complexity of `O(nt+np)`.

```scheme
(define (match t p)
  (define n-t (string-length t))
  (define n-p (string-length p))
  (define sigma (compute-failure-function p))
  (let loop ((i-t 0) (i-p 0))
    (cond
      ((> i-p (- n-p 1)) i-t)
      ((> i-t (- n-t n-p)) #f)
      ((eq? (string-ref t (+ i-t i-p)) (string-ref p i-p)) (loop i-t (+ i-p 1)))
      (else (loop (+ i-t (- i-p (sigma i-p))) (if (> i-p 0) (sigma i-p) 0)))
      )
    )
  )
```

The compute failure function builds a table that contains the length of the longest prefix of the pattern that is also a suffix of the pattern. This table is used to determine the next index in the text to compare with the pattern. I looks for patterns in the pattern. If it finds a pattern it will set the value of the table at the index of the last character of the pattern to the length of the pattern. as an example, if the pattern is `lalaland`, the table will look like this `#(0 0 0 1 2 3 4 0)`. This means it has mached `lala` with `lala`. If it fails to find a pattern it will set the value of the table at the index of the last character of the pattern to 0. As an example, if the pattern is `lalalala`, the table will look like this `#(0 0 0 1 2 3 4 5 6)`. This means it has mached `lalala` with `lalala`. This alows the algorithm to skip the first 4 characters of the pattern when it fails to match the letter `n` with the letter `l`.

```scheme
(define (compute-failure-function p)
  (define n-p (string-length p))
  (define sigma-table (make-vector n-p 0))
  (let loop ((i-p 2) (k 0))
    (when (< i-p n-p)
      (cond
        ((eq? (string-ref p k) (string-ref p (- i-p 1)))
          (vector-set! sigma-table i-p (+ k 1)) 
          (loop (+ i-p 1) (+ k 1)))
        ((> k 0) 
          (loop i-p (vector-ref sigma-table k)))
        (else ; k=0
          (vector-set! sigma-table i-p 0) 
          (loop (+ i-p 1) k)))))
  (vector-set! sigma-table 0 -1)
  (lambda (q)
    (vector-ref sigma-table q)))
```

Lets do a step by step run through of the `compute-failure-function` for the example pattern `lalaland`, for a more detail run down debug the code in DrRacket.

1. `n-p` is set to 8
2. `sigma-table` is created with a length of 8, and all values set to 0
3. `i-p` is set to 2
4. `k` is set to 0
5. `a` at index `i-p` - 1 is equal to the `l` at index `k`
6. `sigma-table` at index `i-p` is set to `k` + 1(1)
7. The `loop` function is called with `i-p` + 1(4), and `k` + 1(1)
8. `a` at index `i-p` - 1 is equal to the `a` at index `k`
9. This repeats until `i-p` is equal to 7 and `k` is equal to 4, white a sigma table of `#(0 0 0 1 2 3 4 0)`. This means it has mached `lala` with `lala`.
10. After this the functions tries to match the letter `n`(index 7) with the letter `l`(index 4), this fails.
11. `k` is set to the value of `sigma-table` at index `k`(4), which is 2
12. It tries to match the letter `n`(index 7) with the letter `a`(index 2), this fails.
13. `k` is set to the value of `sigma-table` at index `k`(2), which is 0
14. It tries to match the letter `n`(index 7) with the letter `l`(index 0), this fails.
15. The `sigma-table` at index `i-p` is set to 0
16. The `loop` function is called with `i-p` + 1(8), and `k` = 0
17. `i-p` is equal to 8, so the `loop` function returns
18. The `sigma-table` at index 0 is set to -1
19. A lambda function is returned that returns the value of `sigma-table` at index `q`

## Performance

The worst case scenario for the compute failure function, `k` might go back to 0 for every character in the pattern. This means that during a loop from the compute failure function either `ip` or `ip` - `k` increases. `ip` - `k` <= `ip` <= `np`, so at a maximum te loop might run `2np` times. This means the time complexity of the compute failure function is `O(np)`.

The algorithm itself also has two path each loop. The first path is when the algorithm finds a match, and the second path is when the algorithm fails to find a match.

* Match: `i-t` + `i-p` => `i-t` + `i-p` + 1
* No match: `i-t` + `i-p` => `i-t` + `i-p` - `sigma`(`i-p`) + `sigma`(`i-p`) = `i-t` +  `i-p`

The conclusion here is the same as for the compute failure function. The algorithm might run `2nt` times. This means the time complexity of the algorithm is `O(nt)`. The total time complexity of the algorithm is `O(nt+np)`. which is better than the bruteforce algorithm, which has a time complexity of `O(nt*np)`.