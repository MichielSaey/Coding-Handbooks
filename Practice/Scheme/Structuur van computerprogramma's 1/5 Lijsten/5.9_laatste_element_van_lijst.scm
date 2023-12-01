;Vraag
;Schrijf een procedure last die het laatste element van een lijst teruggeeft.

;Verwachte resultaat
;> (last '(1 2 3))
;3
;> (last '(1))
;1
;> (last '())
;#f

;Oplossing
(define(last list)
  (cond
    ((null? list) #f) ;if 0 return false
    ((= (length list) 1 ) (car list) )
    (else (last (cdr list)))
    )
  )

;Test
(last '(1 2 3))
(last '(1))
(last '())