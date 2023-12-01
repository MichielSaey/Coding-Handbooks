;Vraag
;Schrijf de procedure my-append op iteratieve wijze, (zonder append te gebruiken?) . Doe dit zo efficiënt mogelijk.

;Verwachte resultaat
;> (my-append '(1 2 3) '(4 5))
;(1 2 3 4 5)
;> (my-append '(1 2 3) '())
;(1 2 3)
;> (my-append '() '(1 2 3))
;(1 2 3)
;> (my-append '() '())
;()


(define (my-append list1 list2)
  (define (list-iter list result)
    (if (null? list)
      result
      (list-iter  (cdr list) (cons (car list) result))
      )
    )

  (list-iter (reverse list1) list2)
  )

;Test
(my-append '(1 2 3) '(4 5))
(my-append '(1 2 3) '())
(my-append '() '(1 2 3))
(my-append '() '())