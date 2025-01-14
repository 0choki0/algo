const solution = (numbers) => {
    let numlist = Array.from({length:10}, (_, i) => i)
    for (const i of numbers) {
       numlist = numlist.filter(item => i!==item) 
    }
    return numlist.reduce((acc, n) => acc + n, acc =0)
}