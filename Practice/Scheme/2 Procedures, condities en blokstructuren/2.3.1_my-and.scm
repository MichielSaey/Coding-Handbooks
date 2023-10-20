;Schrijf, zonder gebruik te maken van de voorgedefinieerde Scheme special form and,je eigen functie my-and,
;die twee parameters neemt en enkel #t teruggeeft indien ze beide #t zijn.Doe dit met behulp van een if.
(#%require racket/trace)

(define (my-and x y)
  (if (eq? #t x) (if (eq? #t y) #t #f) #f)
  )

(my-and #t #t)
(my-and #t #f)
(my-and #f #t)
(my-and #f #f)