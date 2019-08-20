while True:

    from sympy import *
    from sympy.parsing.sympy_parser import parse_expr
    import math, os, time, turtle
    from turtle import *
    x = Symbol('x')
    y = Symbol('y')
    #only use xdo tool when need to press arrows, move mouse

    #button 1 = gpio7

    expr = ""
    gpio = 1
    gpio2 = 1
    gpio3 = 1

    #action area
    """if gpioread(15, High):
        action = "solve"
    """
    print("Options: solve, graphl, graphn, solvei, simplify,\nexpand, factor, and sys solve")
    action = input(str(("action: ")))

    if action == "solve":
        print("||||                  ||||")
        print("vvvv solving feature  vvvv")
        first = parse_expr(input("left side: "))
        second = parse_expr(input("right side: "))
        expr = solveset(Eq(first, second), x)
        print(first, "=", second)
        print('---------------------------')
        print("x =", expr)
        print(simplify(expr))

    if action == "graphl":
        print("||||                          ||||")
        print("vvvv linear graphing feature  vvvv")
        x = Symbol('x')
        inp = str(input("f(x) = "))
        print(inp)
        ls = -200
        x1 = 0
        x2 = 0
        y1=0
        y2=0
        t1 = Turtle()
        t2 = Turtle()
        t3 = Turtle()
        t4 = Turtle()

        for i in range(5):
            t3.fd(100)
            t3.rt(90)
            t3.fd(25)
            t3.bk(50)
            t3.fd(25)
            t3.lt(90)
            t4.rt(180)
            t4.fd(100)
            t4.rt(90)
            t4.fd(25)
            t4.bk(50)
            t4.fd(25)
            t4.rt(90)

        for i in range(abs(ls)*2):
            f1 = parse_expr(inp)
            y1 = f1.subs(x, x1)
            y1 = round(y1)
            t1.goto(x1, y1)

            f2 = parse_expr(inp)
            y2 = f2.subs(x, x2)
            y2 = round(y2)
            t2.goto(x2, y2)
            x1=x1+1
            x2=x2-1

    if action == "graphn":
        print("||||                             ||||")
        print("vvvv nonlinear graphing feature  vvvv")
        x = Symbol('x')
        inp = str(input("f(x) = "))
        scaleh = str((1/((1920/10)*.5)))
        scaleh = scaleh+str("*")
        inp = scaleh + inp
        print("The scale is: ", inp)
        ls = -200
        x1 = 0
        x2 = 0
        y1=0
        y2=0
        t1 = Turtle()
        t2 = Turtle()
        t3 = Turtle()
        t4 = Turtle()

        g = parse_expr(inp)
        yint = g.subs(x, 0)
        print("The y-intercept is: ", yint)
        left = 0
        right = parse_expr(inp)
        xint = solveset(Eq(left, right), x)
        print("The x-intercepts are: ", xint)


        """for i in range(5):
            t3.fd(100)
            t3.rt(90)
            t3.fd(25)
            t3.bk(50)
            t3.fd(25)
            t3.lt(90)
            t4.rt(180)
            t4.fd(100)
            t4.rt(90)
            t4.fd(25)
            t4.bk(50)
            t4.fd(25)
            t4.rt(90)"""

        for i in range(abs(ls)*2):
            f1 = parse_expr(inp)
            y1 = f1.subs(x, x1)
            y1 = round(y1)
            t1.goto(x1, y1)

            f2 = parse_expr(inp)
            y2 = f2.subs(x, x2)
            y2 = round(y2)
            t2.goto(x2, y2)
            x1=x1+1
            x2=x2-1

    if action == "solvei":
        print("||||                             ||||")
        print("vvvv inequality solving feature  vvvv")
        first = parse_expr(input("inequality: "))
        expr = solve(first)
        print(first)
        print('---------------------------')
        pprint(expr)

    if action == "simplify":
        print("||||                         ||||")
        print("vvvv simplification feature  vvvv")
        first = parse_expr(input("expression: "))
        expr = simplify(first)
        print(first)
        print('---------------------------')
        print(expr)
        pprint(expr)

    if action == "expand":
        print("||||                    ||||")
        print("vvvv expanding feature  vvvv")
        first = parse_expr(input("expression: "))
        expr = expand(first)
        print(first)
        print('---------------------------')
        print(expr)
        print('----------------------------')
        pprint(expr)

    if action == "factor":
        print("||||                    ||||")
        print("vvvv factoring feature  vvvv")
        first = parse_expr(input("expression: "))
        expr = factor(first)
        print(first)
        print('---------------------------')
        print(expr)
        print('---------------------------')
        pprint(expr)

    if action == "sys solve":
        print("||||                                      ||||")
        print("vvvv system of equations solving feature  vvvv")
        print("there must be a y in the left side of \nthe first equation")
        first = parse_expr(input("left side: "))
        second = parse_expr(input("right side: "))
        third = parse_expr(input("left side: "))
        fourth = parse_expr(input("right side: "))
        x1 = solveset(Eq(first, second), x)
        x2 = solveset(Eq(third, fourth), x)
        x3 = solveset(Eq(first, second), y)
        x4 = solveset(Eq(third, fourth), y)
        print(first, "=", second)
        print(third, "=", fourth)
        print('---------------------------')
        print("step 1: solve for y ", x1, "=", x2)
        y1 = solveset(Eq(x1, x2), y)
        print("step 2: solve for x ", x3, "=", x4)
        x5 = solveset(Eq(x3, x4), x)
        pprint(x5)
        pprint(y1)
        print("The solution is ", x5, ",", y1)


print("restarting")
os.system("ultimate math solver.py")
time.sleep(0.2)