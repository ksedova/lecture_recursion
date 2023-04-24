def recursive_nth_fibo(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return recursive_nth_fibo(num-1) + recursive_nth_fibo(num - 2)






def main():
   num = int(input("pocet clenu FP"))
   seg = [recursive_nth_fibo(num) for num in range(num + 1)]
   print(seg)


if __name__ == "__main__":
    main()
