;Vraag
;Veralgemeen de procedure accumulate naar de procedure (filtered-accumulate combiner filter? null-value term a
;next b). Deze procedure heeft een extra argument filter?, een predikaat dat bepaalt welke termen er
;geaccumuleerd worden en welk niet. Zorg ervoor dat je procedure een iteratief process genereert.

(define (accumulate combiner null-value term a next b)
  (define (iter result a)
    (if (> a b)
      result
      (iter (combiner result (term a)) (next a))
      )
    )
  (iter null-value a)
  )


(define (filtered-accumulate combiner filter? null-value term a next b)
  (define (iter result a)
    (if (> a b)
      result
      (if (filter? a)
        (iter (combiner result (term a)) (next a))
        (iter result (next a))
        )
      )
    )
  (iter null-value a)
  )

;Test
(filtered-accumulate + even? 0 (lambda (a) a) 1 (lambda (a) (+ a 1)) 9)
(filtered-accumulate + odd?  0 (lambda (a) a) 1 (lambda (a) (+ a 1)) 9)