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
(opbrengst 100 3 4)
(opbrengst 1000 0.1 20)