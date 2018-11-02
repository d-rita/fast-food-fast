let url = 'https://diana-fast-food-fast.herokuapp.com/api/v1/menu';
document.getElementById('menu-items').addEventListener('load', getMenu());

function getMenu() {
    fetch(url)
        .then(response => response.json())
        .then(res => {
            console.log(res)
            console.log(res.message)
            if (res.message === 'Menu successfully returned') {
                let menus = `
                <tr>
                    <th>Food_ID</th>
                    <th>Food</th>
                    <th>Price</th>
                </tr>
                `
                for (let x in res) {
                    menus = `
                    <tr>
                        <td>${res[x].menu_id}</td>
                        <td>${res[x].food_name}</td>
                        <td>${res[x].food_price}</td>
                        <td><button id="add-btn" value="${res[x].menu_id}" onClick="selectFood()">Add</button>
                    </tr>`;
                    document.getElementById('menu-items').innerHTML = menus;
                }
            } else if (res.message === 'There is no menu') {
                let noMenus = `<p>There is no menu available<p>`
                document.getElementById('menu-items').innerHTML = noMenus;
            }
        })
        .catch(err => console.log(err))

}

function selectFood() {
    let myFood = document.getElementById('add-btn').value
    document.getElementById('food_id').innerHTML = myFood;
}