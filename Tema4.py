class AlexFraction:
    def __init__(self, up, down):
        self.numa = up
        self.numi = down

    def __str__(self):
        return str(self.numa) + '/' + str(self.numi)

    def __add__(self, another_fraction):
        numarator = self.numa * another_fraction.numi + self.numi * another_fraction.numa
        numitor = self.numi + another_fraction.numi
        return AlexFraction(numarator, numitor)


class_call1 = AlexFraction(2, 5)
class_call2 = AlexFraction(4, 6)
the_sum = class_call1 + class_call2
print(the_sum)

