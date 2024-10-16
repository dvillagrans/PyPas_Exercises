def run(stock: dict, merch: str, amount: int) -> bool:
    
    available = stock.get(merch, 0) >= amount


    return available

# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
