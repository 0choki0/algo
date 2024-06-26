function solution(array, height) {
    var answer;
    answer = array.filter((h) => h>height)
    return answer["length"];
}