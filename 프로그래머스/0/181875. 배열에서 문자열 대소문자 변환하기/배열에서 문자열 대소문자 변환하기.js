function solution(strArr) {
    let answer = []
    for ([i,str] of strArr.entries()) {
        i%2 ? answer.push(str.toUpperCase()): answer.push(str.toLowerCase())
    }
    return answer
}