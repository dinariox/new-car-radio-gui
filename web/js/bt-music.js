const playpauseIcon = document.getElementById("playpause-icon");

document.addEventListener("DOMContentLoaded", () => {
	document.getElementById("home-button").addEventListener("click", (e) => {
		window.location = "index.html";
	});

	document.getElementById("btn-playpause").addEventListener("click", (e) => {
		if (playpauseIcon.classList.contains("mdi-play")) {
			playpauseIcon.classList.remove("mdi-play");
			playpauseIcon.classList.add("mdi-pause");
			eel.btPlay();
		} else {
			playpauseIcon.classList.remove("mdi-pause");
			playpauseIcon.classList.add("mdi-play");
			eel.btPause();
		}
	});
});
