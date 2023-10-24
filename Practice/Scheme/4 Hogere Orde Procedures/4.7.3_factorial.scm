;Schrijf factorial met behulp van product.

;Dus een procedure die niets veranderd aan zijn argumenten
;fac n => 1 * 2 * 3 * 4 * ... * n

(define (product factor a next b)
  (if (> a b)
    1
    (* (factor a) (product factor (next a) next b))
    )
  )

(define (factorial n)
  (define (id x) x)
  (product id 1 (lambda (x) (+ x 1)) n)
  )

(factorial 5)