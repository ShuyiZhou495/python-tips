from string_search.kmp import kmp

if __name__ == '__main__':
    t = "abababadseddaababcsbabrsbabwabsbrbababw"
    pattern = "bababw"
    print(kmp(t, pattern))