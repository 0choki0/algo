function solution(n) {
    let m = Math.floor(n/2)
    return n % 2 === 1 ? ('수박').repeat(m) + '수' : ('수박').repeat(m)
}