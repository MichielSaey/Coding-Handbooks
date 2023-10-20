;In paragraaf 1.2.4 van Abelson & Sussman wordt de machtsverheffing gedefinieerd in termen van de vermenigvuldiging.
;Definieer nu op analoge wijze de vermenigvuldiging aan de hand van de optelling. Schrijf hiervoor een functie die
;twee positieve getallen vermenigvuldigt, en die als volgt werkt:

;a x 0 = 0
;a x 1 = (a x 0) + a
;a x 2 = (a x 1) + a

;3 * 2 = 3 + (3 * 1)
;      = 3 + (3 + (3 * 0))
;      = 3 + 3 + 0
;      = 6

;Doe dit zowel op recursieve als iteratieve wijze. Noem de recursieve versie (rec-multiply a b). Noem de iteratieve versie (iter-multiply a b).

(#%require racket/trace)

;Recursief
(define (rec-multiply a b)
  (if (zero? b)
    0
    (+ a (rec-multiply a (- b 1)))
    )
  )

;Iteratief
(define (iter-multiply a b)
  (cond
    ((= b 0) 0)
    ((= b 1) a)
    (else (iter-multiply (+ a a)(- b 1)))
    )
  )

;Iteratief alternatieve versie uit oplossing
(define (iter-multiply a b)

  (define (iter result counter)
    (if (zero? counter)
      result
      (iter (+ result a) (- counter 1))
      )
    )

    (iter 0 b)
  )

;3 * 2
;iter 0 2 = iter 3 1
;         = iter 6 0
;         = 6


;Je voegd een derde par toe voer het resultaat te bewaren. B blijft counter. In mijn oplossing pas in a
;aan. Niet echt het gevoeld dat de oplossing juister is. Mijn is leesbaarder, en is zonder helper of
;extra param. oplossing heeft ((= b 1) a) niet nodig.


(trace iter-multiply)

(rec-multiply 10 0)
(rec-multiply 0 10)
(rec-multiply 3 2)

(iter-multiply 10 0)
(iter-multiply 0 10)
(iter-multiply 3 2)