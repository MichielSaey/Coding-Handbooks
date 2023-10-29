;Vraag
;Veralgemeen de procedure uit de vorige oefening tot een procedure (super-merge-n lsts n) die een willekeurig
;aantal lijsten samenvoegt door achtereenvolgens n elementen van elke lijst te nemen. De lijsten zitten samen
;in de formele parameter lsts.

;> (super-merge-n '((a b c d e f)
;                   (g h i j k)
;                   (l m n o p q)
;                   (r s t u v w))
;                   3)
;(a b c g h i l m n r s t d e f j k o p q u v w)

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

;Oplossing
(define (super-merge-n lsts n)
  (define (iter-lst lsts result)
    (cond
      ((null? lsts) result)
      ((not (null? lsts))
        (if (null? (car lsts))
          (iter-lst (cdr lsts) result)
          (iter-lst
            ;lists, with first removed, remainder added to back
            (append (cdr lsts) (list (remainder-after-n (car lsts) n)))
            ;first n of car added to resut
            (append result (first-n (car lsts) n))
            )
          )
        )
      )
    )
  (iter-lst lsts '())
  )

;(first-n '(1 2 6 7 3 4 8 9 5) 3)
;(remainder-after-n '(1 2 6 7 3 4 8 9 5) 3)

(super-merge-n '((a b c d e f)
                  (g h i j k)
                  (l m n o p q)
                  (r s t u v w))
  3)