function solution(todo_list, finished) {
    var answer = [];
    for ([i,v] of finished.entries()) {
        v?answer:answer.push(todo_list[i])
    }
    return answer;
}