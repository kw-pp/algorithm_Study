function solution(distance, scope, times) {
    var answer = 0;
    var points = [];

    for(let i=0; i<scope.length; i++) {
        for(let j=scope[i][0]; j<scope[i][1]; j++) {
            if(points[j] === undefined) {
                points[j] = [];
                points[j].push(i);
            }
            else {
                points[j].push(i);
            }
        }
    }

    for(let i=0; i<distance; i++) {
        var guard = points[i];

        if(guard === undefined) continue;

        for(let i=0; i<guard.length; i++) {
            if(i % (times[guard][0] + times[guard][1]) < times[guard][0]) {
                return i;
            }
        }
    }

    return distance;
}