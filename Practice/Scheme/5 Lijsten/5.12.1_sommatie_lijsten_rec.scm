;Vraag
;De procedure (sum-lists l1 l2) heeft als argumenten 2 lijsten met getallen, en geeft een lijst terug met de
;sommen van de overeenkomstige elementen van de input-lijsten. Merk op dat de twee input-lijsten niet dezelfde
;lengte hoeven te hebben. In dat geval worden de resterende elementen van de langste lijst gewoon overgenomen.

;Schrijf een recursieve versie, noem het (rec-sum-lists l1 l2).

;> (rec-sum-lists '(1 2 3 4) '(5 6 7))
;(6 8 10 4)
;> (rec-sum-lists '(1 2 3 4) '())
;(1 2 3 4)
;> (rec-sum-lists '() '(1 2 3))
;(1 2 3)
