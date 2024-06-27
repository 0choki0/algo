function solution(num_list) {
    let answer;
    if (num_list.length>10) {
        answer=0;
        for (num of num_list) {
            answer += num
        }
    } else {
        answer=1;
        for (num of num_list) {
            answer *= num
        }
    }
    return answer
}