let cars : {total : number, inOut : String}[] = [];

let baseTime : number;
let baseFee : number;
let unitTime  : number;
let unitFee : number;

function solution(fees : number[], records : String[]) : number[] {
    let answer : number[] = [];

    baseTime = fees[0];
    baseFee = fees[1];
    unitTime = fees[2];
    unitFee = fees[3];

    records.forEach((record) => {
        const [time, carNumber, inOut] = record.split(' ');

        if(cars[parseInt(carNumber)] === undefined) {
            if(inOut === "IN")  cars[parseInt(carNumber)] = {"total": -timeToMinute(time), "inOut": inOut};
            else                cars[parseInt(carNumber)] = {"total": timeToMinute(time), "inOut": inOut};
        }
        else {
            if(inOut === "IN") {
                cars[parseInt(carNumber)].total -= timeToMinute(time);
                cars[parseInt(carNumber)].inOut = inOut;
            }
            else {
                cars[parseInt(carNumber)].total += timeToMinute(time);
                cars[parseInt(carNumber)].inOut = inOut;
            }
        }
    });

    cars.forEach((car) => {
        if(car === undefined)   return;
        if(car.inOut === "IN")  car.total += timeToMinute("23:59");

        // answer.push(car.total);
        answer.push(calculate(car.total));
    });

    return answer;
}

function timeToMinute(time : String) : number {
    const [hour, minute] = time.split(':').map((element) => parseInt(element));
    return hour*60 + minute;
}

function calculate(total : number) : number { 
    if(total <= baseTime)    return baseFee;

    let sum = baseFee;
    total -= baseTime;

    sum += Math.ceil(total / unitTime) * unitFee;

    return sum;
}