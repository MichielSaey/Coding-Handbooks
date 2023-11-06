;Vraag
;De procedure (sum-lists l1 l2) heeft als argumenten 2 lijsten met getallen, en geeft een lijst terug met de
;sommen van de overeenkomstige elementen van de input-lijsten. Merk op dat de twee input-lijsten niet dezelfde
;lengte hoeven te hebben. In dat geval worden de resterende elementen van de langste lijst gewoon overgenomen.

;Schrijf een recursieve versie, noem het (rec-sum-lists l1 l2).

;> (rec-sum-lists '(1 2 3 4) '(5 6 7))
;(6 8 10 4)
;> (rec-sum-lists '(1 2 3 4) '())
;(1 2 3 4)
;> (rec-sum-lists '() '(1 2 3))
;(1 2 3)

(define (rec-sum-lists l1 l2)
  (cond
    ((and (not (null? l1)) (not (null? l2)))
      (append (list (+ (car l1) (car l2))) (rec-sum-lists (cdr l1) (cdr l2) ))
      )
    ((null? l2)
      (if (null? l1)
        '()
        (append (list (car l1)) (rec-sum-lists (cdr l1) '()))))
    ((null? l1)
      (if (null? l2)
        '()
        (append (list (car l2)) (rec-sum-lists '() (cdr l2)))))
    )
  )

(rec-sum-lists '(1 2 3 4) '(5 6 7))
(rec-sum-lists '(1 2 3 4) '())
(rec-sum-lists '() '(1 2 3))