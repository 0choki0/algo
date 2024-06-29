function solution(n) {
    let answer = [];
    while (n != 1) {
        answer.push(n)
        n%2?n=3*n+1:n/=2;
    }
    answer.push(n)
    return answer;
}