# n = int(input("please enter the number of variables of your system of equations (2 or 3 or 4): "))


def n_2(err, eq1: list, eq2: list):
    err = float(err)

    x1 = 0.0
    x2 = 0.0
    old_x1 = 0.0
    old_x2 = 0.0

    v1 = [float(i) for i in eq1]
    v2 = [float(i) for i in eq2]

    # enter eq 1 details:
    # print(">>>please enter the details of equation number (1)<<<")
    # for i in range(2):
    #     x = 0.0
    #     # print("please enter the coefficient of variable no# ", end=" ")
    #     # print(i + 1, end='')
    #     # print(" ", end='')
    #
    #     x = coeff1[i]
    #     v1.append(x)
    #
    # eq1 = float(eq)
    # v1.append(eq1)

    # -------------------------------------
    # enter eq 2 details:
    # print(">>>please enter the details of equation number (2)<<<")
    # for i in range(2):
    #     x = 0.0
    #     print("please enter the coefficient of variable no# ", end=" ")
    #     print(i + 1, end='')
    #     print(" ", end='')
    #     x = float(input())
    #     v2.append(x)
    #
    # eq2 = float(input("please enter value of equation number (2): "))
    # v2.append(eq2)

    # ------------------------------------------

    # rearrangement of equations:
    if v1[1] >= (v1[0]):
        v1, v2 = v2, v1
    # --------------------------
    if v2[0] >= v2[1]:
        v2, v1 = v1, v2
    # --------------------------

    iterations = 0
    while True:
        old_x1 = x1
        old_x2 = x2

        x1 = (v1[2] - v1[1] * old_x2) / v1[0]
        x2 = (v2[2] - v2[0] * old_x1) / v2[1]

        iterations += 1

        if abs(x1 - old_x1) < err and abs(x2 - old_x2) < err:
            return f"value of x1: {x1}\nvalue of x2: {x2}\nnumber of iterations: {iterations}"


def n_3(err, eq1: list, eq2: list, eq3: list):
    err = float(err)

    x1 = 0.0
    x2 = 0.0
    x3 = 0.0
    old_x1 = 0.0
    old_x2 = 0.0
    old_x3 = 0.0

    v1 = [float(i) for i in eq1]
    v2 = [float(i) for i in eq2]
    v3 = [float(i) for i in eq3]

    # # enter eq 1 details:
    # print(">>>please enter the details of equation number (1)<<<")
    # for i in range(3):
    #     x = 0.0
    #     print("please enter the coefficient of variable no# ", end=" ")
    #     print(i + 1, end='')
    #     print(" ", end='')
    #     x = float(input())
    #     v1.append(x)
    #
    # eq1 = float(input("please enter value of equation number (1): "))
    # v1.append(eq1)
    #
    # # -------------------------------------
    # # enter eq 2 details:
    # print(">>>please enter the details of equation number (2)<<<")
    # for i in range(3):
    #     x = 0.0
    #     print("please enter the coefficient of variable no# ", end=" ")
    #     print(i + 1, end='')
    #     print(" ", end='')
    #     x = float(input())
    #     v2.append(x)
    #
    # eq2 = float(input("please enter value of equation number (2): "))
    # v2.append(eq2)
    #
    # # ------------------------------------------
    # # enter eq 3 details:
    # print(">>>please enter the details of equation number (3)<<<")
    # for i in range(3):
    #     x = 0.0
    #     print("please enter the coefficient of variable no# ", end=" ")
    #     print(i + 1, end='')
    #     print(" ", end='')
    #     x = float(input())
    #     v3.append(x)
    #
    # eq3 = float(input("please enter value of equation number (3): "))
    # v3.append(eq3)

    # rearrangement of equations:
    if v1[1] >= (v1[0] + v1[2]):
        v1, v2 = v2, v1
    elif v1[2] >= (v1[0] + v1[1]):
        v1, v3 = v3, v1
    # --------------------------
    if v2[0] >= v2[1] + v2[2]:
        v2, v1 = v1, v2
    elif v2[2] >= v2[0] + v2[1]:
        v2, v3 = v3, v2
    # --------------------------
    if v3[0] >= v3[1] + v3[2]:
        v3, v1 = v1, v3
    elif v3[1] >= v3[0] + v3[2]:
        v3, v2 = v2, v3

    iterations = 0
    while True:
        old_x1 = x1
        old_x2 = x2
        old_x3 = x3
        x1 = (v1[3] - v1[1] * old_x2 - v1[2] * old_x3) / v1[0]
        x2 = (v2[3] - v2[0] * old_x1 - v2[2] * old_x3) / v2[1]
        x3 = (v3[3] - v3[0] * old_x1 - v3[1] * old_x2) / v3[2]
        iterations += 1

        if abs(x1 - old_x1) < err and abs(x2 - old_x2) < err and abs(x3 - old_x3) < err:
            return f'value of x1: {x1}\nvalue of x2: {x2}\nvalue of x3: {x3}\nnumber of iterations: {iterations}'


def n_4(err, eq1: list, eq2: list, eq3: list, eq4: list):
    err = float(err)

    x1 = 0.0
    x2 = 0.0
    x3 = 0.0
    x4 = 0.0
    old_x1 = 0.0
    old_x2 = 0.0
    old_x3 = 0.0
    old_x4 = 0.0

    v1 = [float(i) for i in eq1]
    v2 = [float(i) for i in eq2]
    v3 = [float(i) for i in eq3]
    v4 = [float(i) for i in eq4]
    #
    # # enter eq 1 details:
    # print(">>>please enter the details of equation number (1)<<<")
    # for i in range(4):
    #     x = 0.0
    #     print("please enter the coefficient of variable no# ", end=" ")
    #     print(i + 1, end='')
    #     print(" ", end='')
    #     x = float(input())
    #     v1.append(x)
    #
    # eq1 = float(input("please enter value of equation number (1): "))
    # v1.append(eq1)
    #
    # # -------------------------------------
    # # enter eq 2 details:
    # print(">>>please enter the details of equation number (2)<<<")
    # for i in range(4):
    #     x = 0.0
    #     print("please enter the coefficient of variable no# ", end=" ")
    #     print(i + 1, end='')
    #     print(" ", end='')
    #     x = float(input())
    #     v2.append(x)
    #
    # eq2 = float(input("please enter value of equation number (2): "))
    # v2.append(eq2)
    #
    # # ------------------------------------------
    # # enter eq 3 details:
    # print(">>>please enter the details of equation number (3)<<<")
    # for i in range(4):
    #     x = 0.0
    #     print("please enter the coefficient of variable no# ", end=" ")
    #     print(i + 1, end='')
    #     print(" ", end='')
    #     x = float(input())
    #     v3.append(x)
    #
    # eq3 = float(input("please enter value of equation number (3): "))
    # v3.append(eq3)
    #
    # # ------------------------------------------
    # # enter eq 4 details:
    # print(">>>please enter the details of equation number (4)<<<")
    # for i in range(4):
    #     x = 0.0
    #     print("please enter the coefficient of variable no# ", end=" ")
    #     print(i + 1, end='')
    #     print(" ", end='')
    #     x = float(input())
    #     v4.append(x)
    #
    # eq4 = float(input("please enter value of equation number (4): "))
    # v4.append(eq4)

    # rearrangement of equations:
    if v1[1] >= (v1[0] + v1[2] + v1[3]):
        v1, v2 = v2, v1
    elif v1[2] >= (v1[0] + v1[1] + v1[3]):
        v1, v3 = v3, v1
    elif v1[3] >= (v1[0] + v1[1] + v1[2]):
        v1, v4 = v4, v1
        # --------------------------
    if v2[0] >= v2[1] + v2[2] + v2[3]:
        v2, v1 = v1, v2
    elif v2[2] >= v2[0] + v2[1] + v2[3]:
        v2, v3 = v3, v2
    elif v2[3] >= v2[0] + v2[1] + v2[2]:
        v2, v4 = v4, v2
        # --------------------------
    if v3[0] >= v3[1] + v3[2] + v3[3]:
        v3, v1 = v1, v3
    elif v3[1] >= v3[0] + v3[2] + v3[3]:
        v3, v2 = v2, v3
    elif v3[3] >= v3[0] + v3[1] + v3[2]:
        v3, v4 = v4, v3
    # ------------------------------
    if v4[0] >= v4[1] + v4[2] + v4[3]:
        v4, v1 = v1, v4
    elif v4[1] >= v4[0] + v4[2] + v4[4]:
        v4, v2 = v2, v4
    elif v4[2] >= v4[0] + v4[1] + v4[3]:
        v4, v3 = v3, v4

    iterations = 0
    while True:
        old_x1 = x1
        old_x2 = x2
        old_x3 = x3
        old_x4 = x4
        x1 = (v1[4] - v1[1] * old_x2 - v1[2] * old_x3 - v1[3] * old_x4) / v1[0]
        x2 = (v2[4] - v2[0] * old_x1 - v2[2] * old_x3 - v2[3] * old_x4) / v2[1]
        x3 = (v3[4] - v3[0] * old_x1 - v3[1] * old_x2 - v3[3] * old_x4) / v3[2]
        x4 = (v4[4] - v4[0] * old_x1 - v4[1] * old_x2 - v4[2] * old_x3) / v4[3]

        iterations += 1

        if abs(x1 - old_x1) < err and abs(x2 - old_x2) < err and abs(x3 - old_x3) < err:
            return f"value of x1: {round(x1)}\nvalue of x2: {x2}\nvalue of x3: {x3}\nvalue of x4: {x4}\nnumber of iterations: {iterations}"

# if n == 2:
#     n_2()
#
# elif n == 3:
#     n_3()
#
# elif n == 4:
#     n_4()
