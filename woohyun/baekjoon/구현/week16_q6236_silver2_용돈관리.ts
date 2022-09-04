var readline = require("readline");
var reader = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let dayCosts : number[] = [];

let day : number;
let withdrawCount : number;

let minimum : number = 0;
let maximum : number = 0;

let inputCount : number = 0;

reader.on('line', getInput).on('close', printMinWithdrawAmount);

function getInput(input : string) : void {
    if(inputCount === 0)    [day, withdrawCount] = input.split(' ').map((element) => parseInt(element));
    if(inputCount > 0 && inputCount <= day) {
        const cost : number = parseInt(input);

        if(minimum < cost)  minimum = cost;
        dayCosts.push(cost);
    }

    inputCount++;

    if(inputCount > day) {
        maximum = minimum * Math.ceil(day/withdrawCount);
        reader.close();
    }
}

function printMinWithdrawAmount() : void {
    if(enough(minimum)) {
        console.log(minimum);
        return;
    }

    while(1) {
        const allowance = Math.ceil((maximum + minimum) / 2);
        
        if(allowance === maximum) {
            console.log(maximum);
            return;
        }

        if(enough(allowance))   maximum = allowance;
        else                    minimum = allowance;
    }
}

function enough(allowance : number) :boolean {
    let currentAllowance = allowance;
    let currentWithdrawCount = withdrawCount-1;

    for(let i : number = 0; i < day; i++) {
        if(currentAllowance < dayCosts[i]) {
            currentAllowance = allowance;
            currentWithdrawCount--;
        }

        if(currentWithdrawCount < 0)    return false;
        currentAllowance -= dayCosts[i];
    }

    return true;
}