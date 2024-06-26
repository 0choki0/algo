function solution(num_list) {
    var odd='', even='', answer;
    for (num of num_list) {
        if (num%2 === 0) {
            even += num;
        } else {
            odd += num;
        }
    }
    answer = parseInt(odd) + parseInt(even)
    return answer 
}