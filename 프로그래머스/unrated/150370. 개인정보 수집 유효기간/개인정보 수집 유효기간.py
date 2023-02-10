def solution(today, terms, privacies):
    year_of_today, month_of_today, date_of_today = map(int, today.split("."))
    
    terms_dict = dict()
    for term in terms:
        k, v = term.split()
        valid_years = int(v)//12
        valid_months = int(v)%12
        terms_dict[k] = (valid_years, valid_months)

    answer = []
    for i, privacy in enumerate(privacies, 1):
        day, term = privacy.split()
        valid_years, valid_months = terms_dict[term]
        year_of_day, month_of_day, date_of_day = map(int, day.split("."))
        
        year_of_expire = year_of_day + valid_years
        month_of_expire = month_of_day + valid_months
        date_of_expire = date_of_day

        if (year_of_today*12*28 + month_of_today*28 + date_of_today) >= (year_of_expire*12*28 + month_of_expire*28 + date_of_expire):
            answer.append(i)
    
    return answer