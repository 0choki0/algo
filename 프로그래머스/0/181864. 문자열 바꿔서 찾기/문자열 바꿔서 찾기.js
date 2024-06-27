function solution(myString, pat) {
    let answer = ''
    for (s of myString) {
        if (s==="A") {
            answer+="B";
    } else {
        answer+="A";
    }
    }
    return answer.includes(pat)?1:0;
}