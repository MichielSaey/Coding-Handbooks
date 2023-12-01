;Vraag
;Schrijf een procedure (display-as-binary n), die een positief geheel getal n neemt, en dit in binaire vorm afdrukt.
;De meest rechtse bit is 1 als het getal oneven is, 0 als het getal even is. Voor de tweede bit van rechts deel je
;het getal door 2 (met de functie (quotient n1 n2) die het geheel equivalent is van (/ n1 n2), en je doet dezelfde
;test. Voor de derde bit van rechts deel je het vorige quotiënt door 2 enz. ... Je mag een recursief proces
;genereren. Gebruik (display "0") en (display "1") om de cijfers 0 en 1 af te drukken. Let op dat je het getal niet
;omgekeerd afdrukt. Enkele correcte voorbeelden zijn:

;(display-as-binary 8)
;1000
;(display-as-binary 5)
;101
;(display-as-binary 0)
;0

;10 / 2 = 5 + 0
;5 / 2 = 2 + 1
;2 / 2 = 1 + 0
;1 / 2 = 0 + 1

;> (quotient 10 2)
;5

;(modulo 10 2)
;0

;8 4 2 1
;1 0 1 0

;Notes:
;De output moet omgedraaid worden. lijst of string met een append at front zou werken. Uit zoeken hoe we dit in scheme doen.
;Eerst de volgende iter starten en dan pas printen

;Oplossing:
(define (display-as-binary n)
  (define (binary-iter n)
    ;Calculate quotient, if it is not zero pass it on to the next step
    (let ((result (quotient n 2)))
      (if (not (zero? result))
        (binary-iter result)
        )
      )
    ;Calculate the remainder, and print it.
    (display (modulo n 2))
    )
  ;Call the iter function
  (binary-iter n)
  ;After all is printed end the line
  ;(display "\n")
  )

;Test
(display-as-binary 8)
(display "Expected: 1000.\n")
(display-as-binary 5)
(display "Expected: 101.\n")
(display-as-binary 0)
(display "Expected: 0.\n")