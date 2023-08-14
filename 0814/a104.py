try:
    while True:
        how_many_number = int(input())
        figures = list(map(int, input().split()))

        sorted_figures = sorted(figures)

        print(' '.join(map(str, sorted_figures)))
except EOFError:
    pass


# 氣泡排序法
try:
    while True:
        how_many_number = int(input())
        figures = list(map(int, input().split()))

        for j in range(how_many_number - 1):
            swapped = False
            for i in range(how_many_number - 1):
                if figures[i] > figures[i + 1]:
                    figures[i], figures[i + 1] = figures[i + 1], figures[i]
                    swapped = True
            if not swapped:
                break

        print(' '.join(map(str, figures)))
except EOFError:
    pass

# 快速排序法


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


try:
    while True:
        how_many_number = int(input())
        figures = list(map(int, input().split()))

        sorted_figures = quick_sort(figures)

        print(' '.join(map(str, sorted_figures)))
except EOFError:
    pass
