// COUNTDOWN
let count = 3;
const countdownEl = document.getElementById("countdown");
const mainContent = document.getElementById("main-content");

const timer = setInterval(() => {
    countdownEl.textContent = count;
    count--;

    if (count < 0) {
        clearInterval(timer);
        countdownEl.style.display = "none";
        mainContent.classList.remove("hidden");
        startTextSequence();
        startFallingHearts();
    }
}, 1000);

// TEXT SEQUENCE
const texts = [
    "You are",
    "My love",
    "My heart",
    "My everything ❤️"
];

function startTextSequence() {
    const textBox = document.getElementById("text-seq");

    let i = 0;
    function next() {
        if (i < texts.length) {
            textBox.textContent = texts[i];
            i++;
            setTimeout(next, 1200);
        } else {
            textBox.textContent = "";
        }
    }
    next();
}

// FALLING HEARTS
function startFallingHearts() {
    const container = document.getElementById("falling-hearts");

    setInterval(() => {
        const heart = document.createElement("div");
        heart.classList.add("falling-heart");
        heart.textContent = "💗";
        heart.style.left = Math.random() * 100 + "vw";
        heart.style.fontSize = 20 + Math.random() * 30 + "px";
        heart.style.animationDuration = 2 + Math.random() * 3 + "s";

        container.appendChild(heart);

        setTimeout(() => {
            heart.remove();
        }, 5000);
    }, 200);
}