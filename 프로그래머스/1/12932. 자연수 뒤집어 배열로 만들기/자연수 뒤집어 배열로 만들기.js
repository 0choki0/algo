const solution = (n) => {
    const str = String(n)
    const len = str.length
    return Array.from({length:len}, (_, i) => Number(str[len-i-1]))
}