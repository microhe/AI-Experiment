from IDAstar_24nums import IDAStar

import time


def main():
    pazzle_list = [[7, 5, 6, 3, 4, 1, 0, 2, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24], [5, 1, 2, 3, 4, 10, 6, 7, 8, 9, 0, 12, 18, 13, 14, 11, 15, 16, 23, 19, 20, 21, 22, 17, 24], [6, 5, 9, 3, 0, 10, 1, 2, 8, 4, 11, 16, 7, 13, 14, 20, 15, 12, 17, 18, 21, 22, 23, 24, 19], [11, 16, 1, 4, 9, 5, 7, 2, 8, 3, 10, 6, 12, 17, 14, 15, 0, 23, 13, 19, 20, 21, 18, 22, 24], [16, 1, 7, 2, 3, 6, 5, 13, 18, 4, 10, 11, 12, 23, 8, 15, 21, 14, 0, 9, 20, 22, 17, 24, 19], [6, 2, 8, 7, 4, 20, 1, 12, 3, 9, 0, 11, 22, 13, 14, 16, 17, 21, 18, 19, 5, 10, 15, 23, 24], [1, 10, 8, 2, 4, 21, 5, 9, 6, 14, 11, 7, 17, 19, 3, 15, 0, 22, 13, 16, 20, 12, 23, 18, 24], [5, 3, 7, 12, 4, 6, 1, 13, 14, 8, 2, 11, 0, 23, 19, 10, 20, 21, 18, 9, 17, 15, 16, 22, 24], [2, 3, 8, 4, 9, 6, 10, 5, 12, 14, 1, 11, 13, 21, 7, 15, 24, 20, 18, 19, 0, 16, 22, 17, 23], [8, 20, 16, 13, 0, 1, 11, 14, 2, 9, 21, 6, 5, 3, 4, 22, 15, 10, 18, 19, 17, 12, 7, 23, 24]]
    end_pazzle = []
    for i in range(25):
        end_pazzle.append(i)

    for pazzle in pazzle_list:
        # pazzle = [15, 5, 6, 2, 4, 16, 11, 8, 3, 9, 17, 21, 1, 12, 13, 10, 0, 7, 19, 14, 20, 18, 22, 23, 24]
        t0 = time.time()
        ida_start = IDAStar(pazzle, end_pazzle)
        print('IDAStar')
        print(ida_start.solve())
        t1 = time.time()
        print(t1 - t0)
        # break

    pass


if __name__ == '__main__':
    main()
