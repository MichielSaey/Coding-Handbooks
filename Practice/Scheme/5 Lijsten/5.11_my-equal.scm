;Vraag:
;Schrijf de procedure (my-equal? l1 l2) die nagaat of twee lijsten van symbolen l1 en l2 gelijk zijn. Gebruik
;(eq? e1 e2) om twee elementen te vergelijken.

;> (my-equal? '(1 2 3) '(1 2 3))
;#t
;> (my-equal? '(1 2 3) '(4 5 6))
;#f
;> (my-equal? '(1 2 3) '(1 2))
;#f
;> (my-equal? '(1 2 3) '())
;#f
;> (my-equal? '() '(1 2 3))
;#f

;Oplossing:
;Note:
;scheme and is weird... and should only be 1 when all are one.
;#f and #f = #t <- WHAT

(define (my-equal? l1 l2)
  (cond
    ((and (null? l1) (null? l2)) #t)
    ((or (null? l1) (null? l2)) #f)
    ((eq? (car l1) (car l2)) (my-equal? (cdr l1)(cdr l2)))
    (else #f)
    )
  )


;Test:
(my-equal? '(1 2 3) '(1 2 3))
;t
(my-equal? '(1 2 3) '(4 5 6))
;f
(my-equal? '(1 2 3) '(1 2))
;f
(my-equal? '(1 2 3) '())
;f
(my-equal? '() '(1 2 3))
;f