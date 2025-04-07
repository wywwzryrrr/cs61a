(define (ascending? s) 
    'YOUR-CODE-HERE
    (cond
        ((or (null? s) (null? (cdr s))) #t)
        ((<= (car s) (car (cdr s)))
            (ascending? (cdr s)))
        (else #f)
    )
)


(define (my-filter pred s) 
    'YOUR-CODE-HERE
    (cond
        ((null? s) '())
        ((pred (car s))
            (cons (car s) (my-filter pred (cdr s))))
        (else (my-filter pred (cdr s)))
    )
)


(define (interleave lst1 lst2) 
    'YOUR-CODE-HERE
    (cond
        ((null? lst1) lst2)
        ((null? lst2) lst1)
        (else (append (list (car lst1))
                      (list (car lst2))
                      (interleave (cdr lst1) (cdr lst2))))
    )
)


(define (no-repeats s)
  (if (null? s) 
      s
      (cons (car s) 
            (no-repeats (filter (lambda (x) (not (= (car s) x))) (cdr s))))))
