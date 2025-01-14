const solution = (x, n) => {
    const ans = []
    for (i=0; i <n; i++) {
        ans.push(x+i*x)
    }
    return ans
} 