def digitSum(cardNumber):
    global length
    length = len(cardNumber)
    oddSum = 0
    evenSum = 0

    # if nothing gets entered, or the starting situation

    if (length == 0):

        return 0

    # when the length is more than 0, execute the following

    else:

        if (length % 2 == 0):
            last = int(cardNumber)
            evenSum += last

            return evenSum + digitSum(cardNumber[:-1])

        else:

            last = int(cardNumber[-1])
            last = 2 * last
            part_sum = last // 10 + last % 10
            oddSum += part_sum

            return oddSum + digitSum(cardNumber[:-1])


# This checks and reports if the card number is valid

def luhnAlgrorithm():
    cardNumber = input('Enter card number: ')

    total = digitSum(cardNumber)

    if total % 10 == 0:
        print('This is a valid credit card number')

    else:
        print('This is an invalid credit card number')


def main():
    luhnAlgrorithm()


main()
