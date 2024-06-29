function solution(num_list) {
    for ([i,v] of num_list.entries()) {
        if (v<0) {
            return i
        }
    }
    return -1
}