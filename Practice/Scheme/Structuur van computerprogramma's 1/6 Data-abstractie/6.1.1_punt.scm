;Definieer een data-structuur om een (2-dimensionaal) punt voor te stellen. Schrijf hiertoe een constructor
;(make-punt x y) en de selectoren (x punt) en (y punt).

;> (define a (make-punt 2 11))
;> a
;(2 . 11)

;> (x a)
;2

;> (y a)
;11

;Definieer een data-structuur om een lijnstuk voor te stellen d.m.v. het start- en eindpunt van het lijnstuk.
;Schrijf hiertoe een constructor (make-segment start einde) en de selectoren (start-punt segment) en (end-punt
;segment).

;Segment
(define (make-segment start einde)
  (cons start einde))

(define (start-punt segment)
  (car segment))

(define (end-punt segment)
  (cdr segment))

;Punt
(define (make-punt x y)
  (cons x y))

(define (x point)
  (car point))

(define (y point)
  (cdr point))

;Test
(let ((segment
        (make-segment
          (make-punt 1 2)
          (make-punt 3 4))))
  (start-punt segment))
;1. 2

(let ((segment
        (make-segment
          (make-punt 1 2)
          (make-punt 3 4))))
  (end-punt segment))
;3. 4