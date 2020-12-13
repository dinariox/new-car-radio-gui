document.addEventListener("DOMContentLoaded", () => {
	document.getElementById("home-button").addEventListener("click", (e) => {
		window.location = "index.html";
	});

	const btn_ta = document.getElementById("btn-ta");
	btn_ta.addEventListener("click", (e) => {
		if (btn_ta.classList.contains("enabled")) {
			btn_ta.classList.remove("enabled");
		} else {
			btn_ta.classList.add("enabled");
		}
	});
});
