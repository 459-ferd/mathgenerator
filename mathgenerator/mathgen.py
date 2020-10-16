import random

genList = []

# || Generator class
class Generator:
    def __init__(self, title, id, generalProb, generalSol, func):
        self.title = title
        self.id = id
        self.generalProb = generalProb
        self.generalSol = generalSol
        self.func = func
        genList.append([id, title, self])

    def __str__(self):
        return str(self.id) + " " + self.title + " " + self.generalProb + " " + self.generalSol

    def __call__(self):
        return self.func()

# || Non-generator Functions
def genById(id):
    generator = genList[id][2]
    return(generator())

def getGenList():
    return(genList)

# || Generator Functions

def additionFunc(maxSum = 99, maxAddend = 50):
    a = random.randint(0, maxAddend)
    b = random.randint(0, min((maxSum-a), maxAddend)) #The highest value of b will be no higher than the maxsum minus the first number and no higher than the maxAddend as well
    c = a+b
    problem = str(a) + "+" + str(b) + "="
    solution = str(c)
    return problem, solution

def subtractionFunc(maxMinuend = 99, maxDiff = 99):
    a = random.randint(0, maxMinuend)
    b = random.randint(max(0, (a-maxDiff)), a)
    c = a-b
    problem = str(a) + "-" + str(b) + "="
    solution = str(c)
    return problem, solution

def multiplicationFunc(maxRes = 99, maxMulti = 99):
    a = random.randint(0, maxMulti)
    b = random.randint(0, min(int(maxMulti/a), maxRes))
    c = a*b
    problem = str(a) + "*" + str(b) + "="
    solution = str(c)
    return problem, solution

def divisionFunc(maxRes = 99, maxDivid = 99):
    a = random.randint(0, maxDivid)
    b = random.randint(0, min(maxRes, maxDivid))
    c = a/b
    problem = str(a) + "/" + str(b) + "="
    solution = str(c)
    return problem, solution

def binaryComplement1sFunc(maxDigits = 10):
    question = ''
    answer = ''
    for i in range(random.randint(1,maxDigits)):
        temp = str(random.randint(0, 1))
        question += temp
        answer += "0" if temp == "1" else "1"

    problem = question
    solution = answer
    return problem, solution

def moduloFunc(maxRes = 99, maxModulo= 99):
    a = random.randint(0, maxModulo)
    b = random.randint(0, min(maxRes, maxModulo))
    c = a%b
    problem = str(a) + "%" + str(b) + "="
    solution = str(c)
    return problem, solution

def squareRootFunc(minNo = 1, maxNo = 12):
    b = random.randint(minNo, maxNo)
    a = b*b
    problem = "sqrt(" + str(a) + ")="
    solution = str(b)
    return problem, solution

def powerRuleDifferentiationFunc(maxCoef = 10, maxExp = 10, maxTerms = 5):
    numTerms = random.randint(1, maxTerms)
    problem = ""
    solution = ""
    for i in range(numTerms):
        if i > 0:
            problem += " + "
            solution += " + "
        coefficient = random.randint(1, maxCoef)
        exponent = random.randint(1, maxExp)
        problem += str(coefficient) + "x^" + str(exponent)
        solution += str(coefficient * exponent) + "x^" + str(exponent - 1)
    return problem, solution

def squareFunc(maxSquareNum = 20):
    a = random.randint(1, maxSquareNum)
    b = a * a
    problem = str(a) + "^2" + "="
    solution = str(b)
    return problem, solution

def gcdFunc(maxVal=20):
    a = random.randint(1, maxVal)
    b = random.randint(1, maxVal)
    x, y = a, b
    while(y):
       x, y = y, x % y
    problem = f"GCD of {a} and {b} = "
    solution = str(x)
    return problem, solution

def lcmFunc(maxVal=20):
    a = random.randint(1, maxVal)
    b = random.randint(1, maxVal)
    x, y = a, b
    c = a * b
    while(y):
        x, y = y, x % y
    d = c // x
    problem = f"LCM of {a} and {b} = "
    solution = str(d)
    return problem, solution

def basicAlgebraFunc(maxVariable = 10):
    a = random.randint(1, maxVariable)
    b = random.randint(1, maxVariable)
    c = random.randint(b, maxVariable)
    # calculate gcd
    def calculate_gcd(x, y):
        while(y):
            x, y = y, x % y
        return x
    i = calculate_gcd((c - b), a)
    x = f"{(c - b)//i}/{a//i}"
    if (c - b == 0):
        x = "0"
    elif a == 1 or a == i :
        x = f"{c - b}"
    problem = f"{a}x + {b} = {c}"
    solution = x
    return problem, solution

def logFunc(maxBase=3, maxVal=8):
    a = random.randint(1, maxVal)
    b = random.randint(2, maxBase)
    c = pow(b,a)
    problem = "log"+str(b)+"("+str(c)+")"
    solution = str(a)
    return problem, solution

def divisionToIntFunc(maxA=25, maxB=25):
    a = random.randint(1,maxA)
    b = random.randint(1,maxB)
    divisor = a*b
    dividend=random.choice([a,b])
    problem = f"{divisor}/{dividend} = "
    solution=int(divisor/dividend)
    return problem,solution

def DecimalToBinaryFunc(max_dec=99):
    a = random.randint(1, max_dec)
    b = bin(a).replace("0b", "")
    problem = "Binary of "+str(a)+"="
    solution = str(b)
    return problem, solution

def BinaryToDecimalFunc(max_dig=10):
	problem=''
	for i in range(random.randint(1,max_dig)):
		temp = str(random.randint(0, 1))
		problem += temp

	solution=int(problem, 2);
	return problem, solution

def divideFractionsFunc(maxVal=10):
    a = random.randint(1, maxVal)
    b = random.randint(1, maxVal)
    while (a == b):
        b = random.randint(1, maxVal)
    c = random.randint(1, maxVal)
    d = random.randint(1, maxVal)
    while (c == d):
        d = random.randint(1, maxVal)
    def calculate_gcd(x, y):
        while(y):
            x, y = y, x % y
        return x
    tmp_n = a * d
    tmp_d = b * c
    gcd = calculate_gcd(tmp_n, tmp_d)
    x = f"{tmp_n//gcd}/{tmp_d//gcd}"
    if (tmp_d == 1 or tmp_d == gcd):
        x = f"{tmp_n//gcd}"
    # for equal numerator and denominators
    problem = f"({a}/{b})/({c}/{d})"
    solution = x
    return problem, solution

def multiplyIntToMatrix22(maxMatrixVal = 10, maxRes = 100):
    a = random.randint(0, maxMatrixVal)
    b = random.randint(0, maxMatrixVal)
    c = random.randint(0, maxMatrixVal)
    d = random.randint(0, maxMatrixVal)
    constant = random.randint(0, int(maxRes/max(a,b,c,d)))
    problem = f"{constant} * [[{a}, {b}], [{c}, {d}]] = "
    solution = f"[[{a*constant},{b*constant}],[{c*constant},{d*constant}]]"
    return problem, solution

def areaOfTriangleFunc(maxA=20, maxB=20, maxC=20):
	a = random.randint(1, maxA)
	b = random.randint(1, maxB)
	c = random.randint(1, maxC)
	s = (a+b+c)/2
	area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
	problem = "Area of triangle with side lengths: "+ str(a) +" "+ str(b) +" "+ str(c) + " = " 
	solution = area
	return problem, solution

def isTriangleValidFunc(maxSideLength = 50):
    sideA = random.randint(1, maxSideLength)
    sideB = random.randint(1, maxSideLength)
    sideC = random.randint(1, maxSideLength)
    sideSums = [sideA + sideB, sideB + sideC, sideC + sideA]
    sides = [sideC, sideA, sideB]
    exists = True & (sides[0] < sideSums[0]) & (sides[1] < sideSums[1]) & (sides[2] < sideSums[2]) 
    problem = f"Does triangle with sides {sideA}, {sideB} and {sideC} exist?"
    if exists:
        solution = "Yes"
        return problem, solution
    solution = "No"
    return problem, solution

def MidPointOfTwoPointFunc(maxValue=20):
	x1=random.randint(-20,maxValue)
	y1=random.randint(-20,maxValue)
	x2=random.randint(-20,maxValue)
	y2=random.randint(-20,maxValue)
	problem=f"({x1},{y1}),({x2},{y2})="
	solution=f"({(x1+x2)/2},{(y1+y2)/2})"
	return problem,solution

def factoringFunc(range_x1 = 10, range_x2 = 10):
  x1 = random.randint(-range_x1, range_x1)
  x2 = random.randint(-range_x2, range_x2)
  def intParser(z):
    if (z == 0):
      return ""
    if (z > 0):
      return "+" + str(z)
    if (z < 0):
      return "-" + str(abs(z))

  b = intParser(x1 + x2)
  c = intParser(x1 * x2)

  if (b == "+1"):
      b = "+"
      
  if (b == ""):
    problem = f"x^2{c}"
  else:
    problem = f"x^2{b}x{c}"

  x1 = intParser(x1)
  x2 = intParser(x2)
  solution = f"(x{x1})(x{x2})"
  return problem, solution
  
def thirdAngleOfTriangleFunc(maxAngle=89):
	angle1 = random.randint(1, maxAngle)
	angle2 = random.randint(1, maxAngle)
	angle3 = 180 - (angle1 + angle2)
	problem = f"Third angle of triangle with angles {angle1} and {angle2} = "
	solution = angle3
	return problem, solution

def systemOfEquationsFunc(range_x = 10, range_y = 10, coeff_mult_range=10):
    # Generate solution point first
    x = random.randint(-range_x, range_x)
    y = random.randint(-range_y, range_y)
    # Start from reduced echelon form (coeffs 1)
    c1 = [1, 0, x]
    c2 = [0, 1, y]

    def randNonZero():
        return random.choice([i for i in range(-coeff_mult_range, coeff_mult_range)
                              if i != 0])
    # Add random (non-zero) multiple of equations (rows) to each other
    c1_mult = randNonZero()
    c2_mult = randNonZero()
    new_c1 = [c1[i] + c1_mult * c2[i] for i in range(len(c1))]
    new_c2 = [c2[i] + c2_mult * c1[i] for i in range(len(c2))]

    # For extra randomness, now add random (non-zero) multiples of original rows
    # to themselves
    c1_mult = randNonZero()
    c2_mult = randNonZero()
    new_c1 = [new_c1[i] + c1_mult * c1[i] for i in range(len(c1))]
    new_c2 = [new_c2[i] + c2_mult * c2[i] for i in range(len(c2))]

    def coeffToFuncString(coeffs):
        # lots of edge cases for perfect formatting!
        x_sign = '-' if coeffs[0] < 0 else ''
        # No redundant 1s
        x_coeff = str(abs(coeffs[0])) if abs(coeffs[0]) != 1 else ''
        # If x coeff is 0, dont include x
        x_str = f'{x_sign}{x_coeff}x' if coeffs[0] != 0 else ''
        # if x isn't included and y is positive, dont include operator
        op = ' - ' if coeffs[1] < 0 else (' + ' if x_str != '' else '')
        # No redundant 1s
        y_coeff = abs(coeffs[1]) if abs(coeffs[1]) != 1 else ''
        # Don't include if 0, unless x is also 0 (probably never happens)
        y_str = f'{y_coeff}y' if coeffs[1] != 0 else ('' if x_str != '' else '0')
        return f'{x_str}{op}{y_str} = {coeffs[2]}'

    problem = f"{coeffToFuncString(new_c1)}, {coeffToFuncString(new_c2)}"
    solution = f"x = {x}, y = {y}"
    return problem, solution

    # Add random (non-zero) multiple of equations to each other

def distanceTwoPointsFunc(maxValXY = 20, minValXY=-20):
    point1X = random.randint(minValXY, maxValXY+1)
    point1Y = random.randint(minValXY, maxValXY+1)
    point2X = random.randint(minValXY, maxValXY+1)
    point2Y = random.randint(minValXY, maxValXY+1)
    distanceSq = (point1X - point2X) ** 2 + (point1Y - point2Y) ** 2
    solution = f"sqrt({distanceSq})"
    problem = f"Find the distance between ({point1X}, {point1Y}) and ({point2X}, {point2Y})"
    return problem, solution

def multiplyComplexNumbersFunc(minRealImaginaryNum = -20, maxRealImaginaryNum = 20):
    num1 = complex(random.randint(minRealImaginaryNum, maxRealImaginaryNum), random.randint(minRealImaginaryNum, maxRealImaginaryNum))
    num2 = complex(random.randint(minRealImaginaryNum, maxRealImaginaryNum), random.randint(minRealImaginaryNum, maxRealImaginaryNum))
    problem = f"{num1} * {num2} = "
    solution = num1 * num2
    return problem, solution

# || Class Instances

#Format is:
#<title> = Generator("<Title>", <id>, <generalized problem>, <generalized solution>, <function name>)
addition = Generator("Addition", 0, "a+b=", "c", additionFunc)
subtraction = Generator("Subtraction", 1, "a-b=", "c", subtractionFunc)
multiplication = Generator("Multiplication", 2, "a*b=", "c", multiplicationFunc)
division = Generator("Division", 3, "a/b=", "c", divisionFunc)
binaryComplement1s = Generator("Binary Complement 1s", 4, "1010=", "0101", binaryComplement1sFunc)
moduloDivision = Generator("Modulo Division", 5, "a%b=", "c", moduloFunc)
squareRoot = Generator("Square Root", 6, "sqrt(a)=", "b", squareRootFunc)
powerRuleDifferentiation = Generator("Power Rule Differentiation", 7, "nx^m=", "(n*m)x^(m-1)", powerRuleDifferentiationFunc)
square = Generator("Square", 8,"a^2", "b", squareFunc)
lcm = Generator("LCM (Least Common Multiple)", 9, "LCM of a and b = ", "c", lcmFunc)
gcd = Generator("GCD (Greatest Common Denominator)", 10, "GCD of a and b = ", "c", gcdFunc)
basicAlgebra = Generator("Basic Algebra", 11, "ax + b = c", "d", basicAlgebraFunc)
log = Generator("Logarithm", 12, "log2(8)", "3", logFunc)
intDivision = Generator("Easy Division", 13,"a/b=","c",divisionToIntFunc)
decimalToBinary = Generator("Decimal to Binary",14,"Binary of a=","b",DecimalToBinaryFunc)
binaryToDecimal = Generator("Binary to Decimal",15,"Decimal of a=","b",BinaryToDecimalFunc)
fractionDivision = Generator("Fraction Division", 16, "(a/b)/(c/d)=", "x/y", divideFractionsFunc)
intMatrix22Multiplication = Generator("Integer Multiplication with 2x2 Matrix", 17, "k * [[a,b],[c,d]]=", "[[k*a,k*b],[k*c,k*d]]", multiplyIntToMatrix22)
areaOfTriangle = Generator("Area of Triangle", 18, "Area of Triangle with side lengths a, b, c = ", "area", areaOfTriangleFunc)
doesTriangleExist = Generator("Triangle exists check", 19, "Does triangle with sides a, b and c exist?","Yes/No", isTriangleValidFunc)
midPointOfTwoPoint=Generator("Midpoint of the two point", 20,"((X1,Y1),(X2,Y2))=","((X1+X2)/2,(Y1+Y2)/2)",MidPointOfTwoPointFunc)
factoring = Generator("Subtraction", 21, "x^2+(x1+x2)+x1*x2", "(x-x1)(x-x2)", factoringFunc)
thirdAngleOfTriangle = Generator("Third Angle of Triangle", 22, "Third Angle of the triangle = ", "angle3", thirdAngleOfTriangleFunc)
systemOfEquations = Generator("Solve a System of Equations in R^2", 23, "2x + 5y = 13, -3x - 3y = -6", "x = -1, y = 3",
                              systemOfEquationsFunc)
distance2Point = Generator("Distance between 2 points", 24, "Find the distance between (x1,y1) and (x2,y2)","sqrt(distanceSquared)", distanceTwoPointsFunc)
ComplexNumMultiply = Generator("Multiplication of 2 complex numbers", 25, "(x + j) (y + j) = ", "xy + xj + yj -1", multiplyComplexNumbersFunc)
