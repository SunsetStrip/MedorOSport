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
        let delta = Math.ceil(delay / n) * 2;
        console.log('delta =' + delta + '  ' + '')

        function countdownNumbers() {
            if (cpt < n - 250) {
                numbers.innerHTML = cpt += 10;
            } else {
                numbers.innerHTML = ++cpt;
            }
            if (cpt < n) {
                setTimeout(countdownNumbers, delta);
            }
        }

        document.addEventListener('scroll', function () {
            sectionCounter++;
            if (sectionCounter == 1) {
                countdownNumbers();
            }
        }), { passive: true };
    }
    incrementNumber("number1", 2871);
    incrementNumber("number2", 644);
})();