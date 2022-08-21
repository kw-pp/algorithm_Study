var readline = require("readline");
var reader = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let inputArray : number[] = [];
let shorter :number;
let further :number;
let count :number = 0;

reader.on('line', readLine).on('close', getSeats);

function readLine(line :string) :void {
    let inputSplitted :number[] = line.trim().split(' ').filter(blankFilter).map(parseNumber);

    inputArray = inputArray.concat(inputSplitted);
    count += inputSplitted.length;

    if(count >= 2) {
        reader.close();
        return;
    }
}

function blankFilter(word :string) :boolean {
    return word != "";
}

function parseNumber(word :string) :number {
    return parseInt(word);
}

function getSeats() :void {
    let answer :number = 0;

    shorter = inputArray[0];
    further = inputArray[1];

    for(let i :number = shorter; i <= further; i++) answer += i;
    for(let i :number = 1; i <= further - shorter; i++) {
        let iCount :number = Math.floor(further / i) - Math.floor((shorter - 1) / i);
        answer -= getErasedCount(i) * (iCount - 1);
    }

    console.log(answer);
}

function getErasedCount(target :number) :number {
    if(target == 1) return 1;

    let maxDivisor :number = 1;
    let share :number = target;

    for(let divisor :number = 2; divisor <= target/2; divisor++) {
        if(target % divisor == 0) {
            maxDivisor = maxDivisor < divisor ? divisor :maxDivisor;
            share = target / divisor;
        }
    }

    if(maxDivisor == 1)     return target - 1;
    if(maxDivisor == share) return target - maxDivisor;

    return maxDivisor + share - gcd(maxDivisor, share);
}

function gcd(bigger :number, smaller :number) :number {
    let rest :number = bigger % smaller;

    if(rest == 0)   return smaller;
    return gcd(smaller, rest);
}