#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    n = 0
    sum_n = 0

    for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
        if i % 2 == 0.0:
            n += 1
            sum_n += i
            print(i)
    print(f"Сумма этих чисел: {sum_n}\nИх количество: {n}")
