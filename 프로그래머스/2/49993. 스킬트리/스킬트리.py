def solution(skill, skill_trees):
    answer = 0
    skill = {s: i for i, s in enumerate(skill)}
    for skill_tree in skill_trees:

        step = -1
        for s in skill_tree:
            if s in skill.keys(): # 문자가 스킬 순서에 영향을 받는다면
                if skill[s] > step: # 찍으려는 스킬이 현재 스텝보다 높은 경우
                    if skill[s] == step + 1: # 바로 윗 단계 스킬일 경우
                        step += 1 # 스텝을 윗 단계로 변경
                    else: # 2계층 이상 위인 경우 
                        step = -2
                        break 
            else:
                continue
        if step != -2:
            answer += 1

    return answer