;Vraag
;Schrijf factorial met behulp van product.

(define (product factor a next b)
  (if (> a b)
    1
    (* (factor a) (product factor (next a) next b))
    )
  )

(define (iter-product factor a next b)
  (define (iter result a)
    (if (> a b)
      result
      (iter (* result (factor a)) (next a))
      )
    )
  (iter 1 a)
  )

;Test
(iter-product (lambda (a) a) 2 (lambda (a) (+ a 2)) 6)
(iter-product (lambda (a) a) 1 (lambda (a) (+ a 2)) 6)lambda (a) a) 1 (lambda (a) (+ a 2)) 6)