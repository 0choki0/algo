function solution(s) {
    const d = s.length/2
    return s.length % 2 === 1 ? s.slice(d, d+1) : s.slice(d-1 , d+1)
}