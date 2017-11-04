def parse(roman):
    """
    Transform roman digits to latin digits
    Bigger digit after the current one negates sign
    """

    literals = [
        ('I', 1),
        ('V', 5),
        ('X', 10),
        ('L', 50),
        ('C', 100),
        ('D', 500),
        ('M', 1000)
    ]

    def getDigit(c):
        for r, l in literals:
            if c == r: 
                return (1, l)
        raise "Invalid character " + c

    digits = [getDigit(c) for c in roman]
    for i in range(len(digits)-1):
        if digits[i][1] < digits[i+1][1]:
            digits[i] = (-1, digits[i][1])

    return sum([sign * l for sign, l in digits])