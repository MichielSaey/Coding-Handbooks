;Vraag:
;Schrijf de procedures (my-odd? n) en (my-even? n) in functie van elkaar. Je oplossing mag dus geen gebruik
;maken van de even? en odd? procedures van Scheme!

;Expected results:
; is 2 even?
; is 1 oneven?
; is 0 even? #t!

; is 3 even?
; is 2 oveven?
; is 1 even?
; is 0 oneven? #f!

;Notes
;let op het vraag teken, dus enkel t of f terug geven
;Als je kijkt naar de panopte opnames van de oefening worden er veel idngen duidelijk gemaakt die anders niet beschreven worden

;My-Odd?
(define (my-odd? n)
  (if (zero? n)
    (if (zero? (modulo n 2)) #f #t)
    (my-even? (- n 1))
    )
  )

;My-Even?
(define (my-even? n)
  (if (zero? n)
    (if (zero? (modulo n 2)) #t #f)
    (my-odd? (- n 1))
    )
  )

;Tests
(my-odd? 2)
(display "Expected: #f.\n")
(my-odd? 3)
(display "Expected: #t.\n")
(my-even? 2)
(display "Expected: #t.\n")
(my-even? 3)
(display "Expected: #f.\n")