const solution = (s) => {
    const countP = (s.match(/p/gi) || []).length; // 'p' 또는 'P'의 개수를 셈
    const countY = (s.match(/y/gi) || []).length; // 'y' 또는 'Y'의 개수를 셈
    return countP === countY;
};
