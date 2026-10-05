"""
DevOps Fundamentals - Session 04 - Exercise 5
Reset vs Revert Demo
Author: HoQuocKhai
Email: khaiho6040@gmail.com
"""

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    # Da sua dung phep nhan logic
    return a * b

def divide(a, b):
    # Experimental feature: Phep chia chua co xu ly ngoai le ZeroDivisionError
    return a / b

if __name__ == "__main__":
    print("5 + 3 =", add(5, 3))
    print("5 - 3 =", subtract(5, 3))
    print("5 * 3 =", multiply(5, 3))
    print("5 / 3 =", divide(5, 3))
