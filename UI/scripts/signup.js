document.getElementById('signup').addEventListener('submit', registerUser);
let url = 'https://diana-fast-food-fast.herokuapp.com/api/v1/auth/signup';

function registerUser(e) {
    e.preventDefault();

    let username = document.getElementById('username').value;
    let email = document.getElementById('email').value;
    let password = document.getElementById('password').value;
    let adminRadio = document.getElementById('admin').checked;
    console.log(adminRadio);

    let newUser = {
        username: username,
        email: email,
        password: password,
        admin: adminRadio
    }

    fetch(url, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            mode: "cors",
            body: JSON.stringify(newUser)
        })
        .then(response => response.json())
        .then(res => {
            console.log(res.token);
            if (res.message === 201) {
                alert(`You can now sign in as ${newUser['username']}`);
                window.location.replace('user_login.html');
            } else {
                alert('Failed to sign up')
            }
        })
        .catch(err => console.log(err))

}