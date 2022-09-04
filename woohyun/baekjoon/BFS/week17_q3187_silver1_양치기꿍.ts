var readline = require("readline");
var reader = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let width : number, height : number;
let area : string[] = [];

let wolvesCount = 0;
let sheepCount = 0;

let inputCount = 0;
const nesw = [[-1, 0], [0, 1], [1, 0], [0, -1]];

reader.on('line', getInput).on('close', printResult);

function getInput(input : string) : void {
    if(inputCount === 0)    [height, width] = input.split(' ').map((element) => parseInt(element));
    if(inputCount > 0 && inputCount <= height)   area.push(input);
    inputCount++;

    if(inputCount > height) reader.close();
}

function printResult() : void {
    for(let i=0; i<height; i++) {
        for(let j=0; j<width; j++) {
            if(area[i][j] === '.')  bfs(i, j, 0, 0);
            if(area[i][j] === 'v')  bfs(i, j, 1, 0);
            if(area[i][j] === 'k')  bfs(i, j, 0, 1);
        }
    }

    console.log(sheepCount + ' ' + wolvesCount);
}

function bfs(y : number, x : number, v : number, k : number) : void {
    let sheep = k;
    let wolves = v;
    let positions = [[y, x]];

    area[y] = replace(area[y], x, '#');

    while(1) {
        const positionsCount = positions.length;
        if(positionsCount === 0)    break;

        let nextPositions : number[][] = [];

        for(let i=0; i<positionsCount; i++) {
            const currentY = positions[i][0];
            const currentX = positions[i][1];

            for(let j=0; j<4; j++) {
                const nextY = currentY + nesw[j][0];
                const nextX = currentX + nesw[j][1];

                if(isOutOfBound(nextY, nextX))  continue;

                if(area[nextY][nextX] !== '#') {
                    if(area[nextY][nextX] === 'v')  wolves++;
                    if(area[nextY][nextX] === 'k')  sheep++;
                    
                    nextPositions.push([nextY, nextX]);
                    area[nextY] = replace(area[nextY], nextX, '#');
                }
            }
        }

        positions = nextPositions;
    }

    if(sheep > wolves) {
        sheepCount += sheep;
        return;
    }

    wolvesCount += wolves;

}

function isOutOfBound(y : number, x : number) : boolean {
    return y < 0 || y >= height || x < 0 || x >= width;
}

function replace(target : string, index : number, newElement : string) : string {
    return target.substring(0, index) + newElement + target.substring(index+1);
}