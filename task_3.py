import heapq


def min_cost_connect_cables(cables: list[int]) -> int:
    if len(cables) == 1:
        return 0

    heap = cables[:]
    heapq.heapify(heap)

    total_cost = 0

    while len(heap) > 1:
        first = heapq.heappop(heap)
        second = heapq.heappop(heap)

        cost = first + second
        total_cost += cost

        heapq.heappush(heap, cost)

    return total_cost


if __name__ == "__main__":
    cables = [1, 2, 3, 4, 5, 6]
    result = min_cost_connect_cables(cables)

    print(f"RESULT: {result}")
