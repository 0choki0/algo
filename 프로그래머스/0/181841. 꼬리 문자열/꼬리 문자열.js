function solution(str_list, ex) {
    let answer = '';
    for (let str of str_list) {
        if (str.search(ex) == -1) {
            answer = answer.concat(str)
        }
    }
    return answer;
}