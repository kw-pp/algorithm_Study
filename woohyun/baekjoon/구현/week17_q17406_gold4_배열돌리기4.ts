var readline = require("readline");
var reader = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let matrix : number[][] = [];
let cases : number[][] = [];
let width : number, height : number;
let minValue = 250000;

let caseCount : number;
let inputCount = 0;

reader.on('line', getInput).on('close', printMin);

function getInput(input : string) : void {
    if(inputCount === 0) {
        [height, width, caseCount] = input.split(' ').map((element) => parseInt(element));
    }

    if(inputCount > 0 && inputCount <= height) {
        matrix.push(input.split(' ').map((element) => parseInt(element)));
    }

    if(inputCount > height && inputCount <= height + caseCount) {
        const [y, x, distance] = input.split(' ').map((element) => parseInt(element));
        cases.push([y-1, x-1, distance]);
    }

    inputCount++;

    if(inputCount > height + caseCount) reader.close();
}

function printMin() : void {
    let caseList : number[] = [];
    for(let i=0; i<cases.length; i++)   caseList.push(i);

    matrixMin(matrix, caseList);
    console.log(minValue);
}

function matrixMin(target : number[][], caseList : number[]) : void {
    if(caseList.length === 0) {
        for(let i=0; i<height; i++) {
            let sum = 0;
            for(let j=0; j<width; j++)  sum += target[i][j];

            if(sum < minValue)  minValue = sum;
        }

        return;
    }

    for(let i=0; i<caseList.length; i++) {
        const [y, x, r] = cases[caseList[i]];
        let targetCopy = target.map((element) => element.slice());

        let nextTarget = rotate(targetCopy, y, x, r);
        let nextCases = [...caseList.slice(0, i), ...caseList.slice(i+1, caseList.length)];

        matrixMin(nextTarget, nextCases);
    }
}

function rotate(previous : number[][], y : number, x : number, r: number) : number[][] {
    const direction = [[1, 0], [0, 1], [-1, 0], [0, -1]];
    let newOne = previous.map((element) => element.slice());

    for(let i=1; i<=r; i++) {
        let temp = newOne[y-i][x-i];

        for(let j=0; j<4; j++) {
            if(direction[j][0] === 0) {
                const range = direction[j][1]*i;

                let k = y-range;

                while(Math.abs(y+range-k) > 0) {
                    let copy = newOne[k+direction[j][1]][x+range];
                    newOne[k+direction[j][1]][x+range] = temp;
                    temp = copy;

                    k+=direction[j][1];
                }
            }

            if(direction[j][1] === 0) {
                const range = direction[j][0]*i;

                let k = x-range;

                while(Math.abs(x+range-k) > 0) {
                    let copy = newOne[y-range][k+direction[j][0]];
                    newOne[y-range][k+direction[j][0]] = temp;
                    temp = copy;

                    k+=direction[j][0];
                }
            }
        }
    }

    return newOne;
}