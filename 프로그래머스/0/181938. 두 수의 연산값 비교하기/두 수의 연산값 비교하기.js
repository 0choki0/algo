function solution(a, b) {
    var A='', B=0;
    A = A.concat(a,b);
    B = 2 * a * b;
    if (A>B) {
        return +A
    } else {
        return B
    }
}