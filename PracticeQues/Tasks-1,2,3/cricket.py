import array as arr

def array_demo():
    runs = arr.array('i',[6, 12, 4, 0, 15, 8, 3, 20])
    print("Total runs:",sum(runs))
    print("Highest over",max(runs))
    print("Lowest over",min(runs))
    print("Average runs per over:",sum(runs)/len(runs))
    print("Maiden overs:",runs.count(0))
    print("Bytes used:",len(runs)*4)
array_demo()