function alertFunction() {
    alert("Вы попали в болото!");
}

function showButton() {
    const button = document.getElementById("click_me");

    if (button.style.display == "none") {
        button.style.display = "block";
    } else {
        button.style.display = "none";
    }
}

function changeBackground() {
    const currentColor = document.body.style.backgroundColor;
    if (currentColor == "red") {
        document.body.style.backgroundColor = "white";
    } else {
        document.body.style.backgroundColor = "red";
    }
}

function backToMap() {
	window.location.href='index.html';
}

