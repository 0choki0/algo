function solution(arr1, arr2) {
    if (arr1.length==arr2.length) {
        let sum_arr1=0, sum_arr2=0;
        for (a of arr1) {
            sum_arr1 += a
        }
        for (a of arr2) {
            sum_arr2 += a
        }
        if (sum_arr1 === sum_arr2) {
            return 0
        } else {
            return sum_arr1 > sum_arr2 ? 1:-1
        }
    } else {
        return arr1.length > arr2.length ? 1:-1
    }
}