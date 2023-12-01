;Vraag
;Het de onderstaande wiskundige functie kan je berekenen welk getal je op plaats n in de reeks kan vinden.
;golomb (n) = \left\lbrace\begin{array}{ll} 1  &  \mbox{als } n=1 \\ 1 + golomb (n - golomb (golomb (n - 1)))  &  \mbox{anders} \\\end{array}\right.

;Schrijf een functie (golomb n) die deze functie implementeert en zo het n-de getal van de golomb reeks kan berekenen. Je mag er steeds van uit gaan dat n >= 1.


;Verwachte resultaat
;> (golomb 4)
;3
;> (golomb 1)
;1
;> (golomb 30)
;10

;Oplossing
(define (golomb n)
  (cond
    ((= 1 n) 1)
    (else (+ 1 (golomb (- n (golomb (golomb (- n 1)))))))
    )
  )

;Test
(golomb 4)
(golomb 1)
(golomb 30)