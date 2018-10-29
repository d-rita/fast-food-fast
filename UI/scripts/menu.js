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
            if (res.message === '') {
                output = `
                <tr>
                    <th>Food_ID</th>
                    <th>Food</th>
                    <th>Price</th>
                </tr>
                `
                for (let x in res) {
                    output = `
                    <tr>
                        <td>${res[x].menu_id}</td>
                        <td>${res[x].food_name}</td>
                        <td>${res[x].food_price}</td>
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