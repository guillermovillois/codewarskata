function generateHashtag(str) {
    if (str.trim().length == 0) {
        console.log(false)
    } else {
        let wordsList = str.toLowerCase().split(' ');
        let finalWord = '';
        for (let i = 0; i < wordsList.length; i++) {
            finalWord = finalWord + (wordsList[i].charAt(0).toUpperCase() + wordsList[i].substring(1));
        }
        if (finalWord.length < 140) {
            console.log('#' + finalWord)
        } else {
            console.log(false)
        }
    }
}

generateHashtag("")
generateHashtag(" ".repeat(200))
generateHashtag("Do We have A Hashtag")
generateHashtag("Codewars")
generateHashtag("Codewars Is Nice")
generateHashtag("Codewars is nice")
generateHashtag("code" + " ".repeat(140) + "wars")
generateHashtag("Looooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong Cat")
generateHashtag("a".repeat(139))
generateHashtag("a".repeat(140))