;Vraag:
;Schrijf de procedure (depth-weird x) die het aantal recursieve oproepen (= de recursie-diepte) van weird voor een bepaalde x teruggeeft.

; f(x) = x = 1?    => 1
;      = x = even? => f(x/2)
;      else        => f(3 * x + 1)

;Expected results:

;Notes:

;Requirments
(#%require racket/trace)

;Antwoord
(define (depth-weird x)
  (define (rec x count)
    (cond
      ((= x 1) count)
      ((even? x) (rec (/ x 2) (+ count 1)))
      (else (rec (+ (* 3 x) 1) (+ count 1)))
      )
    )
  (rec x 0)
  )

;Trace
;(trace depth-weird)

;Tests
(depth-weird 4)
(display "Expected: 2.\n")
(depth-weird 15)
(display "Expected: 17.\n")
(depth-weird 200)
(display "Expected: 26.\n")
