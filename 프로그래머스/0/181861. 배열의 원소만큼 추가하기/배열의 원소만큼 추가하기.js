function solution(arr) {
    let answer = [];
    for (num of arr) {
        let i=0;
        while (i<num) {
            answer.push(num);
            i++;
        }
    }
    return answer
}