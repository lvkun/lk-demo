(define (dbg x) 
    (display x)
    (display "\n")
)

(dbg "1.1.2  Naming and the Environment")
(define size 2)

(dbg size)

(dbg (* 5 size) )

(define pi 3.14159)

(define radius 10)

(dbg
    (* pi
        (* radius radius)
    )
)

(define circumference
    (* 2 pi radius)
)

(dbg circumference)

(dbg "1.1.4  Compound Procedures")

(define (square x)
    ; (dbg "square")
    ; (dbg x)
    (* x x)
)

(dbg (square 21))
(dbg (square (+ 2 5)))
(dbg (square (square 3)))

(define (sum-of-squares x y)
    (dbg "sum-of-squares")
    (dbg x)
    (dbg y)
    (+ 
        (square x)
        (square y)
    )
)

(dbg (sum-of-squares 3 4))

(define (f a)
    (sum-of-squares
        (+ a 1)
        (* a 2)
    )
)

(dbg "1.1.5  The Substitution Model for Procedure Application")

(dbg (f 5))

(dbg "1.1.6  Conditional Expressions and Predicates")

(define (my-abs-1 x)
    (cond
        ((> x 0) x)
        ((= x 0) 0)
        ((< x 0) (- x))
    )
)

(define (my-abs-2 x)
    (cond 
        ((< x 0) (- x))
        (else x)
    )
)

(define (my-abs-3 x)
    (if (< x 0) 
        (- x)
        x
    )
)

(dbg (my-abs-1 5))
(dbg (my-abs-1 0))
(dbg (my-abs-1 -5))

(dbg (my-abs-2 5))
(dbg (my-abs-2 0))
(dbg (my-abs-2 -5))

(dbg (my-abs-3 5))
(dbg (my-abs-3 0))
(dbg (my-abs-3 -5))

(dbg "exercise 1.1")

(dbg 10)
(dbg (+ 5 3 4))
(dbg (- 9 1))
(dbg (/ 6 2))
(dbg 
    (+
        (* 2 4)
        (- 4 6)
    )
)

(define a 3)
(define b (+ a 1))

(dbg a)
(dbg b)

(dbg
    (+ a b (* a b))
)

(dbg (= a b))

(dbg
    (if
        (and
            (> b a)
            (< b (* a b))
        )
        b
        a
    )
)

(dbg 
    (cond 
        ((= a 4) 6)
        ((= b 4) (+ 6 7 a))
        (else 25)
    )
)

(dbg
    (+ 2
        (if
            (> b a)
            b
            a
        )
    )
)

(dbg
    (* 
        (cond
            ((> a b) a)
            ((< a b) b)
            (else -1)
        )
        (+ a 1)
    )
)

(dbg "exercise 1.2")

(dbg
    (/
        (+ 5 4
            (- 2
                (- 3
                    (+ 6
                        (/ 4 5)
                    )
                )
            )
        )
        (* 3
            (- 6 2)
            (- 2 7)
        )
    )
)

(dbg "exercise 1.3")

(define (max-sum x y z)
    (if (and (< x y) (< x z))
        (+ y z)
        (if (< y z)
            (+ x y)
            (+ x z)
        )
    )
)

(dbg
    (max-sum 1 2 3)
)

(dbg
    (max-sum 1 3 2)
)

(dbg "exercise 1.4")

(define (a-plus-abs-b a b)
    ((if (> b 0) + -) a b)
)

(dbg
    (a-plus-abs-b 3 -5)
)

(dbg "exercise 1.5")

(define (p) (p)
)

(define (test x y)
    (if (= x 0)
        0
        y
    )
)

; (dbg 
;     (test 0 (p))
; )

(dbg "1.1.7  Example: Square Roots by Newton's Method")

(define (good-enough? guess x)
    (<
        (my-abs-1
            (-
                (square guess)
                x
            )
        )
        0.001
    )
)

(define (improve guess x)
    (average guess (/ x guess))
)

(define (average x y)
    (/ (+ x y) 2)
)

(define (sqrt-iter guess x)
    (if
        (good-enough? guess x)
        guess
        (sqrt-iter
            (improve guess x)
            x
        )
    )
)

(define (sqrt x)
    (sqrt-iter 1.0 x)
)

(dbg (sqrt 9))

(dbg "exercise 1.6")

(define (new-if predicate then-clause else-clause)
    (cond (predicate then-clause)
        (else else-clause)
    )
)

; (define (sqrt-iter guess x)
;     (new-if
;         (good-enough? guess x)
;         guess
;         (sqrt-iter
;             (improve guess x)
;             x
;         )
;     )
; )
; (dbg (sqrt 100))

(dbg "exercise 1.7")
(dbg (sqrt (square 0.001)))
(dbg (sqrt (square 10000)))

(define (good-enough? guess x)
    (<
        (my-abs-1
            (/
                (-
                    (square guess)
                    x
                )
                x
            )
        )
        0000.1
    )
)

(dbg (sqrt (square 0.001)))
(dbg (sqrt (square 10000)))

(dbg "exercise 1.8")

(define (good-enough-3? guess x)
    (<
        (my-abs-1
            (/
                (-
                    (* guess guess guess)
                    x
                )
                x
            )
        )
        0000.1
    )
)

(define (improve3 guess x)
    (/ (+ (/ x (square guess))(* 2 guess)) 3)
)

(define (sqrt3-iter guess x)
    (if
        (good-enough-3? guess x)
        guess
        (sqrt3-iter
            (improve3 guess x)
            x
        )
    )
)

(define (sqrt3 x)
    (sqrt3-iter 1.0 x)
)

(dbg (sqrt3 8))

(dbg "1.1.8  Procedures as Black-Box Abstractions")

(define (sqrt x)
    
    (define (good-enough? guess)
        (< (abs (- (square guess) x)) 0.001)
    )

    (define (improve guess)
        (average guess (/ x guess))
    )

    (define (sqrt-iter guess)
        (if (good-enough? guess)
            guess
            (sqrt-iter (improve guess))
        )
    )

    (sqrt-iter 1.0)
)

(dbg (sqrt 100))

(dbg "1.2  Procedures and the Processes They Generate")

(dbg "1.2.1  Linear Recursion and Iteration")

(define (factorial n)
    (fact-iter 1 1 n)
)

(define (fact-iter product counter max-count)
    (if (> counter max-count)
        product
        (fact-iter 
            (* counter product)
            (+ counter 1)
            max-count
        )
    )
)
(dbg (factorial 6))

(dbg "exercise 1.9")

(define (dec x)
    (dbg "dec")
    (dbg x)
    (- x 1)
)
(define (inc x)
    (dbg "inc")
    (dbg x)
    (+ x 1)
)

(define (add-1 a b)
    (dbg (list "add-1" a b))
    (if (= a 0)
        b
        (inc (add-1 (dec a ) b))
    )
)

(dbg (add-1 4 5))

(define (add-2 a b)
    (dbg (list "add-2" a b))
    (if (= a 0)
        b
        (add-2 (dec a) (inc b))
    )
)

(dbg (add-2 4 5))

(dbg "exercise 1.10")

(define (A x y)
    (cond 
        ((= y 0) 0)
        ((= x 0) (* 2 y))
        ((= y 1) 2)
        (else
            (A
                (- x 1)
                (A x
                    (- y 1)
                )
            )
        )
    )
)

(dbg (A 1 10))
(dbg (A 2 4))
(dbg (A 3 3))

; f(n) -> 2*n
; g(n) -> 2^n
; h(n) -> 2^2^2^2...(n)

(dbg "1.2.2  Tree Recursion")

; (define (fib n)
;     (cond 
;         ((= n 0) 0)
;         ((= n 1) 1)
;         (else 
;             (+ 
;                 (fib (- n 1))
;                 (fib (- n 2))
;             )
;         )
;     )
; )

; (dbg (fib 10))

(define (fib n)
    (fib-iter 1 0 n)
)

(define (fib-iter a b count)
    (if (= count 0)
        b
        (fib-iter (+ a b) a (- count 1))
    )
)

(dbg (fib 10))

(dbg "Example: Counting change")

(define (count-change amount)
    (cc amount 5)
)

(define (cc amount kinds-of-coins)
    (cond 
        ((= amount 0) 1)
        ((or (< amount 0) (= kinds-of-coins 0)) 0)
        (else
            (+
                (cc 
                    amount
                    (- kinds-of-coins 1)
                )
                (cc
                    (- amount (first-denomination kinds-of-coins))
                    kinds-of-coins
                )
            )
        )
    )
)

(define (first-denomination kinds-of-coins)
    (cond
        ((= kinds-of-coins 1) 1)
        ((= kinds-of-coins 2) 5)
        ((= kinds-of-coins 3) 10)
        ((= kinds-of-coins 4) 25)
        ((= kinds-of-coins 5) 50)
    )
)

(dbg (count-change 100))