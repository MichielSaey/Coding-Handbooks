;Definieer een procedure (sign number) die een getal als argument neemt en 1 teruggeeft als dat nummer positief is,
; -1 als het negatief is en 0 als het getal gelijk is aan 0.

(define (sign number)
  (cond
    ((> number 0) 1)
    ((< number 0) -1)
    ((= number 0) 0)
    )
  )

(sign -5)
(sign 17.28)
(sign 0)
