function pickPeaks(arr) {
    let position = [];
    let peak = [];
    let new_arr = arr.map((valor, index) => {
        return arr[index] - arr[index - 1]
    })
    for (let i = 1; i < new_arr.length; i++) {
        if (new_arr[i] > 0 & new_arr[i + 1] < 0) {
            peak.push(arr[i]);
            position.push(i);
        } else if (new_arr[i] > 0 & new_arr[i + 1] == 0) {
            for (let j = i + 1; j < arr.length; j++) {
                if (new_arr[j] > 0) { break; } else if (new_arr[j] < 0) {
                    peak.push(arr[i]);
                    position.push(i);
                    break;
                }
            }

        }
    }
    return { pos: [position], peaks: [peak] }
}


pickPeaks([1, 2, 3, 6, 4, 1, 2, 3, 2, 1])//, {pos:[3,7], peaks:[6,3]});
pickPeaks([3, 2, 3, 6, 4, 1, 2, 3, 2, 1, 2, 3])//, {pos:[3,7], peaks:[6,3]});
pickPeaks([3, 2, 3, 6, 4, 1, 2, 3, 2, 1, 2, 2, 2, 1])//, {pos:[3,7,10], peaks:[6,3,2]});
pickPeaks([2, 1, 3, 1, 2, 2, 2, 2, 1])//, {pos:[2,4], peaks:[3,2]});
pickPeaks([2, 1, 3, 1, 2, 2, 2, 2])//, {pos:[2], peaks:[3]});
pickPeaks([2, 1, 3, 2, 2, 2, 2, 5, 6])//, {pos:[2], peaks:[3]});
pickPeaks([2, 1, 3, 2, 2, 2, 2, 1])//, {pos:[2], peaks:[3]});
pickPeaks([1, 2, 5, 4, 3, 2, 3, 6, 4, 1, 2, 3, 3, 4, 5, 3, 2, 1, 2, 3, 5, 5, 4, 3])//, {pos:[2,7,14,20], peaks:[5,6,5,5]});
pickPeaks([])//,{pos:[],peaks:[]});
pickPeaks([1, 1, 1, 1])//,{pos:[],peaks:[]});