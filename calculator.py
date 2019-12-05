#spend per year
#Spend is amount they spend on x category per year 
# cash is the amount cashback they earn for category
#percent is to adjust for points earning card or percent earning cards
def auto(spent,cash, percent):
    sum= spent*cash*percent  
    return sum
def travel(spent, cash, percent): 
    sum = spent*cash*percent
    return sum
def online(spend,cash, percent):
    sum = spend*cash*percent
    return sum
def total(travel,auto,online):
    return travel+auto+online
#function for our credit cards to calculate the cashback
# parameters for amount spend in the category
def costco(auto,travel,online):
    a= auto(auto,4, .01)
    t= travel(travel,3, .01)
    o= online(online,1,.01)
    sum= a+t+o
    return sum
def uber(auto,travel,online):
    a= auto(auto,2,.01 )
    t= travel(travel,3,.01)
    o= online(online,2,.01)
    sum= a+t+o
    return sum
    
# testing
def main():
    au= auto(10,4, .01)
    tr= travel(100,3, .01)
    on= online(100,1, .01)
    t= total(au,tr,on)
    print(t)
    print(au)
    print(tr)
    print(on)

main()

