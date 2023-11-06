;Vraag
;Schrijf de procedure (accumulate combiner null-value term a next b), die een veralgemening is van de procedures
;sum en product. Schrijf accumulate op iteratieve wijze. combiner is een procedure die specificeert hoe de
;huidige term moet gecombineerd worden met de accumulatie van de voorgaande termen. null-value specificeert de
;initiëele waarde van de accumulatie.

(define (accumulate combiner null-value term a next b)
  (define (iter result a)
    (if (> a b)
      result
      (iter (combiner result (term a)) (next a))
      )
    )
  (iter null-value a)
  )

;Test
;(accumulate + 0 (lambda (a) a) 1 (lambda (a) (+ a 1)) 5)