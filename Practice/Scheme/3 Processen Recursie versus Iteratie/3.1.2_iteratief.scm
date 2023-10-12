;Schrijf nu een versie die een iteratief process genereert. Noem deze versie (iter-add a b).
;Ook hier mag je er weer van uitgaan dat a en b positieve getallen zijn.
;(#%require racket/trace)

(define (1- x) (- x 1))
(define (1+ x) (+ 1 x))

;Iteratief
(define (iter-add a b)
  (if (= b 0)
    a
    (iter-add (1+ a)(1- b))
    )
  )

;(trace rec-add)
;(trace 1+)
;(trace 1-)

;(iter-add 4 5)
;(iter-add 0 0)
;(iter-add 3 2)
;(iter-add 3 10)