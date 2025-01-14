const solution = (n) => {
  let sum = 0;

  for (let i = 1; i <= Math.sqrt(n); i++) {
    if (n % i === 0) {
      sum += i; // i는 약수
      if (i !== n / i) {
        sum += n / i; // i와 짝을 이루는 약수 추가
      }
    }
  }

  return sum;
};
