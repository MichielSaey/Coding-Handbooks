// https://dodona.be/nl/courses/2906/series/31339/activities/1999594883
(define (square x) (* x x))
(define (fourth-* x) (* x x x x))
(define (fourth-square x) (square(square x)))

((fourth-* -2))