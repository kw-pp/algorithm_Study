var readline = require("readline");
var reader = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let peopleCount :number = 0;
let relationsCount :number = 0;
let person1 :number, person2 :number;
let found :boolean = false;

let relations :number[][] = [];
let inputCount :number = 0;


reader.on('line', getInput).on('close', degreeOfKinship);

function getInput(input: string) :void {
    if(inputCount == 0) peopleCount = parseInt(input);
    if(inputCount == 1) [person1, person2] = parseIntArray(input);
    if(inputCount == 2) relationsCount = parseInt(input);
    if(inputCount > 2 && inputCount <= relationsCount + 2) {
        let [first, second] = parseIntArray(input);

        if(relations[first] === undefined)  relations[first] = [];
        relations[first].push(second);

        if(relations[second] === undefined)  relations[second] = [];
        relations[second].push(first);
    }

    inputCount++;

    if(inputCount > relationsCount + 2)  reader.close();
}

function parseIntArray(from :string) :number[] {
    return from.trim().split(' ')
        .filter((element: string) => element != "")
        .map((element :string) => parseInt(element));
}

function degreeOfKinship() :void {
    dfs(person1, person2, -1, 0);

    if(!found)  console.log(-1);
}

function dfs(from :number, target :number, previous :number, degree :number) :void {
    for(let i :number = 0; i < relations[from].length; i++) {
        if(relations[from][i] === previous) continue;
        if(relations[from][i] === target) {
            console.log(degree+1);
            found = true;

            return;
        }

        dfs(relations[from][i], target, from, degree+1);
    }
}