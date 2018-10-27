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
            let orders = `
        <tr class="order-list">
            <th>Order_ID.</th>
            <th>Food_ID</th>
            <th>Date</th>
            <th>User_ID</th>
            <th>Location</th>
            <th>Order Status</th>
        </tr>`
            for (let i in res) {
                console.log(res[i].item);
                output += `
            <tr class="order">
                <td>${res[i].order_id}</td>
                <td>${res[i].menu_id}</td>
                <td>${res[i].date}</td>
                <td>${res[i].user_id}</td>
                <td>${res[i]._location}</td>
                <td>${res[i].order_status}</td>
               
            </tr>`;
            }
            document.getElementById('order-list').innerHTML = orders;
        })
}