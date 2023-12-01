;Voorbeeld tentamen Oefening 3: Lijsten
;(a) Schrijf een functie (schrap-3 lst) die van een gegeven lijst elk derde element schrapt.

;> (schrap-3 '(1 2 3 4 5 6 7 8))
;(1 2 4 5 7 8)
;> (schrap-3 '(a b c d e f g h j k l m n o p))
;(a b d e g h k l n o)

(define (schrap-3 lst)
  (define (iter-lijst lst result c)
    (if (null? lst)
      result
      (if (= c 3)
        (iter-lijst (cdr lst) result (+ c 1))
        (iter-lijst (cdr lst) (append result (list (car lst))) (+ c 1))
        )
      )
    )
  (iter-lijst lst '() 1)
  )

(schrap-3 '(1 2 3 4 5 6 7 8))
(schrap-3 '(a b c d e f g h j k l m n o p))

;(b) Veralgemeen je functie naar een functie die elke n-de element uit een lijst schrapt.

;> (schrap-n 4 '(1 2 3 4 5 6 7 8))
;(1 2 3 5 6 7)
;> (schrap-n 4 '(a b c d e f g h j k l m n o p))
;(a b c e f g j k l n o p)
