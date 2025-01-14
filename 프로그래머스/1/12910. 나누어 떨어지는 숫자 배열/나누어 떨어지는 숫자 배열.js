const solution = (arr, divisor) => {
    const ans = arr.filter((num) => num % divisor === 0);
    return ans.length > 0 ? ans.sort((a, b) => a - b) : [-1];
};
