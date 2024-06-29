function solution(my_string, n) {
    var answer = '';
    for (s of my_string) {
        answer += s.repeat(n)
    }
    return answer;
}