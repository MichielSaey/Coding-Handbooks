;Gebruik de operaties van dit ADT om een procedure (middelpunt segment) te schrijven die het middelpunt van een
;lijnstuk teruggeeft.

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