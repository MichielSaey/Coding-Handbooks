;Schrijf een analoge functie my-or (zonder gebruik te maken van de special form or)
;en geef zelf een expressie die zich voor deze my-or verschillend gedraagt dan
;wanneer je de standaard Scheme or gebruikt.
(#%require racket/trace)

(define (my-or x y)
  (cond
    ((eq? #t x) #t)
    ((eq? #t y) #t)
    (else #f)
    )
  )

(my-or #t #t)
(my-or #t #f)
(my-or #f #t)
(my-or #f #f)
