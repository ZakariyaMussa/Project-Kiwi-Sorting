from random import randint, random
from SelectionSort import Selectionsort
from time import time
 
averagecase= [randint(1,10000) for _ in range(1000)]
bestcase= sorted(averagecase)
worstcase= sorted(averagecase, reverse=True)
 
def test_BubbleWorst():
    start= time()
    assert Selectionsort(worstcase) == bestcase
    print(time()-start)
 
def test_BubbleBest():
    start= time()
    assert Selectionsort(bestcase) == bestcase
    print(time()-start)
 
def test_BubbleAvg():
    start= time()
    assert Selectionsort(averagecase) == bestcase
    print(time()-start)