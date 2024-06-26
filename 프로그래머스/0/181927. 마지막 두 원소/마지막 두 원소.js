function solution(num_list) {
    let index = num_list.length;
    if (parseInt(num_list[index-1]) > parseInt(num_list[index-2])) {
        num_list.push(num_list[index-1]-num_list[index-2])
    } else {
        num_list.push(num_list[index-1]*2)
    }
    return num_list;
}