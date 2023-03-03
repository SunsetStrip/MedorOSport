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


(function () {
    function incrementNumber(node, nb) {

        let sectionNumbers = document.querySelector('.sectionNumbers');
        if (!sectionNumbers) return;
        let sectionCounter = 0;
        let numbers = document.querySelector("." + node);

        let n = nb;
        let cpt = 0;
        let delay = 1000;
        let delta = Math.ceil((delay * 15000) / n);

        function countdownNumbers() {
            numbers.innerHTML = ++cpt;
            if (cpt < n) {
                setTimeout(countdownNumbers, numbers);
            }
        }

        document.addEventListener('scroll', function () {
            sectionCounter++;
            if (sectionCounter == 1) {
                setTimeout(countdownNumbers, numbers);
            }
        }), { passive: true };
    }
    setTimeout(function () {
        incrementNumber("number1", 2871);
        incrementNumber("number2", 644);
    }, 2000);
})();