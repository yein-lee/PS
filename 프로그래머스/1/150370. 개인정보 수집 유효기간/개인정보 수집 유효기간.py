def solution(today, terms, privacies):
    t_year, t_month, t_day = map(int, today.split('.'))
    today_c = t_year * 12 * 28 + t_month * 28 + t_day
    
    term_dict = dict()
    for term in terms:
        privacy_type, valid_duration = term.split()
        term_dict[privacy_type] = int(valid_duration)
    
    
    answer = []
    
    for i, privacy in enumerate(privacies):
        date, privacy_type = privacy.split()
        year, month, day = map(int, date.split('.'))
        c = year * 12 * 28 + month * 28 + day
        e_c = c + term_dict[privacy_type] * 28
        
        if today_c > e_c - 1:
            answer.append(i+1)
        
    return answer