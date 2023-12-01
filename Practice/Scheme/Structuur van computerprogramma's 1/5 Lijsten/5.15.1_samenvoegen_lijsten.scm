;Vraag
;Schrijf een procedure die 2 lijsten samenvoegt tot 1 enkele lijst door telkens n elementen van de eerste lijst
;te laten volgen door n elementen van de tweede lijst, enzovoort. Indien er minder dan n elementen overblijven
;in een lijst, neem je alles wat er overblijft. Doe dit zowel op recursieve als iteratieve wijze. Noem de
;recursieve versie (rec-merge-n lst1 lst2 n). Noem de iteratieve versie (iter-merge-n lst1 lst2 n).

;> (rec-merge-n '(1 2 3 4 5) '(6 7 8 9) 2)
;(1 2 6 7 3 4 8 9 5)
;> (rec-merge-n '(1 2 3 4 5) '(6 7 8 9) 3)
;(1 2 3 6 7 8 4 5 9)
;> (rec-merge-n '(1 2) '(3 4 5 6) 4)
;(1 2 3 4 5 6)
;> (iter-merge-n '(1 2 3 4 5) '(6 7 8 9) 2)
;(1 2 6 7 3 4 8 9 5)
;> (iter-merge-n '(1 2 3 4 5) '(6 7 8 9) 3)
;(1 2 3 6 7 8 4 5 9)
;> (iter-merge-n '(1 2) '(3 4 5 6) 4)
;(1 2 3 4 5 6)

(define (first-n lst n)
  (define (iter-list lst n result)
    (if(or (null? lst) (zero? n))
      result
      (iter-list (cdr lst) (- n 1) (append result (list (car lst))))
      )
    )
  (iter-list lst n '())
  )


(define (remainder-after-n lst n)
  (if(or (null? lst) (zero? n))
    lst
    (remainder-after-n (cdr lst) (- n 1))
    )
  )

(define (rec-merge-n lst1 lst2 n)
  (cond
    ((not (null? lst1))
      (append (first-n lst1 n) (rec-merge-n lst2 (remainder-after-n lst1 n) n))
      )
    ((and (null? lst1) (null? lst2)) '())
    ((null? lst1) (rec-merge-n lst2 lst1 n))
    )
  )

(define (iter-merge-n lst1 lst2 n)
  (define (iter-lst lst1 lst2 result)
    (cond
      ((not (null? lst1))
        (iter-lst lst2 (remainder-after-n lst1 n) (append result (first-n lst1 n)))
        )
      ((and (null? lst1) (null? lst2)) result)
      ((null? lst1) (list-iter lst2 lst1 result))
      )
    )
  (iter-lst lst1 lst2 '())
  )

;(first-n '(1 2 6 7 3 4 8 9 5) 3)
;(remainder-after-n '(1 2 6 7 3 4 8 9 5) 3)

(rec-merge-n '(1 2 3 4 5) '(6 7 8 9) 2)
(rec-merge-n '(1 2 3 4 5) '(6 7 8 9) 3)
(rec-merge-n '(1 2) '(3 4 5 6) 4)

(iter-merge-n '(1 2 3 4 5) '(6 7 8 9) 2)
(iter-merge-n '(1 2 3 4 5) '(6 7 8 9) 3)
(iter-merge-n '(1 2) '(3 4 5 6) 4)