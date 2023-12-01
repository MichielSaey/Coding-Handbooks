;Schrijf eerst een versie die een recursief process genereert.
;Noem deze versie (rec-add a b). Je mag ervan uitgaan dat a en
;b positieve getallen zijn.
;(#%require racket/trace)

(define (1- x) (- x 1))
(define (1+ x) (+ 1 x))

;Recursief
(define (rec-add a b)
  (if (= b 0)
    a
    (1+ (rec-add a (1- b)))
    )
  )

;(trace rec-add)
;(trace 1+)
;(trace 1-)

(rec-add 4 5)
(rec-add 0 0)
(rec-add 3 2)
(rec-add 3 10)
;`rec-add` is recursive