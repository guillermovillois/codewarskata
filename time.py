def past(h, m, s):
    # Good Luck!
    print(((h*60+m)*60+s)*1000)
    return ((h*60+m)*60+s)*1000


# Clock shows 'h' hours, 'm' minutes and 's' seconds after midnight.
    # Your task is to make 'Past' function which returns time converted to milliseconds.
    # Example:
past(0, 1, 1) == 61000
# Input constraints: 0 <= h <= 23, 0 <= m <= 59, 0 <= s <= 59
print(past(0, 1, 1) == 61000, past(1, 1, 1) == 3661000, past(0, 0, 0)
      == 0, past(1, 0, 1) == 3601000, past(1, 0, 0) == 3600000)
