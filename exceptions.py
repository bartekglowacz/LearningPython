try:
    file = open("plik.txt", "r")
    file.writelines("Szlachetne zdrowie, nikt się nie dowie\nJako smakujesz, aż się zepsujesz.")
except FileNotFoundError as e:
    print("File doesn't exist")
    print(e)
except Exception as e:
    print("Unknown error")
    print(e)