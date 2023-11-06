;Definieer tenslotte zelf een functie my-if. Hierbij mag je geen gebruik maken van de bestaande special form if, maar wel van de cond special form.
(#%require racket/trace)

(define (my-if op x y)
  (cond
    ((eq? #t op) x)
    ((eq? #f op) y)
    )
  )

;(my-if #t 3 4)
; 3
;(my-if #f 3 4)
; 4