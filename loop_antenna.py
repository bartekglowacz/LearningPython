"""
Do obliczenia wartości pola magnetycznego pomiędzy kwadratowymi cewkami Helmholtza w ich centrum geometrycznym możemy użyć wzoru:
B = μ₀ * N * I / R,
gdzie:

B to pole magnetyczne,
μ₀ to przenikalność magnetyczna próżni (μ₀ = 4π * 10^-7 T*m/A),
N to ilość zwojów w każdej z cewek,
I to prąd płynący przez cewki (w Amperach),
R to promień cewek (w metrach).
W przypadku cewek kwadratowych, promień R to połowa długości boku kwadratu, czyli R = a/2, gdzie a to długość boku cewki.

Możemy więc zapisać wzór na pole magnetyczne w postaci:
B = μ₀ * N * I / (a/2)

Aby uwzględnić fakt, że cewki są kwadratowe, a nie okrągłe, musimy wprowadzić poprawkę kształtu cewki. W przypadku cewek Helmholtza, poprawka ta wynosi 1,0472, czyli:
B = μ₀ * N * I * 1,0472 / (a/2)

Warto zauważyć, że wzór ten dotyczy tylko pola magnetycznego w centrum geometrycznym cewek Helmholtza. W innych punktach wewnątrz cewek pole może się różnić.

Podsumowując, do obliczenia wartości pola magnetycznego pomiędzy kwadratowymi cewkami Helmholtza w ich centrum geometrycznym należy użyć wzoru:
B = μ₀ * N * I * 1,0472 / (a/2)
gdzie N to ilość zwojów w każdej z cewek, I to prąd płynący przez cewki (w Amperach), a a to długość boku cewki (w metrach).






Wzór na pole magnetyczne wewnątrz cewek Helmholtza, który podałem wcześniej, dotyczy pola magnetycznego w punkcie,
który znajduje się w środku geometrycznym obu cewek, czyli w punkcie, gdzie osie obu cewek się przecinają. W
przypadku, gdy chcemy obliczyć pole magnetyczne w innym punkcie, musimy skorzystać z bardziej złożonego wzoru,
który uwzględnia położenie punktu względem cewek.

Wzór ten ma postać:
B = μ₀ * N * I / (2 * R) * [(z + d/2) / sqrt(R² + (z + d/2)²) - (z - d/2) / sqrt(R² + (z - d/2)²)]
gdzie:

μ₀ to przenikalność magnetyczna próżni, N to liczba zwojów w każdej z cewek, I to prąd płynący przez cewki,
R to promień cewek (w przypadku cewek Helmholtza jest to połowa długości boku kwadratu), z to odległość punktu od
płaszczyzny cewek, d to odległość między cewkami (również połowa długości boku kwadratu). Warto zauważyć, że ten wzór
jest bardziej skomplikowany niż wzór dla pola magnetycznego w punkcie centralnym i wymaga podania dokładnego
położenia punktu względem cewek. W praktyce, przy pomiarach pola magnetycznego wewnątrz cewek Helmholtza, stosuje się
przede wszystkim pomiar w punkcie centralnym, ponieważ jest to najprostszy i najdokładniejszy sposób pomiaru pola
magnetycznego.
"""