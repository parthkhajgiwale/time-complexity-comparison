from bigO import BigO
from bigO import algorithm
from random import randint
algo=input("Enter algorithm name:")
algo1=input("Enter algorithm name: ")
def algo(array):
    n = len(array) 
    for i in range(n): 
        for j in range(0, n-i-1): 
            if array[j] > array[j+1]: 
                array[j], array[j+1] = array[j+1], array[j] 
def algo1(array):
    if len(array) <= 1:
        return array
    smaller, equal, larger = [], [], []
    pivot = array[randint(0, len(array) - 1)] 
    for x in array: 
        if x < pivot:
            smaller.append(x)
        elif x == pivot:
            equal.append(x)
        else:
            larger.append(x)
    return algo1(smaller) + equal + algo1(larger)
def TimeComplexity(functionname,functionname1):
    lib = BigO()
    cmplx = lib.test(functionname, "random")
    cmplx = lib.test(functionname, "sorted")
    cmplx = lib.test(functionname, "reversed")
    cmplx = lib.test(functionname1, "random")
    cmplx = lib.test(functionname1, "sorted")
    cmplx = lib.test(functionname1, "reversed")
    cmplx=lib.compare(algo,algo1,"random",5000)
    cmplx=lib.compare(algo,algo1,"all",5000)
  
TimeComplexity(algo,algo1)
