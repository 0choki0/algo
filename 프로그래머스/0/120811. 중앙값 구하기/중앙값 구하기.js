function solution(array) {
    array.sort((a,b) => a-b);
    var n=array.length;
    console.log("array : ", array);
    return array[Math.floor(n/2)];
}