import bit_simulation

#Pre-Change Simulation
number_of_errors = 0
bit_simulation_1 = bit_simulation.BitSimulation(0.001)
total_errors = 0
for _ in range(10):
    number_of_errors = 0
    for _ in range(10000):
        if not bit_simulation_1.get_true():
            number_of_errors += 1
    total_errors += number_of_errors
print("10000 runs pre-change: ", end="")
print(total_errors/10)

total_errors = 0
for _ in range(10):
    number_of_errors = 0
    for _ in range(20000):
        if not bit_simulation_1.get_true():
            number_of_errors += 1
    total_errors += number_of_errors
print("20000 runs pre-change: ", end="")
print(total_errors/10)

total_errors = 0
for _ in range(10):
    number_of_errors = 0
    for _ in range(30000):
        if not bit_simulation_1.get_true():
            number_of_errors += 1
    total_errors += number_of_errors
print("30000 runs pre-change: ", end="")
print(total_errors/10)

total_errors = 0
for _ in range(10):
    number_of_errors = 0
    for _ in range(40000):
        if not bit_simulation_1.get_true():
            number_of_errors += 1
    total_errors += number_of_errors
print("40000 runs pre-change: ", end="")
print(total_errors/10)

#Post-Change Simulation
total_errors = 0
for _ in range(10):
    number_of_errors = 0
    for _ in range(1000000):
        if bit_simulation_1.get_true():
            pass
        elif bit_simulation_1.get_false():
            number_of_errors += 1 
    total_errors += number_of_errors
print("1000000 runs post-change: ", end="")
print(total_errors/10)

total_errors = 0
for _ in range(10):
    number_of_errors = 0
    for _ in range(2000000):
        if bit_simulation_1.get_true():
            pass
        elif bit_simulation_1.get_false():
            number_of_errors += 1 
    total_errors += number_of_errors
print("2000000 runs post-change: ", end="")
print(total_errors/10)

total_errors = 0
for _ in range(10):
    number_of_errors = 0
    for _ in range(3000000):
        if bit_simulation_1.get_true():
            pass
        elif bit_simulation_1.get_false():
            number_of_errors += 1 
    total_errors += number_of_errors
print("3000000 runs post-change: ", end="")
print(total_errors/10)

total_errors = 0
for _ in range(10):
    number_of_errors = 0
    for _ in range(4000000):
        if bit_simulation_1.get_true():
            pass
        elif bit_simulation_1.get_false():
            number_of_errors += 1 
    total_errors += number_of_errors
print("4000000 runs post-change: ", end="")
print(total_errors/10)

total_errors = 0
for _ in range(10):
    number_of_errors = 0
    for _ in range(5000000):
        if bit_simulation_1.get_true():
            pass
        elif bit_simulation_1.get_false():
            number_of_errors += 1 
    total_errors += number_of_errors
print("5000000 runs post-change: ", end="")
print(total_errors/10)

total_errors = 0
for _ in range(10):
    number_of_errors = 0
    for _ in range(6000000):
        if bit_simulation_1.get_true():
            pass
        elif bit_simulation_1.get_false():
            number_of_errors += 1 
    total_errors += number_of_errors
print("6000000 runs post-change: ", end="")
print(total_errors/10)

total_errors = 0
for _ in range(10):
    number_of_errors = 0
    for _ in range(7000000):
        if bit_simulation_1.get_true():
            pass
        elif bit_simulation_1.get_false():
            number_of_errors += 1 
    total_errors += number_of_errors
print("7000000 runs post-change: ", end="")
print(total_errors/10)

total_errors = 0
for _ in range(10):
    number_of_errors = 0
    for _ in range(8000000):
        if bit_simulation_1.get_true():
            pass
        elif bit_simulation_1.get_false():
            number_of_errors += 1 
    total_errors += number_of_errors
print("8000000 runs post-change: ", end="")
print(total_errors/10)

total_errors = 0
for _ in range(10):
    number_of_errors = 0
    for _ in range(9000000):
        if bit_simulation_1.get_true():
            pass
        elif bit_simulation_1.get_false():
            number_of_errors += 1 
    total_errors += number_of_errors
print("9000000 runs post-change: ", end="")
print(total_errors/10)

total_errors = 0
for _ in range(10):
    number_of_errors = 0
    for _ in range(10000000):
        if bit_simulation_1.get_true():
            pass
        elif bit_simulation_1.get_false():
            number_of_errors += 1 
    total_errors += number_of_errors
print("10000000 runs post-change: ", end="")
print(total_errors/10)