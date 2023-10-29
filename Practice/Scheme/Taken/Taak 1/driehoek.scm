;Vraag
;Schrijf nu een procedure (pascal-driehoek n) die de eerste n rijen van de driehoek van Pascal op het scherm
;print. Hint: maak gebruik van meer dan 1 hulpprocedure in je oplossing.

;> (pascal-driehoek 7)
;1
;1	1
;1	2	1
;1	3	3	1
;1	4	6	4	1
;1	5	10	10	5	1
;1	6	15	20	15	6	1
;1	7	21	35	35	21	7	1

;Je kan (display "\t") gebruiken om genoeg spaties tussen getallen te printen.

;> (begin (display 1) (display "\t")
;         (display 2) (display "\t")
;         (display 3))
;1	2	3

;Notes

(define (binom n k)
  (cond
    ((> k n) 0)
    ((zero? k) 1) ;catch alle plaatsen waar een 1 moet staan, en return 1
    ((zero? n) 1)
    (else (+ (binom (- n 1) (- k 1)) (binom (- n 1) k)))
    ;doe de som van twee andere binom calls (binom n-1 k-1) en (binom n-1 k)
    )
  )

(define (pascal-lijn n)
  (display (binom n 0))

  (define (lijn-iter counter)
    (if (<= counter n)
      (begin
        (display "\t")
        (display (binom n counter))
        (lijn-iter (+ counter 1))
        )
      )
    )
  (lijn-iter 1)
  (display "\n")
  )

(define (pascal-driehoek n)
  (define (driehoek-iter counter)
    (if (<= counter n)
      (begin
        (pascal-lijn counter)
        (driehoek-iter (+ counter 1))
        )
      )
    )
  (driehoek-iter 0)
  )

;Test
(pascal-driehoek 7)