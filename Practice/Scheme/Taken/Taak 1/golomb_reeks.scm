;Vraag
;Schrijf nu een procedure (golomb-reeks n) die de eerste n getallen van de Golomb reeks op je scherm print. Ook hier mag je er van uit gaan dat n >= 1.

;Verwachte resultaat
;> (golomb-reeks 20)
;1 2 2 3 3 4 4 4 5 5 5 6 6 6 6 7 7 7 7 8

;Oplossing
(define (golomb n)
  (cond
    ((= 1 n) 1)
    (else (+ 1 (golomb (- n (golomb (golomb (- n 1)))))))
    )
  )

(define (golomb-reeks n)
  (define (golomb-iter counter)
    (if (>= n counter)
      (begin
        (display (golomb counter))
        (display " ")
        (golomb-iter (+ 1 counter))
        )
      )
    )
  (golomb-iter 1)
  )

;Test
(golomb-reeks 20)