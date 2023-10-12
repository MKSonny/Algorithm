def reverse_str(str):
    str_ = []
    for ch in str:
        str_.append(ch)
    for _ in range(len(str_)):
        print(str_.pop(), end='')

my_str = input()
reverse_str(my_str)