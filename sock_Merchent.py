
def sock_merchant(arr):
    pairs = 0
    for i in set(arr):
        if arr.count(i) >= 2:
            pairs += arr.count(i) // 2

    return pairs

if __name__ == '__main__':
    sock_list = list(map(int, input().rstrip().split()))


    result = sock_merchant(sock_list)

    print(result)