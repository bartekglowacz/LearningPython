import math

# stałe
mu = 4 * math.pi * 1e-7  # permeability of free space
c = 299792458  # speed of light in vacuum

# funkcja do obliczania współczynnika antenowego w dB(S/m)
def antenna_factor(lam, R, N):
    return 10 * math.log10(4 * math.pi * R ** 2 / (N * lam ** 2))

# wczytywanie danych z pliku
filename = input("Podaj nazwę pliku z częstotliwościami pomiarowymi: ")
frequencies = []
with open(filename, 'r') as f:
    for line in f:
        frequencies.append(float(line.strip()))

# wczytywanie danych od użytkownika
diameter_tx = float(input("Podaj średnicę anteny nadawczej w metrach: "))
diameter_rx = float(input("Podaj średnicę anteny odbiorczej w metrach: "))
turns_tx = int(input("Podaj liczbę zwojów w antenie nadawczej: "))
turns_rx = int(input("Podaj liczbę zwojów w antenie odbiorczej: "))
distance = float(input("Podaj odległość pomiarową w metrach: "))

# obliczanie długości fali i promienia anteny
wavelengths = [c / freq for freq in frequencies]
radii_tx = [diameter_tx / 2 for freq in frequencies]
radii_rx = [diameter_rx / 2 for freq in frequencies]

# obliczanie współczynników antenowych i zapisywanie wyników do pliku
filename_output = input("Podaj nazwę pliku do zapisu wyników: ")
with open(filename_output, 'w') as f:
    f.write("Częstotliwość (MHz)\tWspółczynnik antenowy (dB(S/m))\n")
    for i in range(len(frequencies)):
        lam = wavelengths[i]
        R = (radii_tx[i] * radii_rx[i]) / distance
        N = turns_tx * turns_rx
        af = antenna_factor(lam, R, N)
        f.write("{:.2f}\t{:.2f}\n".format(frequencies[i], af))
