class Solution:
    def maximumWealth(self, accounts):
      customer_wealth = []
      for customer in accounts:        
        customer_wealth.append(sum(customer))
      return max(customer_wealth)  
      
# def maximumWealth(self, accounts):
#   return max(map(sum, accounts))
