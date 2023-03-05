"""Program oblicza natężenie pola magnetycznego pomiędzy cewkami, w różnych odległościach od nich, licząc od środka
geometrycznego układu"""
import math


def read_current():
    file = open("current.txt", "r")
    current_file = file.readlines()
    current = [float(x.replace(",", ".")) / 1000 for x in current_file]
    return current  # I [A]


def read_frequency():
    file = open("frequencies.txt", "r")
    frequency_file = file.readlines()
    frequency = [float(x.replace(",", ".")) for x in frequency_file]
    return frequency  # f [Hz]


def read_distance():
    file = open("distance.txt", "r")
    distance_file = file.readlines()
    z = [float(x) / 100 for x in distance_file]
    return z


class HelmholtzCOils:
    def __init__(self, side_length, number_off_turns, distance_between_coils):
        self.current = None
        self.side_length = side_length
        self.number_of_turns = number_off_turns
        self.distance = distance_between_coils

    def magnetic_induction(self):
        B_list = []
        B_uT_list = []
        H_list = []
        H_dBuA_list = []
        ur = 1.00000037  # przenikalnosc powietrza
        u0 = 4 * math.pi * 10 ** -7
        i = read_current()[0]
        for z in self.distance:
            component1 = 2 * u0 * ur * self.number_of_turns * (self.side_length / 2) ** 2 * i / math.pi
            component2 = (self.side_length / 2) ** 2 + (z + self.distance / 2) ** 2
            component3 = (2 * (self.side_length / 2) ** 2 + (z + self.distance / 2) ** 2) ** (1 / 2)
            component4 = (self.side_length / 2) ** 2 + (z - self.distance / 2) ** 2
            component5 = (2 * (self.side_length / 2) ** 2 + (z - self.distance / 2) ** 2) ** (1 / 2)
            B = component1 * (1 / (component2 * component3) + 1 / (component4 * component5))  # [T]
            B_list.append(B)

            B_uT = B * 10 ** 6
            B_uT_list.append(B_uT)

            H = B / (u0 * ur)  # [A/m]
            H_list.append(H)

            H_dBuA = 20 * math.log10(H * 10 ** 6)  # [dBuA/m]
            H_dBuA_list.append(H_dBuA)
        return B_list, B_uT_list, H_list, H_dBuA_list

helmholtz_coil = HelmholtzCOils(1.04, 100, 0.566)

result = open("result.txt", "w")
for z in range(0, len(helmholtz_coil.distance)):
    result.write(str(helmholtz_coil.distance) + "\t" + str(helmholtz_coil.magnetic_induction()[3]))
