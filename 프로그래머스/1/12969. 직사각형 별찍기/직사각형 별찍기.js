process.stdin.setEncoding('utf8');
process.stdin.on('data', (data) => {
    const [n, m] = data.split(' ').map(Number); // 입력된 값을 정수로 변환
    const result = Array.from({ length: m }, () => '*'.repeat(n)).join('\n');
    console.log(result); // 직사각형 출력
});
