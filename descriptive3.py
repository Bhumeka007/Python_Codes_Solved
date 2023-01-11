import random
random.seed(77)
temperature = []
for i in range(0,20):
    temperature.append(random.randint(20,95))

def temp(temps):
    pass

def tempra(temps):
    import statistics
    print(temps)
    print("Mean:",statistics.mean(temps))
    print("Median:",statistics.median(temps))
    print("Standard deviation:",statistics.stdev(temps))
    try:
        print("Mode:",statistics.mode(temps))
    except Exception as e:
        print("Mode error", e)
