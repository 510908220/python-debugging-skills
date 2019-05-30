# -*- encoding: utf-8 -*-


def generate_list(number, number_list=[]):
    number_list.append(number)
    return number_list


def main():
    num = 1
    list1 = generate_list(num)
    print('list1:', list1)
    assert list1[0] == 1, 'bad list 1'
    num = 2
    list2 = generate_list(num)
    print('list2:', list2)
    assert list2[0] == 2, 'bad list 2'


if __name__ == "__main__":
    main()
