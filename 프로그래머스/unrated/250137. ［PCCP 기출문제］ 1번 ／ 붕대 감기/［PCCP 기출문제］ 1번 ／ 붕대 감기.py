def solution(bandage, health, attacks):
    max_health = health
    c_health = health
    continuos = 0
    
    previous_attack_time = 0
    for attack_time, damage in attacks:
        continuos_recovery_time = (attack_time - previous_attack_time) - 1
        c_health += (continuos_recovery_time // bandage[0]) * bandage[2] + continuos_recovery_time * bandage[1]
        c_health = min(max_health, c_health)
        c_health -= damage
        
        if c_health <= 0:
            return -1
        previous_attack_time = attack_time
        
    return c_health