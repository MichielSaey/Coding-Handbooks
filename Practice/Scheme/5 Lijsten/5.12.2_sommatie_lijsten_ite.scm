;Vraag
;De procedure (sum-lists l1 l2) heeft als argumenten 2 lijsten met getallen, en geeft een lijst terug met de
;sommen van de overeenkomstige elementen van de input-lijsten.

;Merk op dat de twee input-lijsten niet dezelfde lengte hoeven te hebben. In dat geval worden de resterende
;elementen van de langste lijst gewoon overgenomen.

;Schrijf een iteratieve versie, noem het (iter-sum-lists l1 l2).

;> (iter-sum-lists '(1 2 3 4) '(5 6 7))
;(6 8 10 4)
;> (iter-sum-lists '(1 2 3 4) '())
;(1 2 3 4)
;> (iter-sum-lists '() '(1 2 3))
;(1 2 3)

(define (iter-sum-lists l1 l2)
  (define (iter-lists list1 list2 result)
    (cond
      ((and (not (null? list1)) (not (null? list2)))
        (iter-lists (cdr list1) (cdr list2) (append result (list (+ (car list1) (car list2)))))
        )
      ((null? list2)
        (if (null? list1)
          result
          (iter-lists (cdr list1) '() (append result (list (car list1))))
          )
        )
      ((null? list1)
        (if (null? list2)
          result
          (iter-lists '() (cdr list2) (append result (list (car list2))))
          )
        )
      )
    )
  (iter-lists l1 l2 '())
  )

(iter-sum-lists '(1 2 3 4) '(5 6 7))
(iter-sum-lists '(1 2 3 4) '())
(iter-sum-lists '() '(1 2 3))