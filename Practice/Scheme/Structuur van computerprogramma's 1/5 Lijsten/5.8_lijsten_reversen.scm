;Vraag
;Schrijf de procedure (rec-reverse l) die een lijst teruggeeft met dezelfde elementen als l maar in de
;omgekeerde volgorde. Maak 2 versies: één die een recursief proces en één die een iteratief proces genereert.
;Noem de recursieve versie (rec-reverse l) en de iteratieve versie (iter-reverse l).

;Verwachte resultaat
;> (rec-reverse '(1 2 3))
;(3 2 1)
;> (rec-reverse '(1))
;(1)
;> (rec-reverse '())
;()
;> (iter-reverse '(1 2 3))
;(3 2 1)
;> (iter-reverse '(1))
;(1)
;> (iter-reverse '())
;()

;Oplossing
(define(rec-reverse l)
  (if (<= (length l) 1) ;if 1 return the list
    l
    ;if not get the last and add it to to the front of the result of the next rec
    (append (rec-reverse (cdr l)) (list (car l)))
    )
  )

(define (iter-reverse l)
  (define (list-iter list result)
    (if (null? list) ;if 1 return the list
      result
      (list-iter (cdr list) (cons (car list) result))
      )
    )
  (list-iter l '())
  )

;Test
;(rec-reverse '(1 2 3))
;(rec-reverse '(1))
;(iter-reverse '(1 2 3))
;(iter-reverse '(1))
;(iter-reverse '())