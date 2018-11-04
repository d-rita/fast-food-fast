document.getElementById('payform').addEventListener('submit', addOrder);
let orderUrl = 'http://127.0.0.1:5000/api/v1/users/orders';
token = localStorage.getItem('token')

function addOrder(e) {
    e.preventDefault();

    let foodId = document.getElementById('add-btn').value;
    let location = document.getElementById('location').value;

    let newOrder = {
        food_id: foodId,
        location: location
    }

    fetch(orderUrl, {
            method: 'POST',
            headers: {
                'Authorization': `Bearer ${token}`,
                'Accept': 'application/json, text/plain, */*',
                'Content-type': 'application/json',
            },
            mode: "cors",
            body: JSON.stringify(newOrder)
        })
        .then(res => res.json())
        .then(response => {
            if (response.message === 'Created one food order') {
                alert('You have made one new order');
            } else {
                alert(`${response.message}`)
                console.log(response.message)
            }
        })
        .catch(err => console.log(err))
}