let url = 'https://diana-fast-food-fast.herokuapp.com/api/v1/orders';
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
                    order_id += allOrders[i].order_id
                    localStorage.setItem('order_id', order_id)

                    orders += `
                    <table>
        <tr>
            <th>Order(Id)</th>
            <th>Food(Id)</th>
            <th>Date</th>
            <th>User(Id)</th>
            <th>Location</th>
            <th>Status</th>
            <th>Update</th>
        </tr> 
        <tr>
            <td>${allOrders[i].order_id}</td>
            <td>${allOrders[i].menu_id}</td>
            <td>${allOrders[i].date}</td>
            <td>${allOrders[i].user_id}</td>
            <td>${allOrders[i].location}</td>
            <td>${allOrders[i].status}</td>
            <td><select>
            <option value="Processing">Processing</option>
            <option value="Complete">Complete</option>
            <option value="Cancelled">Cancelled</option>
          </select></td>
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

let order_id = localStorage.getItem('order_id')
console.log(order_id)

function getSingleOrder(order_id) {
    let order_id = localStorage.getItem('order_id')
    console.log(order_id)


    let orderUrl = 'https://diana-fast-food-fast.herokuapp.com/api/v1/orders/' + order_id;
    window.location.replace('update_order.html')


    fetch(orderUrl, {
            headers: {
                'Authorization': `Bearer ${token}`
            }
        })
        .then(res => res.json())
        .then(response => {

            let oneOrder = ''
            console.log(response.message)
            if (response.message === 'One order has been returned') {
                oneOrder = `
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
                    <td>${res.Order.order_id}</td>
                    <td>${res.Order.menu_id}</td>
                    <td>${res.Order.date}</td>
                    <td>${res.Order.user_id}</td>
                    <td>${res.Order.location}</td>
                    <td>${res.Order.status}</td>
                </tr>
                </table>`;
                document.getElementById('results').innerHTML = oneOrder;
            } else {
                alert(response.message)
                console.log(response.message)
            }
        })
        .catch(err => console.log(err))
}