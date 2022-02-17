# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
#print('hello world')

#
#age = 5
#if age > 18:
    #print("обследование")
   # print('идите в кабинет')
#if age < 18:
   # print('поликлиника')

#

num = 1234567
count = 0
while num > 0:
    num = num // 10
    count += 1
    if count > 4:
       break
    print(count,num)