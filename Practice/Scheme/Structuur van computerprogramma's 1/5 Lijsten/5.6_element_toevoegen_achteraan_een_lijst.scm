;Vraag
;Defineer (zonder gebruik te maken van append) een procedure (add-to-end e l) die een nieuwe lijst teruggeeft
;met dezelfde elementen als de lijst l, maar met het object e aan het einde toegevoegd.

;Verwachte resultaat
;> (add-to-end 999 '(1 2 3 4 5))
;(1 2 3 4 5 999)
;> (add-to-end 999 '())
;(999)
;> (add-to-end 999 '(1))
;(1 999)

(define (add-to-end e l)
  (define (new-list e) (list e))

  (define (list-iter ol nl)
    (if (null? ol)
        nl
        (list-iter (cdr ol) (cons (car ol) nl))
        )
    )

  (list-iter (reverse l) (new-list e))
  )

;Test
(add-to-end 999 '(1 2 3 4 5))
(add-to-end 999 '())
(add-to-end 999 '(1))