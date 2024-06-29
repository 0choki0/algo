function solution(names) {
    let answer = [];
    for ([i,v] of names.entries()) {
        !(i%5)?answer.push(v):undefined;
    }
    return answer;
}