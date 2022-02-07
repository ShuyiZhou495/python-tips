from string_search.kmp import kmp

if __name__ == '__main__':
    t = "abababadseddaababcsbabrsbabwabsbrbababw"
    pattern = "aabaab"
    print(kmp(t, pattern))