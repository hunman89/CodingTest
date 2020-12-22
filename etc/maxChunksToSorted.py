def maxChunksToSorted(arr):
    """
    :type arr: List[int]
    :rtype: int
    """
    if not arr: return 0
    n=len(arr)
    temp=arr[::]
    temp.sort()
    chunks=0
    cum_sum_temp=cum_sum_arr=0

    for i in range(n):
      cum_sum_temp+=temp[i]
      cum_sum_arr+=arr[i]
      if cum_sum_temp==cum_sum_arr:
        chunks+=1
    print(chunks)

test = [2, 1, 4, 3, 5]
maxChunksToSorted(test)