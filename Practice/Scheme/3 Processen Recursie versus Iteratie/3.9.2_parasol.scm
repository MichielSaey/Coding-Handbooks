;Vraag
;Schrijf een procedure (parasol n) (n is een geheel getal) die een parasolletje met gegeven hoogte op
;het scherm ‘tekent’. In het volgend voorbeeld heeft het driehoekje als hoogte 5 (de waarde van de
;parameter n) en als maximale breedte 9 (= (2 * n) - 1). De hoogte van het stokje is altijd 3. Enkele
;sterretjes en spaties kan je op het scherm printen door gebruik te maken van respectievelijk (display "*")
;en (display " "). Gebruik uiteraard de display-n procedure als je meerdere sterretjes of spaties op het
;scherm moet printen. Om een nieuwe lijn te beginnen gebruik je (newline).

;> (parasol 5)
;    *
;   ***
;  *****
; *******
;*********
;    *
;    *
;    *

;Notes:
;This used to be a christmas tree right?

; n = height of tree, constant
; c = countar, goes up by 2 each round
; w = weight, max with calculated with formula (2 * n) - 1
; s = spaces to print in fornt of the stars, calculated with formula (w - c)/2

;Helper
(define (display-n char n)
  (if (> n 0)
    (begin
      (display-n char (- n 1))
      (display char)
      )
    )
  )

;Oplossing:
(define (parasol n)
  (define (w) (- (* 2 n) 1))

  ;Prints a line of the tree
  (define (print-parasol-lijn ster spatie)
    (display-n " " spatie)
    (display-n "*" ster)
    (display "\n")
    )

  ;Calculates for each row of the parasol how many stars and spaces need to be printed
  (define (parasol-iter c)
    (if (<= c (w))
      (begin
        (print-parasol-lijn c (/ (- (w) c) 2))
        (parasol-iter (+ c 2))
        )
      )
    )

  ;prints the stick, wich is the same as the first row, repeated tree times (l = lenght of stick)
  (define (print-stick l)
    ;in the space function s is replaced with 1, this could be a way to select the with of the stick
    (define (s) (/ (- (w) 1) 2))
    (if (> l 0)
      (begin
        (print-parasol-lijn 1 (s))
        (print-stick (- l 1))
        )
      )
    )

  ;1 could be replaced if you want to chang the with of the first line of the parasol
  (parasol-iter 1)
  (print-stick 3)
  )

;Test
;(parasol 5)
