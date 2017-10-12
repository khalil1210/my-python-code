def main():
    a = '123456788'
    while a < '999999999':
        a = str(int(a) + 1) # dont do this instead find next permuttion
        a = make9digitNumber(a)
        b = splitNumberToArray(a)
        if isMagicSquare(b):
            print('magic__'+a)
    print('end')

def isMagicSquare(a):
    setTemp = []
    for i in a:
        for j in i:
            if j in setTemp:
                return False
            else:
                setTemp.append(j)

    sum1 = int(a[0][0]) + int(a[0][1]) + int(a[0][2])
    sum2 = int(a[1][0]) + int(a[1][1]) + int(a[1][2])
    sum3 = int(a[2][0]) + int(a[2][1]) + int(a[2][2])
    if sum1 == sum2 & sum2 == sum3:
        sum4 = int(a[0][0]) + int(a[1][0]) + int(a[2][0])
        sum5 = int(a[0][1]) + int(a[1][1]) + int(a[2][1])
        sum6 = int(a[0][2]) + int(a[1][2]) + int(a[2][2])
        if sum4 == sum5 & sum5 == sum6 & sum6 == sum1:
            sum7 = int(a[0][0]) + int(a[1][1]) + int(a[2][2])
            sum8 = int(a[2][0]) + int(a[1][1]) + int(a[0][2])
            if sum7 == sum8 & sum8 == sum1:
                return True
            else:
                return False
        else:
            return False
    else:
        return False


def make9digitNumber(a):
    while len(a) < 9:
        a = '0' + str(a)
    return a


def splitNumberToArray(a):
    b = [[a[0], a[1], a[2]], [a[3], a[4], a[5]], [a[6], a[7], a[8]]]
    return b


main()
