;Vraag:
;Onderstaande reeksontwikkeling heeft als som het getal e = 2,718281828...

;e = \frac{1}{0!} +\frac{1}{1!} +\frac{1}{2!} +\frac{1}{3!} + ...
;https://en.wikipedia.org/wiki/E_(mathematical_constant)

;We kunnen in Scheme een procedure (calc-e n) definiëren die het getal e benaderd door de som van de eerste
;n + 1 termen van de reeks te berekenen:

(define (factorial n)
  (if (zero? n)
    1
    (* n (factorial (- n 1)))))

(define (calc-e n)
  (if (= n 0)
    1
    (+ (/ 1 (factorial n))
      (calc-e (- n 1)))))

;Hierbij geeft (factorial n) het resultaat n! waarbij precies n vermenigvuldigingen worden gedaan (zie
;Abelson&Sussman blz. 32). Hoeveel vermenigvuldigingen neemt (calc-e n) dan in beslag? Verander de definitie van
;calc-e zodat je in totaal precies n vermenigvuldigingen doet.

;Hint: Verweef de definities van calc-e en factorial met elkaar en maak gebruik van een iteratief proces.

(exact->inexact (calc-e 10))
;2.7182818011463845

;Oplossing

;Ze vragen iteratief die hiervoor mag je er vanuit gaan dat je een hulp functie en een cumulatieve par gaat nodig
;hebben.

(define (calc-e-iter n)
  (define (iter ctr res fac-prev) ;ctr = counter(i in for loops), res = de comulatieve, fac-prev = de voorgaande
    (if (> ctr n) ;basicly do while ctr is <= n
      res ; als het gevraagde aantal is berekend return je het resultaat
      (let ((new-fac (* ctr fac-prev))) ;ctr vermenigvuldigen met fac-prev om de volgende fac te berekenen
        (iter (+ ctr 1) (+ res (/ 1 new-fac)) new-fac) ;n++ voor counter, res + 1/fac(n), 'save point' fac
        )
      )
    )
  (iter 1 1 1)
  )

(exact->inexact (calc-e-iter 10))
(exact->inexact (calc-e-iter 3))