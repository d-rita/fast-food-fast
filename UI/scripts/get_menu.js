let url = 'http://127.0.0.1:5000/api/v1/menu';
document.getElementById('menu-items').addEventListener('load', getMenu());

function getMenu() {
    fetch(url)
        .then(response => response.json())
        .then(res => {
            console.log(res)
            console.log(res.message)
            let menus = ''
            if (res.message === 'Menu successfully returned') {
                myMenu = res.Menu
                console.log(myMenu)
                for (let x in myMenu) {
                    console.log(myMenu[x])
                    menus += `
                    <table>
                    <tr>
                        <th>Food_ID</th>
                        <th>Food</th>
                        <th>Price</th>
                    </tr>
                        <tr>
                            <td>${myMenu[x].menu_id}</td>
                            <td>${myMenu[x].food_name}</td>
                            <td>${myMenu[x].food_price}</td>
                            <td><button  id="add-btn" value="${myMenu[x].menu_id}" onClick="selectFood()">Add</button>
                        </tr>
                    </table> `;
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