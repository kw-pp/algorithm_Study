var readline = require("readline");
var reader = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let seatCount :number;
let fixedCount :number = 0;
let fixedArray :number[] = [0];
let count :number = 0;

reader.on('line', getInput).on('close', countCase);

function getInput(input: string) :void {
    if(count == 0)                          seatCount = parseInt(input);
    if(count == 1)                          fixedCount = parseInt(input);
    if(count > 1 && count < fixedCount + 2) fixedArray.push(parseInt(input));
    count++;

    if(count >= fixedCount + 2) {
        fixedArray.push(seatCount+1);
        reader.close();
    }
}

function countCase() :void {
    let caseCount :number = 1;

    for(let i :number = 1; i < fixedArray.length; i++) {
        caseCount *= subCaseCount(fixedArray[i] - fixedArray[i-1] - 1);
    }

    console.log(caseCount);
}

function subCaseCount(target :number) :number {
    if(target == 0) return 1;
    if(target == 1) return 1;

    return subCaseCount(target-1) + subCaseCount(target-2);
}