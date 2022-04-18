def main():

    def reduced_fraction(x, y):
        while x % y != 0:
            xx = x
            yy = y
            x = yy
            y = xx % yy
        return y

    class AlexFraction:
        def __init__(self, up, down):
            self.numa = up
            self.numi = down

        def __str__(self):
            return str(self.numa) + '/' + str(self.numi)

        def __add__(self, another_fraction):
            numarator = self.numa * another_fraction.numi + self.numi * another_fraction.numa
            numitor = self.numi + another_fraction.numi
            common = reduced_fraction(numarator, numitor)
            return AlexFraction(numarator // common, numitor // common)

    def inverse(numerator, denominator):
        return AlexFraction(denominator, numerator)

    class_call1 = AlexFraction(2, 2)
    class_call2 = AlexFraction(4, 4)
    the_sum = class_call1 + class_call2
    print(the_sum)

    str_sum = str(the_sum)
    list_sum = list(str_sum)
    print(inverse(list_sum[0], list_sum[2]))


if __name__ == '__main__':
    main()
