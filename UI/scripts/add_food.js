let url = 'https://diana-fast-food-fast.herokuapp.com/api/v1/menu';
document.getElementById('add-food').addEventListener('submit', addFood);
token = localStorage.getItem('token')

function addFood(e) {
    e.preventDefault();

    let food_name = document.getElementById('food_name').value;
    console.log(food_name)
    let price = document.getElementById('price').value;
    console.log(price)

    let formData = new FormData('add-food');
    formData.append('name', food_name);
    formData.append('price', price);
    console.log(formData)


    fetch(url, {
            method: 'POST',
            headers: { 'Authorization': `Bearer ${token}` },
            mode: "cors",
            body: formData
                // body: JSON.stringify(body)
        })
        .then(response => response.json())
        .then(res => {
            let output = `
              <tr>
                <td>${formData['name']}</td>
               <td>${formData['price']}</td>
            </tr>`;
            console.log(res.message)
            if (res.message === 'Food successfully added!') {
                alert(`You have added ${body['name']} to the menu`);
                document.getElementById('menus').innerHTML = output;
            } else {
                alert(res.message)
                console.log(res.message)
            }

        })
        .catch(err => console.log(err))

}