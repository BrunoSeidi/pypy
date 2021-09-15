def main():
    dollars = get_positive()
    cents = calculate_cents(dollars)
    coins = calculate_minimum(cents)
    
    print(coins)
    
    
def get_positive():
    while True:
        try:
            value = float(input("Change owed: "))
            if value > 0:
                return value
        except ValueError:
            continue
            
            
def calculate_cents(dollars):
    return round(dollars * 100)
    
    
def calculate_minimum(cents):
    coins = 0
    
    if (cents >= 25):
        coins += cents // 25
        cents = cents % 25
        
    if (cents >= 10):
        coins += cents // 10
        cents = cents % 10
        
    if (cents >= 5):
       coins += cents // 5
       cents = cents % 5
    
    coins += cents
        
    return coins


main()
