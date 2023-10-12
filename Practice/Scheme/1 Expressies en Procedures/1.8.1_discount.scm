(define (discount prijs korting)
  (* prijs (- 1 (/ korting 100)))
  )


(discount 10 5)
(discount 29.90 50)