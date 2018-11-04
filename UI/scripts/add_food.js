let url = 'https://diana-fast-food-fast.herokuapp.com/api/v1/menu';
document.getElementById('add-food').addEventListener('submit', addFood);
token = localStorage.getItem('token')

function addFood(e) {
    e.preventDefault();

    let name = document.getElementById('name').value;
    console.log(name)
    let price = document.getElementById('price').value;
    console.log(price)

    let newFood = {
        name: name,
        price: price
    }

    fetch(url, {
            method: 'POST',
            headers: {
                'Accept': 'application/json, text/plain, */*',
                'Content-type': 'application/json',
                'Authorization': `Bearer ${token}`
            },
            mode: "cors",
            body: JSON.stringify(newFood)
        })
        .then(response => response.json())
        .then(res => {
            let output = `
                  <tr>
                    <td>${newFood['name']}</td>
                   <td>${newFood['price']}</td>
                </tr>`;
            console.log(res.message)
            if (res.message === 'Food successfully added!') {
                alert(`You have added ${newFood['name']} to the menu`);
                document.getElementById('menus').innerHTML = output;
            } else {
                alert(res.message)
                console.log(res.message)
            }

        })
        .catch(err => console.log(err))

}

let menuUrl = 'https://diana-fast-food-fast.herokuapp.com/api/v1/menu';
document.getElementById('menus').addEventListener('load', getMenu());

function getMenu() {
    fetch(menuUrl)
        .then(response => response.json())
        .then(res => {
            console.log(res)
            console.log(res.message)
            let menus = ''
            if (res.message === 'Menu successfully returned') {
                myMenu = res.Menu
                console.log(myMenu)
                for (let x in myMenu) {
                    menus += `
                    <table>
                    <tr>
                        <th>Food</th>
                        <th>Price</th>
                    </tr>
                        <tr>
                        <td>${myMenu[x].menu_id}</td>
                            <td>${myMenu[x].food_name}</td>
                            <td>${myMenu[x].food_price}</td>
                        </tr>
                    </table> `;
                }
                document.getElementById('menus').innerHTML = menus;


            } else if (res.message === 'There is no menu') {
                let noMenus = `<p>There is no menu available<p>`
                document.getElementById('menus').innerHTML = noMenus;
            }
        })
        .catch(err => console.log(err))

}