def solution(today, terms, privacies):
    t_year, t_month, t_day = map(int, today.split('.'))
    term_dict = dict()
    for term in terms:
        privacy_type, valid_duration = term.split()
        term_dict[privacy_type] = int(valid_duration)
    
    
    answer = []
    
    for i, privacy in enumerate(privacies):
        date, privacy_type = privacy.split()
        year, month, day = map(int, date.split('.'))
        
        valid_duration_of_privacy_type = term_dict[privacy_type]
        e_year = year
        e_month = month + valid_duration_of_privacy_type
        e_day = day - 1
        if e_day == 0:
            e_day = 28
            e_month -= 1
        if e_month > 12:
            if e_month % 12 != 0:
                e_year += e_month // 12
                e_month = e_month % 12
            else:
                e_year += e_month // 12 - 1
                e_month = 12
        
        if t_year > e_year or \
            t_year == e_year and t_month > e_month or \
            t_year == e_year and t_month == e_month and t_day > e_day:
            answer.append(i+1)
        
    return answer