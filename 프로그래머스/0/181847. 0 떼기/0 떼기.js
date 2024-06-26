function solution(n_str) {
    stop = -1
    for (i in n_str) {
        if (n_str[i] == '0') {
            continue;
        } else {
            stop = i;
            break;
        }
    }
    if (stop === -1) {
        return ""
    }
    return n_str.substr(i)
}