document.getElementById('signup').addEventListener('submit', registerUser);
let url = 'https://diana-fast-food-fast.herokuapp.com/api/v1/auth/signup';

function registerUser(e) {
    e.preventDefault();

    let username = document.getElementById('username').value;
    let email = document.getElementById('email').value;
    let password = document.getElementById('password').value;
    let adminCheck = document.getElementById('admin').checked;
    console.log(adminCheck);

    let newUser = {
        username: username,
        email: email,
        password: password,
        admin: adminCheck
    }

    fetch(url, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            mode: "cors",
            body: JSON.stringify(newUser)
        })
        .then(response => response.json())
        .then(res => {
            if (res.message === 'New user added') {
                alert(`You can now sign in as ${newUser['username']}`);
                window.location.replace('user_login.html');
            } else {
                alert(res.message)
            }
        })
        .catch(err => console.log(err))

}