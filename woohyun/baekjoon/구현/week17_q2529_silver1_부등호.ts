var readline = require("readline");
var reader = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let inequalitiesCount : number;
let inequalities : string[];

let inputCount : number = 0;

reader.on('line', getInput).on('close', printResult);

function getInput(input : string) : void {
    if(inputCount === 0)    inequalitiesCount = parseInt(input);
    if(inputCount === 1)    inequalities = input.split(' ');
    inputCount++;

    if(inputCount > 1)      reader.close();
}

function printResult() : void {
    let maxValue = '';
    let minValue = '';

    // max
    let indexes = [0];

    for(let i : number = 0; i < inequalitiesCount; i++) {
        if(inequalities[i] === '>') indexes.push(i+1);
    }
    
    indexes.push(inequalitiesCount+1);

    for(let i : number = 1; i < indexes.length; i++) {
        for(let j : number = 9-indexes[i]+1; j <= 9-indexes[i-1]; j++)    maxValue += j.toString();
    }

    // min
    indexes = [0];

    for(let i : number = 0; i < inequalitiesCount; i++) {
        if(inequalities[i] === '<') indexes.push(i+1);
    }
    
    indexes.push(inequalitiesCount+1);

    for(let i : number = 1; i < indexes.length; i++) {
        for(let j : number = indexes[i]-1; j >= indexes[i-1]; j--)  minValue += j.toString();
    }

    console.log(maxValue);
    console.log(minValue);
}