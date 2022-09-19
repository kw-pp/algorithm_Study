function solution(queue1 : Array<number>, queue2 : Array<number>) : number {
    let answer = 0;

    let length1 = queue1.length;
    let length2 = queue1.length;
    let index1 = 0;
    let index2 = 0;

    let half : number;
    let sum1 = 0;
    let sum2 = 0;

    queue1.forEach((element) => sum1 += element);
    queue2.forEach((element) => sum2 += element);
    half = sum1 + sum2;
    
    if(half % 2 === 1)  return -1;
    half /= 2;

    while(index1 < length1 || index2 < length2) {
        if(sum1 === sum2)   return answer;
        answer++;

        if(sum1 < sum2) {
            let current = queue2[index2++];
            queue1.push(current);

            sum1 += current;
            sum2 -= current;

            continue;
        }

        let current = queue1[index1++];
        queue2.push(current);

        sum1 -= current;
        sum2 += current;
    }

    return -1;
}