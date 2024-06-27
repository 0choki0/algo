function solution(my_string, alp) {
    var answer = '';
    for (let s of my_string) {
        s === alp?answer += alp.toUpperCase():answer += s
    }
    return answer;
}