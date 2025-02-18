def run(time: str, offset: int) -> str:
    hours, minutes = map(int, time.split(':'))
    minutes += offset
    hours += minutes // 60  
    minutes = minutes % 60  

    hours = hours % 24

    final_time = f'{hours}:{minutes:02}' if hours < 10 else f'{hours:02}:{minutes:02}'

    return final_time

# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
