function solution(num_list) {
    var odd=0, even=0;
    for (num of num_list) {
        num%2?odd++:even++;
    }
    return [even, odd];
}