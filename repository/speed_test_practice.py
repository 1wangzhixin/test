def speeding_ticket(speed, is_birthday):
    # Adjust speed limits
    if is_birthday:
        speed -= 5

    # Determine ticket category
    if speed <= 60:
        return "No Ticket"
    elif 61 <= speed <= 80:
        return "Small Ticket"
    else:
        return "Big Ticket"

# Test cases
print(speeding_ticket(60, False))  # Expected output: "No Ticket"
print(speeding_ticket(75, False))  # Expected output: "Small Ticket"
print(speeding_ticket(85, False))  # Expected output: "Big Ticket"
print(speeding_ticket(65, True))   # Expected output: "No Ticket"
print(speeding_ticket(85, True))   # Expected output: "Small Ticket"
