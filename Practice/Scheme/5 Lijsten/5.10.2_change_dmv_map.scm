;Vraag:
;Implementeer de procedure change-dmv-map, door middel van de ingebouwde procedure map.

;> (change-dmv-map 1 999 '(1 2 1 3 1 4 1 5 1))
;(999 2 999 3 999 4 999 5 999)
;> (change-dmv-map 1 999 '(2 3 4 5 6 7))
;(2 3 4 5 6 7)
;> (change-dmv-map 1 999 '(1))
;(999)
;> (change-dmv-map 1 999 '())
;()

;Oplossing:

(define (change-dmv-map getal1 getal2 lijst)
  (map
    (lambda (x)
      (if (= x getal1)
        getal2
        x
        )
      )
    lijst
    )
  )


;Test:
;(change-dmv-map 2 3 '())
;(change-dmv-map 2 3 '(2))
;(change-dmv-map 2 3 '(1 1 1))
;(change-dmv-map 2 3 '(2 0 2))
;(change-dmv-map 2 3 '(1 1 1))