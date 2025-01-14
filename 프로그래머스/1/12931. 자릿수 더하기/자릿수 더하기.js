function solution(n) {
    const strN = String(n)
    const strList = [...strN]
    let sum = 0
    strList.map((item) => sum += Number(item))
    return sum
}