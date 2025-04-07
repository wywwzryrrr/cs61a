(define (over-or-under num1 num2) 
  'YOUR-CODE-HERE
  (cond 
    ((< num1 num2) -1)
    ((> num1 num2) 1)
    (else 0)
  )
)


(define (over-or-under num1 num2) 
  'YOUR-CODE-HERE
  (if (< num1 num2) -1
    (if (= num1 num2) 0
      1))
)


(define (make-adder num) 
  'YOUR-CODE-HERE
  (lambda (inc) (+ inc num))
)


(define (composed f g) 
  'YOUR-CODE-HERE
  (lambda (x) (f (g x)))
)


(define (repeat f n) 
  'YOUR-CODE-HERE
  (if (= n 0)
    (lambda(x) x)
    (compose f (repeat f (- n 1)))
  )
)


(define (max a b)
  (if (> a b)
      a
      b
  )
)

(define (min a b)
  (if (> a b)
      b
      a
  )
)

(define (gcd a b) 
  'YOUR-CODE-HERE
  (= a (max a b))
  (= b (min a b))
  (if (= (remainder a b) 0)
    b
    (gcd b (remainder a b))
  )
)