from __future__ import print_function
import string
import random

def generate_complex_password():
    sp = string.ascii_letters + string.digits + string.punctuation
    res = ''.join(random.sample(sp, 12))
    return res


def generate_normal_password():
    sp = string.ascii_letters + string.digits
    res = ''.join(random.sample(sp, 12))
    return res



def generate_simple_password():
    sp = string.ascii_letters
    res = ''.join(random.sample(sp, 12))
    return res


def main():
    #s = raw_input('please input complex/normal/simple')
    s = raw_input('please input complex/normal/simple: ')
    if s.lower() == 'complex':
        print(generate_complex_password())
    elif s.lower() == 'normal':
        print(generate_normal_password())
    elif s.lower() == 'simple':
        print(generate_simple_password())
    else:
        raise Exception('Error Input,Please Try Again!')

if __name__ == '__main__':
    main()