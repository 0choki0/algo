function solution(num_str) {
    var answer = 0;
    for (i of num_str) {
        answer += +i
    }
    return answer;
}