;Voorbeeld tentamen Oefening 2: Lijsten en Hogere Orde

;(a) Schrijf een functie (aantal-positief lst) die van een lijst van getallen berekent hoeveel positieve
;getallen er in voor komen.

;> (aantal-positief '(-1 1 2 -2))
;2
;> (aantal-positief '(0 -1))
;1

(define (aantal-positief lst)
  (define (lijst-iter lst c)
    (if (null? lst)
      c
      (if (zero? (modulo (car lst) 2))
        (lijst-iter (cdr lst) (+ c 1))
        (lijst-iter (cdr lst) c)
        )
      )
    )
  (lijst-iter lst 0)
  )

;Test
(aantal-positief '(-1 1 2 -2))
(aantal-positief '(0 -1))

;(b) Schrijf een veralgemening van je functie (aantal test lst) zodat ze van een lijst berekent hoeveel
;elementen aan een gegeven predicaat voldoen.

;> (aantal even? '(1 2 3))
;1
;> (aantal odd? '(1 2 3))
;2
;(c) Herschrijf (a) door je oplossing van (b) te gebruiken.

(define (aantal test lst)
  (define (lijst-iter lst c)
    (if (null? lst)
      c
      (if (test (car lst))
        (lijst-iter (cdr lst) (+ c 1))
        (lijst-iter (cdr lst) c)
        )
      )
    )
  (lijst-iter lst 0)
  )

;Test:
(aantal even? '(1 2 3))
(aantal odd? '(1 2 3))
