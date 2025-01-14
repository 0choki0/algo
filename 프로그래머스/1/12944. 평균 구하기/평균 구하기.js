const solution = (arr) => {
    const sum = arr.reduce((acc, n) => acc + n, 0)
    return sum / arr.length
}