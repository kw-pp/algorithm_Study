function solution(a, b, n) {
    var answer = 0;

    let whole = n;
    let have = 0;
    let rest = 0;

    while(whole >= a) {
        have = Math.floor(whole / a) * b;
        rest = whole % a;

        answer += have;
        whole = have + rest;
    }

    return answer;
}