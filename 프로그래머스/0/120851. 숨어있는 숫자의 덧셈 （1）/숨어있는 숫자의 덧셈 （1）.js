function solution(my_string) {
    var answer = 0;
    for (n of my_string) {
        n = parseInt(n)
        if (n) {
            answer += n 
        }
    }
    return answer;
}
