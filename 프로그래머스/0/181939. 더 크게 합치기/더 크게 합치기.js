function solution(a, b) {
    var A='', B='';
    A = A.concat(a,b);
    B = B.concat(b,a);
    if (A>B) {
        return +A
    } else {
        return +B
    }
}