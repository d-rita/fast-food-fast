let url = 'http://127.0.0.1:5000/api/v1/menu';
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