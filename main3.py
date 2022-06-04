class PartyAnimal:
    x = 0
    name = ""

    def __init__(self, name):
        self.name = name

    def party(self):
        self.x = self.x + 1


class FootballFan(PartyAnimal):
    points = 0

    def touchdown(self):
        self.points = self.points + 1
        self.party()

    def show(self):
        print("Value " + self.name)


def arithmetic_arranger(elements, isResult=None):
    len_space = 4
    ans = ""
    results = []
    lengths = []
    for i in range(0, len(elements)):
        s = str(elements[i])
        str_split = s.split()
        num1 = str_split[0]
        operator = str_split[1]
        num2 = str_split[2]
        max_len = max(len(num1), len(num2))
        lengths.append(max_len + 2)
        if isResult is not None:
            isPlus = True
            if operator == "-":
                isPlus = False

            if isPlus:
                results.append(str(int(num1) + int(num2)))
            else:
                results.append(str(int(num1) - int(num2)))

    # Print Num 1
    for i in range(0, len(elements)):
        s = str(elements[i])
        str_split = s.split()
        num1 = str_split[0]
        for j in range(0, lengths[i] - len(num1)):
            ans += " "
        ans += num1
        if i != len(elements) - 1:
            for k in range(0, len_space):
                ans += " "
    ans += '\n'
    # Print Num 2
    for i in range(0, len(elements)):
        s = str(elements[i])
        str_split = s.split()
        operator = str_split[1]
        num2 = str_split[2]
        ans += operator
        for j in range(0, lengths[i] - len(num2) - 1):
            ans += " "
        ans += num2
        if i != len(elements) - 1:
            for k in range(0, len_space):
                ans += " "
    ans += '\n'
    # Print line
    for i in range(0, len(elements)):
        for j in range(0, lengths[i]):
            ans += "-"

        if i != len(elements) - 1:
            for k in range(0, len_space):
                ans += " "

    # Print Result
    if isResult is not None:
        ans += '\n'
        for i in range(0, len(elements)):
            for j in range(0, lengths[i] - len(results[i])):
                ans += " "

            ans += results[i]
            if i != len(elements) - 1:
                for k in range(0, len_space):
                    ans += " "

    return ans


def add_time(start, duration):
    new_time = ""
    time = start.split(':')

    hour = int(time[0])
    minute = int(time[2])

    return new_time


if __name__ == '__main__':
    # print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))

    add_time("3:00 PM", "3:10")
