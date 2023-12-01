;Vraag
;In de driehoek van Pascal wordt een bepaalde eigenschap van de binomiaalcoëfficiënten heel duidelijk: elke
;coëfficiënt is de som van de twee bovenliggende coëfficiënten. Zo kan je hieronder op de onderste rij zien
;dat 21 de som is van de twee bovenliggende getallen, 6 en 15.
;Schrijf nu een procedure (binom n k) die recursief de binomiaalcoëfficiënt berekent, zonder gebruik te maken van faculteit.

;Hint: laat je inspireren door die andere wiskundige, Leonardo van Pisa, ook wel gekend als Fibonacci.

;> (binom 0 0)
;1
;> (binom 1 1)
;1
;> (binom 2 1)
;2
;> (binom 3 2)
;3
;> (binom 6 3)
;20

;Als K groter is dan n, geeft de procedure 0 terug.

;> (binom 0 5)
;0

;Processen
;Voeg commentaar toe aan je code die uitlegt wat voor process de binom procedure oplevert. Leg kort uit wat de
;eigenschappen van zulke processen zijn.

;Je kan commentaar aan je code toevoegen door een puntkomma voor de commentaar te zetten. Bijvoorbeeld:

;(define (binom n k)
;  ...)

; De binom procedure levert een ... process op. Dit process heeft als eigenschappen
; dat ...

;Notes
;Mijn python/oo getraind brein wou een multi-dim list data object aanmaken met een functie om op basis van de
;index het gepast element op te zoeken, maar ik heb ingezien dat dit hier warschijnlijk niet de bedoeling is.
;een gewoone recursieve functie bleek inderdaad een pak minder code te zijn. En uitendelijk is het gewoon een
;func die recursief 1'n opteld tot je aan de gevraagde index zit. (1 optellen all te way down)

(define (binom n k)
  (cond
    ((> k n) 0)
    ((zero? k) 1) ;catch alle plaatsen waar een 1 moet staan, en return 1
    ((zero? n) 1)
    (else (+ (binom (- n 1) (- k 1)) (binom (- n 1) k)))
    ;doe de som van twee andere binom calls (binom n-1 k-1) en (binom n-1 k)
    )
  )

;Test
(binom 0 0)
(binom 1 1)
(binom 2 1)
(binom 3 2)
(binom 6 3)
(binom 0 5)