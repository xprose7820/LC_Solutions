class Solution:
    def fib(self, n):
        g_ratio = (1 + (5 ** .5)) / 2
        return round((g_ratio ** n) / (5 ** .5))