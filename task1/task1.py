import sys

if __name__ == '__main__':

    arr = list(range(1, int(sys.argv[1]) + 1))
    len_check_arr = int(sys.argv[2])

    flag, path = arr[0] - 1, [arr[0]]
    len_arr = len(arr)
    next_el_ind = (flag + len_check_arr - 1) % len_arr

    while arr[next_el_ind] != arr[0]:

        flag = next_el_ind
        path.append(flag + 1)

        next_el_ind = (flag + len_check_arr - 1) % len_arr

    print(path)




