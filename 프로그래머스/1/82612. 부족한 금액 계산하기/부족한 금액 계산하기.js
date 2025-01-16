const solution = (price, money, count) => {
    let sum = 0
    for (let i=1; i <= count; i++) {
        sum += price*i
    }
    const ans = sum-money
    return ans >=0 ? ans : 0 
}