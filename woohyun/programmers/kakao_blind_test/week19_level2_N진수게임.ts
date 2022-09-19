const numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F'];

function solution(n : number, t : number, m : number,  p : number) {
    let answer = '';
    let stringLength = getLength(t, m, p);
    
    let numberString = ' 0';
    let decimal = 0;

    while(1) {
        if(numberString.length > stringLength+1)  break;
        numberString += getNumberString(n, decimal++);
    }

    for(let i=0; i<t; i++)  answer += numberString[m*i + p];

    return answer;
}

function getLength(t : number, m : number, p : number) : number {
    return (t-1)*m + p;
}

function getNumberString(n : number, decimal : number) : string {
    let result = '';

    while(decimal > 0) {
        let rest = decimal % n;
        result = numbers[rest] + result;

        decimal = (decimal - rest) / n;
    }

    return result;
}