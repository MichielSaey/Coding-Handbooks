;Vraag:
;weird(x) = \left\lbrace\begin{array}{ll}  1  & \mbox{als } x=1 \\ weird (x/2) & \mbox{als  x even is}\\ weird (3*x+1) & \mbox{anders}\end{array}\right.
;Schrijf de procedure (weird x) die de wiskundige functie van eerder implementeert. Genereert je oplossing een recursief of iteratief proces?

; f(x) = x = 1?    => 1
;      = x = even? => f(x/2)
;      else        => f(3 * x + 1)

;Expected results:

;Notes:

;Requirments
(#%require racket/trace)

;Antwoord
(define (weird x)
  (cond
    ((= x 1) 1)
    ((even? x) (weird (/ x 2)))
    (else (weird (+ (* 3 x) 1)))
    )
  )

;Trace
(trace weird)

;Tests
(weird 1)
(display "Expected: 1.\n")
(weird 2)
(display "Expected: 1.\n")
(weird 15)
(display "Expected: 1.\n")
(weird 387)
(display "Expected: 1.\n")