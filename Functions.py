import asyncio
import time
import schedule
import datetime

def start_timer(timer):
    """Starts timer"""
    task = asyncio.ensure_future(timer.start())
    task

def compare_time(fTimelist, sTime):
    fTime = float(fTimelist[0][0])
    """Returns True if difference in time is [10;infinity]"""
    difference = sTime - fTime
    difference = difference / 60
    if difference >= 10:
        return True
    else:
        return False

def bubbleSort(arr):
    n = len(arr)

    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j][1] > arr[j + 1][1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def get_dates_and_rates(request, currency):
    string = str(request)
    answer = [[] for i in range(5)]
    pos = 0
    skip = 0
    for i in range(len(string)):
        if i + skip < len(string):
            if string[i+skip] == "-":
                year = string[i+skip-4]+string[i+skip-3]+string[i+skip-2]+string[i+skip-1]
                month = string[i+skip+1]+string[i+skip+2]
                day = string[i+skip+4]+string[i+skip+5]
                answer[pos].append(int(year))
                answer[pos].append(int(month))
                answer[pos].append(int(day))
                answer[pos].append(request[year+"-"+month+"-"+day][currency])
                skip += 5
                pos += 1
        else:
            break
    answer = bubbleSort(answer)
    return answer