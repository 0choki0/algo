const solution = (a,b) => {
    return a.reduce((sum, value, i) => sum + value * b[i], 0)
}