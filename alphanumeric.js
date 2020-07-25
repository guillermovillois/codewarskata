function alphanumeric(string) {
    console.log(RegExp("^[a-zA-Z0-9]{1,}$").test(string));
}

alphanumeric("Mazinkaiser")
alphanumeric("hello world_")
alphanumeric("PassW0rd")
alphanumeric("_")