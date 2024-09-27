def run(n: int) -> int:
    
    acum = 1 
    
    for i in range(1, n + 1):  
        acum *= i**2 
        
    return acum  

# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor
    vendor.launch(run)
