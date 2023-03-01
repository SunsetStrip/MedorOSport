function visible() {

    if (trigger == 0) {
        var menu = document.getElementById("menu");
        menu.classList.add("visible");
        trigger = 1;
    }

    else {
        var menu = document.getElementById("menu");
        menu.classList.remove("visible");
        trigger = 0;
    }

}

var trigger = 0;

var burger = document.getElementById("burger-menu");
burger.addEventListener("click", visible);
