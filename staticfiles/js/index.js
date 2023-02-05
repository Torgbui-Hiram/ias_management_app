// counter app
let count = 0;
document.getElementById('decreaseBtn').onclick = function () {
    count -= 1;
    document.getElementById('counterLbl').innerHTML = count;
}
document.getElementById('resetBtn').onclick = function () {
    count = 0;
    document.getElementById('counterLbl').innerHTML = count;
}
document.getElementById('increaseBtn').onclick = function () {
    count += 1;
    document.getElementById('counterLbl').innerHTML = count;
}

let username;
let password;
// l mycheckbox;
// document.getElementById('submit').onclick = function () {
//     document.getElementById('username').value = username;
//     document.getElementById('password').value = password;
//     document.getElementById('email').value = email;
//     console.log(username);
//     console.log(password);
//     console.log(email);
// }
document.getElementById('submit').onclick = function () {
    const mycheckBox = document.getElementById('mycheckbox');
    if (document.getElementById("mycheckbox").checked) {
        console.log('working');
    }
    else {
        console.log('Not working');
    }
}