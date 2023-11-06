;Vraag
;Schrijf een recursieve procedure (display-n x n) die twee parameters aanvaardt, een karakter en een
;positief geheel getal. Ze zal — gebruik makende van de standaard procedure display — het gegeven karakter
;zoveel maal afdrukken als de tweede parameter aangeeft.

;> (display-n "*" 4)
;****

;Notes:

;Oplossing:
(define (display-n char n)
  (if (> n 0)
    (begin
      (display-n char (- n 1))
      (display char)
      )
    )
  ;(display "\n")
  )

;Test
(display-n "*" 4)
(display " Expected: ****.\n")
(display-n "*" 0)
(display " Expected: .\n")
(display-n "*" 1)
(display " Expected: *.\n")
(display-n "*" 5)
(display " Expected: *****.\n")