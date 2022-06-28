'''
주식 가격이 주어질 때 어느 시점에 사서 파는 것이 최대의 이익인지 이익의 크기를 출력

입력:[7,1,5,3,6,4]
출력:5
'''

review

# def maxProfit(prices):
#     max_price = 0
#
#     for i, price in enumerate(prices):
#         for j in range(i, len(prices)):
#             max_price = max(prices[j] - price, max_price)
#     return max_price
#
# price = [7,1,5,3,6,4]
# print(maxProfit(price))

# def maxProfit(prices):
#     profit = 0
#     min_price = prices[0]
#     # 최솟값과 최댓값을 계속 갱신
#     for price in prices:
#         min_price = min(min_price, price)
#         profit = max(profit, price - min_price)
#     return profit
#
# prices = [7,1,5,3,6,4]
# print(maxProfit(prices))