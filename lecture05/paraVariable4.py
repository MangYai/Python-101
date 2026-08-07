def display_info(**kwarge):
    for key, value in kwarge.items():
        print(f"{key}: {value}")
        
display_info(name="Alice", age=30, city="New York")
