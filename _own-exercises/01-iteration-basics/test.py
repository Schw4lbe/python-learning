def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


# Get first 10 Fibonacci numbers
gen = fibonacci()
for _ in range(10):
    print(next(gen))


def echo_generator():
    while True:
        received = yield
        print("Received:", received)


gen = echo_generator()
next(gen)  # Prime the generator
gen.send("Hello")
gen.send("World")
