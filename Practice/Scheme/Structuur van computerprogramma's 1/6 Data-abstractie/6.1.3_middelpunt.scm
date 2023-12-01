;Gebruik de operaties van dit ADT om een procedure (middelpunt segment) te schrijven die het middelpunt van een
;lijnstuk teruggeeft.

;Segment
(define (make-segment start einde)
  (cons start einde))

(define (start-punt segment)
  (car segment))

(define (end-punt segment)
  (cdr segment))

(define (middelpunt segment)
  (let ((x1 (x (start-punt segment)))
         (x2 (x (end-punt segment)))
         (y1 (y (start-punt segment)))
         (y2 (y (end-punt segment))))
    (make-punt (/ (+ x1 x2) 2) (/ (+ y1 y2) 2))
    ))

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
  (middelpunt segment))
;1. 2