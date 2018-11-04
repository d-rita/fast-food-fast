let url = 'http://127.0.0.1:5000/api/v1/orders';
document.getElementById('order-list').addEventListener('load', getAllOrders());

function getAllOrders() {
    token = localStorage.getItem('token')
    fetch(url, {
            headers: {
                'Authorization': `Bearer ${token}`
            }
        })
        .then(response => response.json())
        .then(res => {
            let orders = ''
            if (res.message === 'All orders are returned!') {
                allOrders = res.Orders
                for (let i in allOrders) {
                    console.log(allOrders[i])
                    orders += `
                    <table>
        <tr>
            <th>Order(Id)</th>
            <th>Food(Id)</th>
            <th>Date</th>
            <th>User(Id)</th>
            <th>Location</th>
            <th>Order Status</th>
        </tr> 
        <tr>
            <td>${allOrders[i].order_id}</td>
            <td>${allOrders[i].menu_id}</td>
            <td>${allOrders[i].date}</td>
            <td>${allOrders[i].user_id}</td>
            <td>${allOrders[i].location}</td>
            <td>${allOrders[i].status}</td>
        </tr>
        </table>`;
                    document.getElementById('order-list').innerHTML = orders;
                }

            } else {
                alert(res.message)
                let noOrders = `<p>${res.message}</p>`
                document.getElementById('order-list').innerHTML = noOrders;
            }

        })
        .catch(err => console.log(err))
}