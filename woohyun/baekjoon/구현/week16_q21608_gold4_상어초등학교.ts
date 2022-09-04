var readline = require("readline");
var reader = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let sideLength :number;
let inputCount :number = 0;

let favoiteList : number[][];
let seats :number[][];

reader.on('line', getInput).on('close', () => console.log(satisfaction()));

function getInput(input : string) : void {
    if(inputCount === 0) {
        sideLength = parseInt(input);

        seats = Array(sideLength);
        for(let i : number = 0; i < sideLength; i++)    seats[i] = Array(sideLength);

        favoiteList = Array(sideLength+1);
        for(let i : number = 0; i < sideLength+1; i++)  favoiteList[i] = Array(4);
    }

    if(inputCount > 0 && inputCount <= sideLength * sideLength) {
        const [student , ...favorites] = input.split(' ').map((element) => parseInt(element));
        favoiteList[student] = favorites;

        sit(student, favorites);
    }

    inputCount++;

    if(inputCount > sideLength * sideLength) reader.close();
}

function sit(student : number, favorites : number[]) : void {
    // seat, favorite 인접 개수, 빈 칸 개수 변수 생성
    // 모든 칸을 순회하며 조건에 seat 업데이트
    // 동일한 조건이면 스킵

    let seat : number[];
    let favoriteCount : number = 0;
    let emptyCount : number = 0;

    for(let i : number = 0; i < sideLength; i++) {
        for(let j : number = 0; j < sideLength; j++) {
            if(seats[i][j] !== undefined)   continue;
            if(seat === undefined)          seat = [i, j];

            let currentEmpty : number = 0;
            let currentFavorite : number = 0;

            if(i !== 0) {
                if(seats[i-1][j] === undefined)         currentEmpty++;
                if(favorites.includes(seats[i-1][j]))   currentFavorite++;
            }

            if(i !== sideLength - 1) {
                if(seats[i+1][j] === undefined)         currentEmpty++;
                if(favorites.includes(seats[i+1][j]))   currentFavorite++;
            }

            if(j !== 0) {
                if(seats[i][j-1] === undefined)         currentEmpty++;
                if(favorites.includes(seats[i][j-1]))   currentFavorite++;
            }

            if(j !== sideLength - 1) {
                if(seats[i][j+1] === undefined)         currentEmpty++;
                if(favorites.includes(seats[i][j+1]))   currentFavorite++;
            }

            if(favoriteCount < currentFavorite) {
                seat = [i, j];
                favoriteCount = currentFavorite;
                emptyCount = currentEmpty;
                
                continue;
            }

            if(favoriteCount === currentFavorite) {
                if(emptyCount < currentEmpty) {
                    seat = [i, j];
                    favoriteCount = currentFavorite;
                    emptyCount = currentEmpty;
                }
            }
        }
    }

    seats[seat[0]][seat[1]] = student;
}

function satisfaction() : number {
    let satisfactionSum : number = 0;

    for(let i : number = 0; i < sideLength; i++) {
        for(let j : number = 0; j < sideLength; j++) {
            let currentSatisfaction : number = 1;
            let currentStudent : number = seats[i][j];

            if(i !== 0 && favoiteList[currentStudent].includes(seats[i-1][j]))  currentSatisfaction *= 10;
            if(i !== sideLength - 1 && favoiteList[currentStudent].includes(seats[i+1][j])) currentSatisfaction *= 10;
            if(j !== 0 && favoiteList[currentStudent].includes(seats[i][j-1]))   currentSatisfaction *= 10;
            if(j !== sideLength - 1 && favoiteList[currentStudent].includes(seats[i][j+1])) currentSatisfaction *= 10;

            satisfactionSum += Math.floor(currentSatisfaction / 10);
        }
    }

    return satisfactionSum;
}