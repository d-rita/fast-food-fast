let order_id = document.getElementById('searchId').value;
console.log(order_id)
    //document.getElementById('order-search').addEventListener('submit', getOneOrder())

function getOneOrder() {



    let orderUrl = 'http://127.0.0.1:5000/api/v1/orders/' + order_id;


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
                    <td>${ares.Order.location}</td>
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