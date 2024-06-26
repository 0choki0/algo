function solution(a, b) {
    var answer = 0, A = a % 2, B = b % 2;
    if (A & B) {
        answer += a**2 + b**2;
    } else if (A ^ B) {
        answer = 2 * (a+b)
    } else {
        answer = Math.abs(a-b);
    }
    return answer;
}
