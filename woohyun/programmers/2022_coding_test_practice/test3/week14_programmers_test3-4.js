function solution(n, lighthouse) {
    var answer = 0;

    var points = [];

    for(let i=0; i<n-1; i++) {
        var house1 = lighthouse[i][0];
        var house2 = lighthouse[i][1];
        
        if(points[house1] === undefined)  points[house1] = [];
        if(points[house2] === undefined)  points[house2] = [];

        points[house1].push(house2);
        points[house2].push(house1);
    }

    while(1) {
        var parentList = [];
        
        for(let i=0; i<n-1; i++) {
            if(points[i].length === 0)  continue;
            if(points[i].length === 1)  {
                if(parentList.indexOf(points[i]) === -1)    parentList.push(points[i]); 


            }
        }

        if(parentList.length === 0) break;

        answer += parentList.length;

        for(let i=0; i<parentList.length; i++) {
            for(let j=0; j<points[parentList[i]].length; j++) {
                points[parentList[i]].splice(points[parentList[i]].indexOf(points[parentList[i]][j]), 1);
                points[points[parentList[i]][j]].splice(points[points[parentList[i]][j]].indexOf(parentList[i]), 1);
            }
        }
    }

    return answer;
}