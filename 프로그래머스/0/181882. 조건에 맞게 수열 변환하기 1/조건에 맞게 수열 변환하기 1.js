function solution(arr) {
    let answer = [];
    for (v of arr) {
        if (v>=50) {
            if (v%2) {
                answer.push(v);
            } else {
                answer.push(v/2);
            } 
        } else {
            if (v%2) {
                answer.push(2*v);
            } else {
                answer.push(v)
            }
        }
    }
    return answer
    
}