const lenValidator = (s) => 
    s.length === 4 || s.length === 6; // 길이가 4 또는 6인지 정확히 확인

const digitValidator = (s) => /^\d+$/.test(s); // 모든 문자가 숫자인지 확인

function solution(s) {
    return lenValidator(s) && digitValidator(s); // 두 조건이 모두 만족되면 true 반환
}
