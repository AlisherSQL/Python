Exercise 1: Threaded Prime Number Checker

Write a Python program that checks whether a given range of numbers contains prime numbers. Divide the range among
multiple threads to parallelize the prime checking process. Each thread should be responsible for checking a subset of the range, 
and the main program should print the list of prime numbers found.




import threading

def is_prime(n):
    if n < 2:
        return False
    if n ==2:
        return True
    if n % 2==0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True
    

def chek_primes_is_range(star, end, result_list):
    for num in range(star,end):
        if is_prime(num):
            result_list.append(num)

def thread_prime_checker(start,end,num_threads):
    thread_list=[]
    result=[]
    result_lock=threding_lock()

def thread_task(start_i,end_i):
    local_results=[]
    chek_primes_is_range(start_i,local_results)
    with results_lock:
        results.extend(local_results)

    step=(end,start)//num_threads
    for i in range(num_threads):
        thread_start=start+i*step
        thread_end=end if i== num_threads-1 else thread_start+step
        thread=threading.Thread(target=thread_task,args=(thread_start,thread_end))
        thread_list.append(thread)
        thread_start()

    for thread in thread_list:
        thread.join()

    return sorted(results)
if __name__=="__main__":
    start_range=1
    end_range=100
    threads=4

    primes = threaded_prime_checker(start_range, end_range, threads)
    print(f"{start_range} dan {end_range} gacha bo‘lgan tub sonlar:")
    print(primes)
