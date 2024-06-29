function solution(my_string) {
    let rm = 'aeiou', answer = '';
    for (a of my_string) {
        rm.includes(a)?answer:answer+=a
    }
    return answer
}