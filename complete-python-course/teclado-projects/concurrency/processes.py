import time
from multiprocessing import Process


def ask_user():
    start = time.time()
    user_input = input("Enter your name: ")
    greeting = f"Hello, {user_input}"
    print(greeting)
    print(f"ask_user: {time.time() - start}")


def complex_calculation():
    start = time.time()
    print("Started calculating...")
    [x ** 2 for x in range(20000000)]
    print(f"complex_calculation: {time.time() - start}")


if __name__ == "__main__":
    start = time.time()
    ask_user()
    complex_calculation()

    print(f"Single thread total time: {time.time() - start}")

    process = Process(target=complex_calculation)
    process2 = Process(target=complex_calculation)

    process.start()
    process2.start()

    start = time.time()
    # ask_user()
    process.join()
    process2.join()

    print(f"Two process total time: {time.time() - start}")
