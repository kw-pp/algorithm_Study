function solution(ingredient) {
    var answer = 0;

    var toString = '';

    for(let i=0; i<ingredient.length; i++) {
        toString += ingredient[i];
    }

    while(1) {
        var splitted = toString.split('1231');

        if(splitted.length == 1)    break;

        answer += splitted.length-1;

        toString = '';
        for(let i=0; i<splitted.length; i++)    toString += splitted[i];
    }

    return answer;
}