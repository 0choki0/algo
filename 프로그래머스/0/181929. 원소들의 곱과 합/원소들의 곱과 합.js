function solution(num_list) {
    var sum_num=0, product=1;
    for (num of num_list) {
        sum_num += num;
        product *= num;
    }
    if (product < (sum_num)**2) {
        return 1
    } else {
        return 0
    }
}