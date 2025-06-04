let list = document.querySelectorAll(".list .item");
list.forEach((item) => {
  item.addEventListener("click", function (event) {
    if (event.target.classList.contains("add")) {
    }
  });
});
