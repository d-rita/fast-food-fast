let orderUrl = 'https://diana-fast-food-fast.herokuapp.com/api/v1/users/orders';
token = localStorage.getItem('token')
document.getElementById('history').addEventListener('load', getUserOrders());

function getUserOrders() {
    fetch(orderUrl, {
            headers: { 'Authorization': `Bearer ${token}` }
        })
        .then(response => response.json())
        .then(res => {
            console.log(res)
            console.log(res.message)
            let orders = ''
            if (res.message === 'Your order history has been returned') {
                myOrders = res.Orders
                for (let i in myOrders) {
                    orders += `
                <table>
                <tr>
                    <th>Order(Id)</th>
                    <th>Date</th>
                    <th>Food(Id)</th>
                    <th>Location</th>
                    <th>Status</th>
                </tr>
            <tr class="order">
                <td>${myOrders[i].order_id}</td>
                <td>${myOrders[i].date}</td>
                <td>${myOrders[i].menu_id}</td>
                <td>${myOrders[i].location}</td>
                <td>${myOrders[i].status}</td>
               
            </tr>`;
                    document.getElementById('history').innerHTML = orders;
                }
            } else if (res.message === 'You have no order history!') {
                orders = `<p>${res.message}<p>`
                document.getElementById('history').innerHTML = orders;
            }
        })
        .catch(err => console.log(err))

}