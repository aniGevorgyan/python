# !usr/bin/python

import datetime


class Time:
    def __init__(self, h, m, s):
        self.hours = h
        self.minutes = m
        self.seconds = s

    def __add__(self, other):
        h = self.hours + other.hours
        m = self.minutes + other.minutes
        s = self.seconds + other.seconds
        m += s // 60
        h += m // 60
        h = h % 24
        m = m % 60
        s = s % 60
        return Time(h, m, s)

    def __sub__(self, other):
        h = self.hours - other.hours
        m = self.minutes - other.minutes
        s = self.seconds - other.seconds
        m += s // 60
        h += m // 60
        h = h % 24
        m = m % 60
        s = s % 60
        return Time(h, m, s)

    def __str__(self):
        if (self.hours > 12):
            return "{}:{}:{} {}".format(self.hours - 12, self.minutes, self.seconds, "PM")
        else:
            return "{}:{}:{} {}".format(self.hours, self.minutes, self.seconds, "AM")


def main():
    d = datetime.datetime.now()
    t_now = Time(d.hour, d.minute, d.second)
    print(t_now)
    t_new = Time(0, 0, 0)
    q1 = input("What do you want to do(add(a)/decrease(d))? ")
    if (q1 == "a"):
        q2 = input("What do you want to add(h/m,s)? ")
        if (q2 == "h"):
            t_new = Time((int(input("Enter hours here: "))), 0, 0)
        elif (q2 == "m"):
            t_new = Time(0, (int(input("Enter minutes here: "))), 0)
        elif (q2 == "s"):
            t_new = Time(0, 0, (int(input("Enter seconds here: "))))
        else:
            print("Invalid option")
        print(t_now + t_new)
    elif (q1 == "d"):
        q2 = input("What do you want to decrease(h/m,s)? ")
        if (q2 == "h"):
            t_new = Time((int(input("Enter hours here: "))), 0, 0)
        elif (q2 == "m"):
            t_new = Time(0, (int(input("Enter minutes here: "))), 0)
        elif (q2 == "s"):
            t_new = Time(0, 0, (int(input("Enter seconds here: "))))
        else:
            print("Invalid option")
        print(t_now - t_new)


if __name__ == "__main__":
    main()
