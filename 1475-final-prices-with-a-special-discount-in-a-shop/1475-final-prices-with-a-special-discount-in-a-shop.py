class Solution(object):
    def finalPrices(self, prices):
        st = []
        for i in range(len(prices)):
            while st and prices[i]<=prices[st[-1]]:
                prv = st.pop()
                prices[prv]=prices[prv]-prices[i]
            st.append(i)
        return prices
        