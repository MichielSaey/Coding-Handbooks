# Bruteforce algoritme

The bruteforce algorithm is a simple algorithm used for patternrecognition. It is used to find a pattern in a text, and return an _'offset'_ or _'shift'_ value. This value is the index of the first character of the pattern in the text. If the pattern is not found in the text, the algorithm will return a `false`. 

```scheme
(define (bruteforce t p)
  (define n-t (string-length t)) ; length of text
  (define n-p (string-length p)) ; length of pattern
  (let loop 
    (( i-t 0) ; index in text
      ( i-p 0)) ; index in pattern
    (cond
      ((> i-p (- 1 n-p) ; if index in pattern is greater than length of pattern 
         i-t)  ; return index in text
      ((> i-t (- n-t n-p) ; if index in text is greater than length of text - length of pattern 
         #f) ; return false, this means the pattern is not found in the text
      ((eq? (string-ref t (+ i-t i-p)) (string-ref p i-p)) ; if character in text is equal to character in pattern
        (loop i-t (+ i-p 1))) ; continue with next character in pattern
      (else ; if character in text is not equal to character in pattern
        (loop (+ i-t 1) 0))))))) ; continue with next character in text
```

It starts at the first character of the text and compares it with the first character of the pattern. If they are the same, it will compare the second character of the text with the second character of the pattern. If they are not the same, it will compare the first character of the text with the second character of the pattern. This will continue until the end of the text or the end of the pattern is reached. If the end of the pattern is reached, the pattern is found in the text. If the end of the text is reached, the pattern is not found in the text, and the procedure return a false.

## Performance

The performance of the bruteforce algorithm is not very good. The worst case scenario is when the pattern is not found in the text. In this case, the algorithm will have to compare every character in the text with the first character of the pattern. This will result in a time complexity of `O(nt*np)`, where `nt` is the length of the text and `np` is the length of the pattern.