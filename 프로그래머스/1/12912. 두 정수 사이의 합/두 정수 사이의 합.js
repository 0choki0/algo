const solution = (a, b) => {
    const [M, m] = [Math.max(a,b), Math.min(a,b)] 
    const list = Array.from({length: M-m+1}, (_, i) => m + i)
    return list.reduce((sum, num) => sum + num, 0)
}