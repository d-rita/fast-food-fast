let url = 'https://diana-fast-food-fast.herokuapp.com/api/v1/menu';
document.getElementById('add-food').addEventListener('submit', addFood);
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
            if (res.message === 'Food successfully added!') {
                alert(`You have added ${newFood['name']} to the menu`);
            } else {
                console.log(res.message)
            }

        })
        .catch(err => console.log(err))

}