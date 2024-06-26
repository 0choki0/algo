function solution(rsp) {
    var answer = '';
    for (a of rsp) {
        if (a==2) {
            answer += 0;
        } else if (a==0) {
            answer += 5;
        } else {
            answer += 2
        }
    }
    return answer;
}