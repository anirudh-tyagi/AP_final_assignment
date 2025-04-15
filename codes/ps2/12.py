def fee(base_fee, roll):
    # Validate roll number length
    if len(roll) != 7:
        raise ValueError("Invalid roll number length. Must be 7 characters.")
    
    # Extract components
    dept = roll[0:2]
    year_str = roll[2:4]
    program = roll[4]
    roll_last_two = roll[5:7]

    # Validate department
    if dept not in ['CS', 'DS', 'EE', 'ME']:
        raise ValueError("Invalid department code.")

    # Validate year
    try:
        year_of_admission = int(year_str)
        full_year = 2000 + year_of_admission
    except:
        raise ValueError("Invalid year of admission.")

    if full_year > 2022:
        raise ValueError("Admission year cannot be after 2022.")

    # Validate program
    if program == '1':
        duration = 4  # B.Tech
    elif program == '2':
        duration = 2  # M.Tech
    else:
        raise ValueError("Invalid program code. Must be 1 or 2.")

    # Calculate how many years' fees should be counted till 2022-23
    max_years_paid = 2022 - full_year + 1
    actual_years = min(duration, max_years_paid)

    # Fee calculation
    total_fee = 0
    current_fee = base_fee
    for _ in range(actual_years):
        total_fee += current_fee
        current_fee = current_fee + (current_fee // 10)  # Increase by 10%

    return total_fee
print(fee(100000, 'CS20143'))