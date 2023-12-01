;Vraag
;Schrijf de functie (change e1 e2 l) die een lijst teruggeeft, gelijk aan lijst l, maar waarin alle elementen
;gelijk aan e1 vervangen zijn door e2. Gebruik (eq? e1 e2) om twee elementen te vergelijken. De procedure mag
;een recursief proces genereren.

;Verwachte resultaat
;> (change 1 999 '(1 2 1 3 1 4 1 5 1))
;(999 2 999 3 999 4 999 5 999)
;> (change 1 999 '(2 3 4 5 6 7))
;(2 3 4 5 6 7)
;> (change 1 999 '(1))
;(999)
;> (change 1 999 '())
;()

;Oplossing
(define(change e1 e2 l)
  (define (list-iter source result)
    (if (null? source)
      result ;if 0 return the result list
      (if (eq? e1 (car source))
        (list-iter (cdr source) (append result (list e2)))
        (list-iter (cdr source) (append result (list (car source))))
        )
      )
    )
  (list-iter l '())
  )

;Test
(change 1 999 '(1 2 1 3 1 4 1 5 1))
(change 1 999 '(2 3 4 5 6 7))
(change 1 999 '(1))
(change 1 999 '())