function solution(array) {
    var answer = [], temp=0, temp2=0;
    for (const i in array) {
        if (array[i]>temp) {
            temp = array[i];
            temp2 = parseInt(i);
        }
    }
    answer.push(temp, temp2);
    return answer;
}