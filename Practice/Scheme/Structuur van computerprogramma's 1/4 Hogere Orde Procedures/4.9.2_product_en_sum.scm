;Vraag
;Schrijf product en sum met behulp van accumulate.

(define (accumulate combiner null-value term a next b)
  (define (iter result a)
    (if (> a b)
      result
      (iter (combiner result (term a)) (next a))
      )
    )
  (iter null-value a)
  )


(define (product factor a next b)
  (accumulate * 1 factor a next b)
  )

(define (sum term a next b)
  (accumulate + 0 term a next b)
  )

;Test
;(product (lambda (a) a) 2 (lambda (a) (+ a 2)) 10)
;(sum (lambda (a) a) 2 (lambda (a) (+ a 2)) 10)