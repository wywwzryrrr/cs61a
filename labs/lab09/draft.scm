(define (fact n)
    (if (= n 0) 1 (* n (fact (- n 1))))
)


(define (fact-exp n)
    (if (= n 0) 1 (list '* n (fact-exp (- n 1))))
)


(define (fib-exp n)
    (if (<= n 1) n (list '+ (fib-exp (- n 2)) (fib-exp (- n 1))))
)


(define (fib n)
    (if (<= n 1) n (+ (fib (- n 2)) (fib (- n 1))))
)


(begin 
    (define (f x total)
        (if (< (* x x) 50)
            (f (+ x 1) (+ total x))
            total)
    )
    (f 1 0)
)


(define (sum-while initial-x condition add-to-total update-x)
;       (sum-while 1)        '(< (* x x) 50) 'x     '(+ x 1)
    `(begin
        (define (f x total)
            (if, condition
                (f ,update-x (+ total ,add-to-total))
                total))
        (f ,initial-x 0)
    )
)


(define (sum-evens s)
    (if (null? s)
        0
    (if (even? (car s))
        (+ (car s) (sum-evens (cdr s)))
        (sum-evens (cdr s))
        )
    )
)


(define (compose f g)
    (lambda (x) (f (g x)))
)


(define (repeat f n)
    (if (= n 0)
        (lambda (x) x)
        (compose f (repeat f (- n 1)))
    )
)


(define-macro
    (for sym vals expr)
        (list 'map (list 'lambda (list sym) expr) vals)
)


(define fact (lambda (n)
    (if (zero? n) 1 (* n (fact (- n 1)))))
)


(define-macro (trace expr)
    (define operator (car expr))
`(begin
    (define original ,operator)
    (define ,operator (lambda (n)
                        (print (list (quote ,operator) n))
                        (original n))
    )
    (define result ,expr)
    (define ,operator original)
    result
 )
)