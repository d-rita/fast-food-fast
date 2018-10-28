document.getElementById('user_login').addEventListener('submit', userLogin);
let url = 'https://diana-fast-food-fast.herokuapp.com/api/v1/auth/login';

function userLogin(e) {
    e.preventDefault();

    let username = document.getElementById('username').value;
    let password = document.getElementById('password').value;

    let User = {
        username: username,
        password: password,
    };

    fetch(url, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            mode: "cors",
            body: JSON.stringify(User)
        })
        .then(res => res.json())
        .then(response => {
            if (response.message === 'Logged in as client') {
                token = response.token
                localStorage.setItem('token', token);
                alert(`Welcome ${User['username']}`);
                window.location.replace('user_dashboard.html')
            } else if (response.message === 'Logged in as admin') {
                token = response.token
                localStorage.setItem('token', token);
                alert(`Welcome ${User['username']}`);
                window.location.replace('admin_dashboard.html')
            } else {
                alert(response.message)
            }
        })
        .catch(err => console.log(err))
}