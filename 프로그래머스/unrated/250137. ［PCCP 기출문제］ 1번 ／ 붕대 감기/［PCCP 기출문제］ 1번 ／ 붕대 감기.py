def solution(bandage, health, attacks):
    
    attack_time = {}
    for attack in attacks:
        attack_time[attack[0]] = attack[1]


    time, combo = 0, 0
    maximum = health
    while time != attacks[-1][0]: 
        time += 1
        combo += 1

        # attacked
        if time in attack_time.keys():
            combo = 0
            health -= attack_time[time]
            if health <= 0:
                return - 1
        # heal
        else:
            health += bandage[1]
            if combo == bandage[0]:
                health += bandage[2]
                combo = 0
            if health > maximum:
                health = maximum
        
    return health