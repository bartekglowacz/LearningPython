import math
import csv

def calculate_loop_antenna_coefficients(transmit_loop_diameter, receive_loop_diameter, transmit_loop_turns, receive_loop_turns, measurement_distance):
    wavelength = 299792458 # prędkość światła w m/s
    transmit_loop_area = math.pi * (transmit_loop_diameter/2)**2
    receive_loop_area = math.pi * (receive_loop_diameter/2)**2
    mutual_inductance = (wavelength**2 * transmit_loop_turns * receive_loop_turns * transmit_loop_area * receive_loop_area) / (4 * math.pi**2 * measurement_distance**3)
    transmit_loop_inductance = (wavelength**2 * transmit_loop_turns**2 * transmit_loop_area) / (4 * math.pi**2 * measurement_distance**3)
    receive_loop_inductance = (wavelength**2 * receive_loop_turns**2 * receive_loop_area) / (4 * math.pi**2 * measurement_distance**3)
    transmit_loop_coefficient = 10*math.log10(mutual_inductance / transmit_loop_inductance)
    receive_loop_coefficient = 10*math.log10(mutual_inductance / receive_loop_inductance)
    return transmit_loop_coefficient, receive_loop_coefficient

def save_to_csv(filename, data):
    with open(filename, mode='w') as file:
        writer = csv.writer(file)
        for row in data:
            writer.writerow(row)

if __name__ == '__main__':
    transmit_loop_diameter = float(input("Podaj średnicę anteny nadawczej: "))
    receive_loop_diameter = float(input("Podaj średnicę anteny odbiorczej: "))
    transmit_loop_turns = int(input("Podaj ilość zwojów w antenie nadawczej: "))
    receive_loop_turns = int(input("Podaj ilość zwojów w antenie odbiorczej: "))
    measurement_distance = float(input("Podaj odległość pomiarową między antenami: "))

    transmit_loop_coefficient, receive_loop_coefficient = calculate_loop_antenna_coefficients(transmit_loop_diameter, receive_loop_diameter, transmit_loop_turns, receive_loop_turns, measurement_distance)

    print("Współczynnik antenowy anteny nadawczej: {} dB(S/m)".format(transmit_loop_coefficient))
    print("Współczynnik antenowy anteny odbiorczej: {} dB(S/m)".format(receive_loop_coefficient))

    filename = input("Podaj nazwę pliku do zapisu: ")
    save_to_csv(filename, [['Antena', 'Współczynnik antenowy (dB(S/m))'], ['Antena nadawcza', transmit_loop_coefficient], ['Antena odbiorcza', receive_loop_coefficient]])
    print("Wynik został zapisany do pliku {}".format(filename))
