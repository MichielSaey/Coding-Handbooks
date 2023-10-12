;Definieer een predicaat leap-year? dat een jaartal als argument neemt en teruggeeft of het betreffende jaar een
;schrikkeljaar is. Alle jaren die deelbaar zijn door 400 zijn schrikkeljaren, alle jaren die deelbaar zijn door 100
; (maar niet door 400) zijn geen schrikkeljaren, en alle jaren die deelbaar zijn door 4 (maar niet door 100) zijn wel
; schrikkeljaren. Alle jaren die niet aan de voorgaande voorwaarden voldoen zijn dan weer geen schrikkeljaren.

(define (leap-year? year)
  (define (devides? year devider)
    (if (= (modulo year devider) 0)
      #t
      #f
      )
    )
  (cond
    ((devides? year 400) #t)
    ((devides? year 100) #f)
    ((devides? year 4) #t)
    (else #f)
    )
  )

(leap-year? 1989)
(leap-year? 2000)
(leap-year? 1900)