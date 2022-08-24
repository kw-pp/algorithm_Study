var readline = require("readline");
var reader = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let games : string[] = [];

reader.on('line', getInput).on('close', () => games.forEach(printGameResult));

function getInput(input: string) :void {
    if(input === "end") reader.close();
    games.push(input);
}

function printGameResult(game :string) :void {
    let oCount :number = 0, xCount :number = 0;
    let isValid :boolean = false;

    for(let i :number = 0; i < game.length; i++) {
        if(game[i] === 'O')  oCount++;
        if(game[i] === 'X')  xCount++;
    }

    if(xCount === oCount) {
        for(let i :number = 0; i < game.length; i++) {
            if(game[i] === 'O') {
                let previous :string = game.substring(0, i) + '.' + game.substring(i+1, game.length);
                if(!isGameOver(previous))   isValid = true;
            }
        }
    }
    
    if(xCount === oCount + 1) {
        for(let i :number = 0; i < game.length; i++) {
            if(game[i] === 'X') {
                let previous :string = game.substring(0, i) + '.' + game.substring(i+1, game.length);
                if(!isGameOver(previous))   isValid = true;
            }
        }
    }

    if(!isValid || !(isGameOver(game) || !game.includes('.'))) {
        console.log('invalid');
        return;
    }

    console.log('valid');

    // if(!isValid || !isGameOver(game)) {
    //     console.log('invalid');
    //     return;
    // }
    
    // console.log('valid');
}

function isGameOver(game :string) :boolean {
    // 세로
    if(game[0] !== '.' && game[0] === game[3] && game[0] === game[6])  return true;
    if(game[1] !== '.' && game[1] === game[4] && game[1] === game[7])  return true;
    if(game[2] !== '.' && game[2] === game[5] && game[2] === game[8])  return true;

    // 가로
    if(game[0] !== '.' && game[0] === game[1] && game[0] === game[2])  return true;
    if(game[3] !== '.' && game[3] === game[4] && game[3] === game[5])  return true;
    if(game[6] !== '.' && game[6] === game[7] && game[6] === game[8])  return true;

    // 대각선
    if(game[0] !== '.' && game[0] === game[4] && game[0] === game[8])  return true;
    if(game[2] !== '.' && game[2] === game[4] && game[2] === game[6])  return true;
}