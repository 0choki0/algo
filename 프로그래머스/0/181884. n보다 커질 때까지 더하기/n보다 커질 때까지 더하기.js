function solution(numbers, n) {
    var answer = 0;
    for (num of numbers) {
        answer += num;
        if (answer>n) {
            break
        }
    }
    return answer
}