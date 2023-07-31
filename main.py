def nth_triangular_number(n):
    if n%100 == 1:
        nth_ordinal = f"{n}st"
    elif n%100 == 2:
        nth_ordinal = f"{n}nd"
    else:
        nth_ordinal = f"{n}th"
    answer = int(n*(n+1)/2)
    print(f"The {nth_ordinal} triangular number is {answer}")
    return answer

nth_triangular_number(100)