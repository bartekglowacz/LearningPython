import math


class HelmholtzCoil:
    def __init__(self, side_length, number_of_turns, current):
        self.frequencies = None
        self.side_length = side_length
        self.number_of_turns = number_of_turns
        self.current = current
        self.core_magnetic_permeability = 1

    def magnetic_induction(self):
        ur = 1.00000037  # przenikalnosc powietrza
        u0 = 4 * math.pi * 10 ** -7
        h = 0.566
        z = 0 # odległość od środka cewek
        B = (2*u0*self.number_of_turns*self.current*(self.side_length/2)/math.pi)*(1/(((self.side_length/2)**2+(z+h/2)**2)*(2*(self.side_length/2)**2+(z+h/2)**2)**(1/2))+1/(((self.side_length/2)**2+(z-h/2)**2)*(2*(self.side_length/2)**2+(z-h/2)**2)**(1/2)))# [T]
        H = B / (u0 * ur)  # [A/m]
        H_dBuA = 20 * math.log10(H * 10 ** 6)  # [dBuA/m]
        return [B, H, H_dBuA]


helmholtz_coil = HelmholtzCoil(1.04, 100, 1)
H_dbuA = helmholtz_coil.magnetic_induction()
print(H_dbuA)
