const solution = (x) => {
    const y = String(x).split('').reduce((acc, num) => acc + Number(num), acc=0)
    return x % y === 0

}