def decimal_to_binary(num):
    # Separate integer and fractional parts
    integer_part = int(num)
    fractional_part = num - integer_part
    
    # Convert integer part to binary
    binary_integer = bin(integer_part).replace("0b", "")
    
    # Convert fractional part to binary (up to 8 bits precision)
    binary_fraction = ""
    while fractional_part > 0 and len(binary_fraction) < 8:
        fractional_part *= 2
        bit = int(fractional_part)
        binary_fraction += str(bit)
        fractional_part -= bit

    # Combine both parts
    if binary_fraction:
        return f"{binary_integer}.{binary_fraction}"
    else:
        return binary_integer

# Example usage
decimal = float(input("Enter a decimal number: "))
print("Binary number is:", decimal_to_binary(decimal))
