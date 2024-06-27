function solution(arr, n) {
    var answer = [];
    if (arr.length%2) {
        for (let [i, v] of arr.entries()) {
            answer.push(i%2 ? v : v+n);
        }
    } else {
        for (let [i, v] of arr.entries()) {
            answer.push(i%2?v+n:v)
        }
    }
    return answer;
}
