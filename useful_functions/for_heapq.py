from heapq import heapify, heappush, heappop


if __name__ == '__main__':

    original = [3, 2, 4, 5, 7, 4, 9, 6]
    heapify(original)
    minimum = heappop(original)
    heappush(original, 8)