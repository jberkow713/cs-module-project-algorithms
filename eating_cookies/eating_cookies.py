'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n, cache):
    # can eat 1, 2, 3 cookies at one time,
    # count possible ways of eating n cookies
    # runtime O(3^n)
    if n < 0:
        return 0
    if n == 0:
        return 1
    # check cache, to see if it holds answer this branch is looking for
    elif n in cache:
        return cache[n]
    else: 
        # otherwise n not in cache
        # but once new answer computed, save in cache
        cache[n] = eating_cookies(n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache)
        return cache[n]
# so each additional n value is counted only once, so runtime is
# O(n)
#space complexity is probably O(n) since youre storing each value 1 time
# as well


# use cache so that when a branch is computer, it is stored in the cache,
# as a value for that branch, and so then that branch doesnt
# have to be recomputed

# what data structure should we use for a cache?
# save n value for branch, along with it's answer
# each branch has 3 values
# save n value as key, save associated answer as value in dict
# we will need to pass dictionary to each recursive call

    

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    #print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
