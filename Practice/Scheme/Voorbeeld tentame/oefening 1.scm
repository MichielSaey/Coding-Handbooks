;Voorbeeld tentamen Oefening 1:

;Als je bij de bank 3% interest krijgt op je spaargeld is elke 100 euro die je inlegt een
;jaar later 100 + 3% van 100 = 103 euro geworden. Als je de interest niet opneemt maar
; gewoon herbelegt krijg je volgende opbrengsten:

;na 2 jaar 103      + 3% van 103      = 106.09
;na 3 jaar 106.09   + 3% van 106.09   = 109.2727
;na 4 jaar 109.2727 + 3% van 109.2727 = 112.550881
;...

;a)  Schrijf een functie (define (opbrengst x c n) ...) die uitrekent hoeveel geld er
;op je spaarrekening staat na n jaar als je x euro inlegt aan een interestvoet van c%.

;> (opbrengst 100 3 4)
;112.550881
;> (opbrengst 1000 0.1 20)
;1020.1911448605427

(#%require racket/trace)

;x = startbedrag
;c = intrest per jaar
;n = intrest over n aantal jaar
(define (opbrengst x c n)
  (if (zero? n)
    x
    (opbrengst (* x (+ 1.0 (/ c 100))) c (- n 1))
    )
  )

;Test
(trace opbrengst)

(opbrengst 100 3 4)
(opbrengst 1000 0.1 20)

;b)Levert je oplossing een recursief of een iteratief proces op? Leg uit waarom je dit antwoord geeft. Schrijf
;dan ook de andere versie.

;De hierboven beschreven oplossing is een iteratief poces. Er per stap van de herhaling een tussen resultaat
;word berekend voor die stap, voordat deze stap van de recursie word afgesloten.

;Hier zal ik het recursieve versie neer schrijven

(define (opbrengst-rec x c n)
  (if (zero? n)
    x
    (* (opbrengst-rec x c (- n 1)) (+ 1.0 (/ c 100)))
    )
  )

;Test
;(trace opbrengst-rec)

(opbrengst-rec 100 3 4)
(opbrengst-rec 1000 0.1 20)






