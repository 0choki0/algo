const solution = (arr) => {
    if (arr.length <= 1) {
        return [-1]
    } 
    const minNum = Math.min(...arr)
    const list = arr.filter((item) => item !== minNum)
    return list 
}