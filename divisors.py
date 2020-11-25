def divisors(integer):
    final_list = [each for each in range(
        2, integer) if (integer/each).is_integer()]

    print('{} is prime'.format(integer) if final_list == [] else final_list)


divisors(12)
divisors(25)
divisors(13)
