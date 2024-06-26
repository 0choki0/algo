function solution(money) {
    var answer = [], n;
    n = Math.trunc(money/5500);
    answer.push(n, money-5500*n);
    return answer;
}