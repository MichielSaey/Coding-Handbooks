;Vraag:
;Veronderstel dat je beschikt over procedures (double a) en (halve a) die hun argument
;verdubbelen respectievelijk halveren. Definieer een functie die hetzelfde is als de
;multiply uit vraag 3.2, maar die in logaritmische tijd haar resultaat berekent. Doe
;dit zowel op recursieve als op iteratieve wijze. Noem de recursieve versie
;(rec-fast-multiply a b). Noem de iteratieve wijze (iter-fast-multiply a b).

;Hint: Gebruik de analogie met de definitie van fast-expt uit Abelson&Sussman paragraaf 1.2.4.

;Notes:
;Wat gevraagd word is dat je de functie meerdere keer called voor een resultaat(f(x)= f(x) + f(x)),
;en op deze manier en om op deze manier een tree te maken van alle resultaten die horen berekend te
;worden. Ik snap hoe ik dit moet doen maar vermeenigvuldiging is daar zo een rare oefening voor. Is
;uitendelijk tog niet nodig? De fib oefening uit de les snap ik, maar dan vind ik het spijtig dat
;het geen oefening is.

;Requirments
(#%require racket/trace)

;Hulp functies
(define (double x) (+ x x))
(define (halve x) (/ x 2))

;Beschrijving logica
;a   b
;3 * 4 = 6 * 2
;      = 12 * 1
;      = 12 + (12 * 0)
;      = 12

;even getallen kan je delen door twee oneven niet dus daar word eerst nog een controlle op gedaan....

;Recursief
(define (rec-fast-multiply a b)
  (cond
    ((zero? b) 0)                                        ;als het nul is return 0
    ((even? b) (rec-fast-multiply (double a) (halve b))) ;3 * 4 -> 6 * 2
    (else (+ a (rec-fast-multiply a (- b 1))))           ;12 * 1 -> 12 + (12 * 0) of (a * b - 1)
    )
  )

;Iteratief fast
(define (iter-fast-multiply a b)
  (cond
    ((= b 0) 0)
    ((= b 1) a)
    (else (rec-fast-multiply (double a)(- b 1)))
    )
  )

(define (iter-fast-multiply a b)
  (define (iter a b acc) ;acc is acculmulater of gewoon som
    (cond
      ((zero? b) acc) ;als er b = 0 is er niet meer te vemeenigvuldigen dus returnen
      ((even? b) (iter (double a) (halve b) acc)) ; //
      (else (iter a (- b 1) (+ acc a))) ; //
      )
    )
  (iter a b 0)
  )

;Trace
;(trace iter-fast-multiply)
;(trace rec-fast-multiply)

;Testen
(rec-fast-multiply 10 0)
;0
(rec-fast-multiply 0 10)
;0
(rec-fast-multiply 10 20)
;200

(iter-fast-multiply 10 0)
;0
(iter-fast-multiply 0 10)
;0
(iter-fast-multiply 10 20)
;200