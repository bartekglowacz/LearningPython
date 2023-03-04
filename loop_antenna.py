import math
import matplotlib.pyplot as draw


def read_current():
    file = open("current.txt", "r")
    current = file.readlines()
    current = [float(x.replace(",", ".")) / 1000 for x in current]
    # print(current)
    return current


def read_frequencies():
    file = open("frequencies.txt", "r")
    frequencies_file = file.readlines()
    frequencies_file = [float(x.replace(",", ".")) for x in frequencies_file]
    # print(current)
    return frequencies_file  # w Hz


class HelmholtzCoil:
    def __init__(self, side_length, number_of_turns):
        self.frequencies = None
        self.side_length = side_length
        self.number_of_turns = number_of_turns
        self.current = read_current()

    def magnetic_induction(self):
        B_list = []
        B_uT_list = []
        H_list = []
        H_dBuA_list = []
        ur = 1.00000037  # przenikalnosc powietrza
        u0 = 4 * math.pi * 10 ** -7
        for i in self.current:
            B = 1.01796 * 2 * u0 * ur * self.number_of_turns * i / (math.pi * self.side_length / 2)  # [T]
            B_list.append(B)

            B_uT = B * 10 ** 6
            B_uT_list.append(B_uT)

            H = B / (u0 * ur)  # [A/m]
            H_list.append(H)

            H_dBuA = 20 * math.log10(H * 10 ** 6)  # [dBuA/m]
            H_dBuA_list.append(H_dBuA)
        return B_list, B_uT_list, H_list, H_dBuA_list


helmholtz_coil = HelmholtzCoil(1.04, 100)

induction_T = helmholtz_coil.magnetic_induction()[0]
induction_uT = helmholtz_coil.magnetic_induction()[1]
induction_A = helmholtz_coil.magnetic_induction()[2]
induction_dBuA = helmholtz_coil.magnetic_induction()[3]

frequencies = read_frequencies()
print(frequencies)
print(induction_dBuA)

results = open("result.txt", "w")
results.write("f [Hz]\tH [dBuA/m]\n")

for x in range(0, len(frequencies)):
    results.write(str(frequencies[x]).replace(".", ",") + "\t" + str(induction_dBuA[x]).replace(".", ",") + "\n")

draw.plot(frequencies, induction_dBuA)
draw.title("Rozkład pola magnetycznego pomiędzy cewkami Helmholtza")
draw.xlabel("f [Hz]")
draw.ylabel("A [dBuA/m]")
draw.xscale("log")
draw.grid(True, which='both')
draw.show()
