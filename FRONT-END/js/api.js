window.addEventListener("load", fetch_api);
const MAIN_CONTENT = document.getElementsByClassName("main_content")

function fetch_api(){
    fetch('http://127.0.0.1:5000/api/food-stores/sales')
      .then((response) => response.json())
      .then((data) => console.log(data));
}
// cross-origin request blocked! :(