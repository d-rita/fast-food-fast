document.getElementById('add-food').addEventListener('submit', addFood);
let url = 'https://diana-fast-food-fast.herokuapp.com/api/v1/menu';
token = localStorage.getItem('token')

function addFood(e) {
    e.preventDefault();

    let food_name = document.getElementById('food_name').value;
    let price = document.getElementById('price').value;

    let formData = new FormData();
    formData.append('name', food_name);
    formData.append('price', price);


    fetch(url, {
            method: 'POST',
            headers: { 'Authorization': `Bearer ${token}` },
            mode: "cors",
            body: formData
        })
        .then(response => response.json())
        .then(res => {
            output = ''
            output = `
              <tr>
                <td>${formData['name']}</td>
               <td>${formData['price']}</td>
            </tr>`;
            document.getElementById('menus').innerHTML = output;
            console.log(res.message)
                // if (res.message === 'Food successfully added!') {
                //     alert(`You have added ${newFood['name']} to the menu`);
                // } else {
                //     console.log(res.message)
                // }

        })
        .catch(err => console.log(err))

}

function getMenu() {
    fetch(url, { method: 'GET' })
        .then(response => response.json())
        .then(res => {
            console.log(res)
            output = ''
            if (res.message === 'Menu successfully returned') {
                output = `
                <tr>
                    <th>Food_ID</th>
                    <th>Food</th>
                    <th>Price</th>
                </tr>
                `
                let myMenu = res.Menu
                for (let x in myMenu) {
                    output = `
                    <tr>
                        <td>${myMenu[x].menu_id}</td>
                        <td>${myMenu[x].food_name}</td>
                        <td>${myMenu[x].food_price}</td>
                        <td><button id="add-btn" value="${myMenu[x].menu_id}" onClick="selectFood()">Add</button>
                    </tr>`;
                    document.getElementById('menu-items').innerHTML = output;
                }
            } else if (res.message === 'There is no menu') {
                output = `<p>There is no menu available<p>`
                document.getElementById('menu-items').innerHTML = output;
            }
        })
        .catch(err => console.log(err))

}

function selectFood() {
    let myFood = document.getElementById('add-btn').value
    document.getElementById('food_id').innerHTML = myFood;
}

document.getElementById('payform').addEventListener('submit', addOrder);
let orderUrl = 'https://diana-fast-food-fast.herokuapp.com/api/v1/user/order';

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