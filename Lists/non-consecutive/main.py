def run(values: list) -> int:
    
    for i in range(len(values) - 1):
      
        if values[i + 1] != values[i] + 1:
            return values[i + 1]  
    return None 

# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
