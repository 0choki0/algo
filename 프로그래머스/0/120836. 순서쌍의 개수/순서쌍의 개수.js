function solution(n) {
    var answer = 0;
    for (i=1; i<Math.sqrt(n); i++) {
        n%i===0?answer++:answer
    }
    return Math.sqrt(n) === parseInt(Math.sqrt(n))?answer*2+1:answer*2
}