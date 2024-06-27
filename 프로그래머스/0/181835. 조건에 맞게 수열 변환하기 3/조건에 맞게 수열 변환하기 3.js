function solution(arr, k) {
    let answer = [];
    if (k%2) {
        for (i of arr) {
            answer.push(i*k);
        }
    } else {
        for (i of arr) {
            answer.push(i+k);
        }
    }
    return answer
}