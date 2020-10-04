def solution(string, markers):
    final_string = string
    for each in markers:
        finalstr = final_string.find(
            '''\n''', final_string.find(each))
        if finalstr == -1:
            final_string = final_string.split(each)[0]
            break
        start = final_string[:final_string.find(each)]
        end = final_string[finalstr:]
        final_string = start + end

    print(str(final_string))
    # your code here


result = solution(
    "apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
solution("a #b\nc\nd $e f g", ["#", "$"])
solution('.\navocados watermelons ?\npears', ['#', '=', ',', '-', "'", '.'])
