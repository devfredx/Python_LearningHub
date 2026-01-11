class Computer:
    def __init__(self, brand, cpu_name, ram_size):
        self.brand = brand
        self.inner_cpu = self.CPU(cpu_name)
        self.inner_ram = self.RAM(ram_size)

    def show(self):
        print(f"Computer: {self.brand}")
        self.inner_cpu.display()
        self.inner_ram.display()

    class CPU:
        def __init__(self, name):
            self.name = name
            self.cores = 8

        def display(self):
            print(f"CPU: {self.name} | Cores: {self.cores}")

    class RAM:
        def __init__(self, size):
            self.size = size

        def display(self):
            print(f"RAM: {self.size}GB")

laptop = Computer("ASUS", "Intel i7", 16)
laptop.show()

cpu_standalone = Computer.CPU("AMD Ryzen 9")
cpu_standalone.display()

class University:
    def __init__(self, name):
        self.name = name
        self.departments = []

    class Department:
        def __init__(self, dept_name):
            self.dept_name = dept_name

        def info(self):
            return f"Department: {self.dept_name}"

    def add_department(self, name):
        new_dept = self.Department(name)
        self.departments.append(new_dept)

uni = University("Istanbul Technical University")
uni.add_department("Software Engineering")
uni.add_department("Cyber Security")

for dept in uni.departments:
    print(dept.info())

class Outer:
    def __init__(self):
        self.value = "Outer Value"

    class Inner:
        def __init__(self, outer_instance):
            self.outer = outer_instance

        def access_outer(self):
            print(f"Accessing: {self.outer.value}")

out = Outer()
inn = Outer.Inner(out)
inn.access_outer()