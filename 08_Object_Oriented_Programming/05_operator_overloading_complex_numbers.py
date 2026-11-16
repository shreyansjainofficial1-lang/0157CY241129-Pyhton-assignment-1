class Complex:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        return Complex(
            self.real + other.real,
            self.imaginary + other.imaginary
        )

    def __str__(self):
        sign = "+" if self.imaginary >= 0 else "-"
        return f"{self.real} {sign} {abs(self.imaginary)}i"

first = Complex(
    float(input("First number - real part: ")),
    float(input("First number - imaginary part: "))
)
second = Complex(
    float(input("Second number - real part: ")),
    float(input("Second number - imaginary part: "))
)

print("Sum:", first + second)
