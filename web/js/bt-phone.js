document.addEventListener("DOMContentLoaded", () => {
	document.getElementById("home-button").addEventListener("click", (e) => {
		window.location = "index.html";
	});

	for (let i = 0; i < 10; i++) {
		document.getElementById("btn-dial-" + i).addEventListener("click", (e) => {
			addDialNumber(i);
		});
	}

	document.getElementById("btn-dial-+").addEventListener("click", (e) => {
		addDialNumber("+");
	});

	document.getElementById("btn-clear").addEventListener("click", clearDialedNumber);

	document.getElementById("btn-delete").addEventListener("click", deleteDialNumber);
});

dialedNumber = "";

function addDialNumber(number) {
	if (number == "+" && dialedNumber.length > 0) return; // + nur an erster Stelle
	dialedNumber += number;
	showDialedNumber();
}

function deleteDialNumber() {
	dialedNumber = dialedNumber.slice(0, -1);
	showDialedNumber();
}

function clearDialedNumber() {
	dialedNumber = "";
	showDialedNumber();
}

function showDialedNumber() {
	document.getElementById("number").innerHTML = dialedNumber;
}
