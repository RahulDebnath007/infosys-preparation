class Solution(object):
    def change(self, amount, coins):
        

        C = [0] * (amount + 1)
        C[0] = 1
        for coin in coins:
            for a in xrange(coin, amount + 1):
                C[a] += C[a - coin]
        return C[amount]    