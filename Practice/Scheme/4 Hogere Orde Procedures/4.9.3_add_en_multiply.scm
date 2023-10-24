;Vraag
;Schrijf de procedures (add a b) en (multiply a b) om respectievelijk 2 positieve getallen op te tellen en te
;vermenigvuldigen. Maak hierbij gebruik van accumulate.

;Tip: kijk naar oefeningen 3.1 en 3.2 voor inspiratie.

(define (accumulate combiner null-value term a next b)
  (define (iter result a)
    (if (> a b)
      result
      (iter (combiner result (term a)) (next a))
      )
    )
  (iter null-value a)
  )


(define (multiply a b)
  (accumulate * b (lambda (a) a) a (lambda (a) (+ a 1)) a)
  )

(define (add a b)
  (accumulate + b (lambda (a) a) a (lambda (a) (+ a 1)) a)
  )

;Test
(add 4 5)
;9
(multiply 5 2)
;10