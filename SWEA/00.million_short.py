test_case = int(input())
for i in range(1, test_case+1):
    N = int(input())
    profit = 0
    price_list = list(map(int, input().split()))
    ref_price = price_list[N-1]
    for j in range(N-1):
        if ref_price > price_list[N-j-2]:
            profit = profit + ref_price - price_list[N-j-2]
        else:
            ref_price = price_list[N-j-2]
    print(f"#{i} {profit}")

test_case = int(input())
for i in range(1, test_case+1):
    day_length=int(input())
    prices=list(map(int,input().split()))
    peak = 0
    sum1 = 0
    for i in range(len(prices)-1,-1,-1):
        if prices[i] > peak:
            peak = prices[i]
        ckpt = peak - prices[i]
        sum1 += ckpt
    print("#%i %i"%(test_case, sum1))