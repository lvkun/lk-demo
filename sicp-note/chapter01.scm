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
    (dbg "square")
    (dbg x)
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