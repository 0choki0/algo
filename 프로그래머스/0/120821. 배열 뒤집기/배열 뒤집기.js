function solution(num_list) {
    let answer = []
    for (num of num_list) {
        answer.unshift(num);
    }
    return answer
}