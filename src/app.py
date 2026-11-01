def welcome():
    return "Welcome to Git Collaboration Workflow"

def calculate_total(price, quantity):
    return price * quantity
    
    
    
def apply_discount(price, discount):
    return price - (price * discount / 100)

if __name__ == "__main__":
    print(welcome())
    print("Total:", calculate_total(100, 3))
    
    
