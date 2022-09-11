var readline = require("readline");
var reader = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let width : number, active : number;
let lab : number[][] = [];

let inputCount = 0;

reader.on('line', getInput).on('close', printResult);

function getInput(input : string) : void {
    if(inputCount === 0)    [width, active] = input.split(' ').map((element) => parseInt(element));
    if(inputCount > 0 && inputCount <= width)    lab.push(input.split(' ').map((element) => parseInt(element)));
    inputCount++;

    if(inputCount > width)  reader.close();
}

function printResult() : void {
    
}