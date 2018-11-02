//document.getElementById('payform').addEventListener('submit', addOrder);
let orderUrl = 'https://diana-fast-food-fast.herokuapp.com/api/v1/users/orders';
token = localStorage.getItem('token')

function addOrder(e) {
    e.preventDefault();

    let foodId = document.getElementById('food_id').value;
    let location = document.getElementById('location').value;

    let newOrder = {
        food_id: foodId,
        location: location
    }

    fetch(orderUrl, {
            method: 'POST',
            headers: { 'Authorization': `Bearer ${token}` },
            mode: "cors",
            body: JSON.stringify(newOrder)
        })
        .then(res => res.json())
        .then(response => {
            output = ` 
            <table>
                <tr>
                    <th colspan="2">My order</th>
                </tr>
                <tr>
                    <td>${newOrder['food_id']}</td>
                    <td>${newOrder['location']}</td>
                </tr>
            </table> `;
            document.getElementsByClassName('checkout').innerHTML = output;
            alert('You have made one new order');
        })
        .catch(err => console.log(err))
}

document.getElementById('history').addEventListener('load', getUserOrders());

function getUserOrders() {
    fetch(orderUrl, {
            headers: { 'Authorization': `Bearer ${token}` }
        })
        .then(response => response.json())
        .then(res => {
            console.log(res)
            console.log(res.message)
            output = ''
            if (res.message === 'Your order history has been returned') {
                output = `
                <tr>
                    <th>Order_ID</th>
                    <th>Food_ID</th>
                    <th>User_ID</th>
                    <th>Location</th>
                    <th>Date</th>
                    <th>Status</th>
                </tr>
                `
                for (let x in res) {
                    output = `
                    <tr>
                        <td>${res[x].order_id}</td>
                        <td>${res[x].menu_id}</td>
                        <td>${res[x].user_id}</td>
                        <td>${res[x].location}</td>
                        <td>${res[x].date}</td>
                        <td>${res[x].status}</td> 
                    </tr>`;
                    document.getElementById('history').innerHTML = output;
                }
            } else if (res.message === 'You have no order history!') {
                output = `<p>${res.message}<p>`
                document.getElementById('history').innerHTML = output;
            }
        })
        .catch(err => console.log(err))

}