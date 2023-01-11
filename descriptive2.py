import random
startList = []
for i in range(0,100):
    startList.append(1000*random.random()+5000)

ilis = [3, 4, 7, 2, 1, 7]
def stats(slis):
    import statistics
    print("Mean: ", statistics.mean(slis))
    print("Median: ", statistics.median(slis))
    try:
        print("Mode: ", statistics.mode(slis))
    except statistics.StatisticsError as e:
        print("Mode error: ", e)
    print("Standard Deviation: ", statistics.stdev(slis))
    print("Variance: ", statistics.variance(slis))

def test():
    num = input("Enter num: ")
    print(type(num))
    try:
        num = float(num)
        print(num)
    except Exception as e:
        print("Exception:", e)
