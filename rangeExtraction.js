function solution(list) {
    let tempList = list.map((element, index) => list[index - 1] - element);
    let finalList = [];
    let primer;
    for (i = 0; i < tempList.length; i++) {
        if (tempList[i] != -1 && tempList[i + 1] == -1 && tempList[i + 2] == -1) {
            primer = list[i];
        } else if (tempList[i] == -1 && tempList[i - 1] == -1 && tempList[i + 1] != -1) {
            finalList.push(String(primer) + "-" + String(list[i]));
        } else if (tempList[i] != -1) {
            finalList.push(list[i])
        } else if (tempList[i] == -1 && ((tempList[i + 1] + tempList[i] != -2) && (tempList[i - 1] + tempList[i] != -2))) {
            finalList.push(list[i])
        }
    };

    return finalList.toString();
}

// TODO: complete solution

solution([-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20])//, "-6,-3-1,3-5,7-11,14,15,17-20")