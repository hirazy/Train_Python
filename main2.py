import re


if __name__ == '__main__':
    s = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
    lst = re.findall('\\S+@\\S+', s)
    print(lst)

    hello = "Hello"
    print(hello.center(10))