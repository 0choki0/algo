function solution(price) {
    var sale;
    if (price >= 500000) {
        sale = 1-0.2;
    } else if (price >= 300000) {
        sale = 1-0.1;
    } else if (price >= 100000) {
        sale = 1-0.05
    } else {
        sale = 1;
    }
    return Math.trunc(price*sale);
}