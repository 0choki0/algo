function solution(myString) {
    let answer=[];
    for (a of myString.split('x')) {
        answer.push(a.length);
    }
    return answer
}