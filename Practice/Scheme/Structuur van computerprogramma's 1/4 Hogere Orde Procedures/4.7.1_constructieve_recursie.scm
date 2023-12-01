;Vraag
;Definieer de procedure (product factor a next b), naar analogie met de hogere-orde procedure sum uit vorige
;oefening. Maak hierbij gebruik van constructieve recursie.

(define (sum term a next b)
  (if (> a b)
    0
    (+ (term a) (sum term (next a) next b))))

;Dit is een uitwerking van een sigma notatie, of een sommatie van een series.
;term is de functie voor het berekenen van de huidige teller <- is een procedure
;a en b zijn onder en boven grens van de sommasie
;next neemt de huidege teller, en geeft devolgende teller terug <- is een procedure

;Deze procedure vermenig vuldicht alle factoren met elkaar, dit is waarom term word vervangen door factor.
;factor en next worden gedefineerd wanneer de procedure word aangeroepen
(define (product factor a next b)
  (if (> a b)
    1
    (* (factor a) (product factor (next a) next b))
    )
  )

;Test
(product (lambda (a) a) 2 (lambda (a) (+ a 2)) 6)]
; 2 * 4 * 6 = 48
(product (lambda (a) a) 1 (lambda (a) (+ a 2)) 6)
; 1 * 3 * 5 = 15