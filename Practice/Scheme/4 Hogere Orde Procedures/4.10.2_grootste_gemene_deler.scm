;Vraag
;Schrijf een procedure (product-gcd n) die het product berekent van alle gehele getallen i < n waarvoor geldt
;dat (= (gcd i n) 1). (Opmerking: gcd is een voorgedefinieerde Scheme-procedure die de grootste gemene deler van
;2 getallen berekent.)

(define (filtered-accumulate combiner filter? null-value term a next b)
  (define (iter result a)
    (if (> a b)
      result
      (if (filter? a b)
        (iter (combiner result (term a)) (next a))
        (iter result (next a))
        )
      )
    )
  (iter null-value a)
  )

(define (product-gcd n)
  (filtered-accumulate * (lambda (i n) (= (gcd i n) 1)) 1 (lambda (a) a) 1 (lambda (a) (+ a 1)) n)
  )

