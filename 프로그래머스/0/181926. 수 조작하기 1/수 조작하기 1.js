function solution(n, control) {
    for (a of control) {
        if (a==='w') {
            n += 1;
        } else if (a==='s') {
            n -= 1;
        } else if (a==='d') {
            n += 10;
        } else if (a==='a') {
            n -= 10
        }
    }
    return n;
}