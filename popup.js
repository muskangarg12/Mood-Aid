var quote = document.getElementById("quote");
var author = document.getElementById("author");

var current_quote = {"current_id": 0};

document.getElementById("brighter").addEventListener("click", function() {
	var url = new URL("http://moodyquotes.pythonanywhere.com/");
	url.searchParams.set('brighter', current_quote.current_id);

	var xhttp = new XMLHttpRequest();
	xhttp.open('GET', url);
	xhttp.send();

	xhttp.onreadystatechange = function() {
	    if (this.readyState == 4 && this.status == 200) {
	       current_quote = JSON.parse(xhttp.responseText);
	       console.log(xhttp.responseText);

	       quote.innerHTML = current_quote.quote;
	       author.innerHTML = current_quote.author;
	    }
	};
});


document.getElementById("darker").addEventListener("click", function() {
	var url = new URL("http://127.0.0.1:5000/");
	url.searchParams.set('darker', current_quote.current_id);

	var xhttp = new XMLHttpRequest();
	xhttp.open('GET', url);
	xhttp.send();

	xhttp.onreadystatechange = function() {
	    if (this.readyState == 4 && this.status == 200) {
	       current_quote = JSON.parse(xhttp.responseText);
	       console.log(xhttp.responseText);

	       quote.innerHTML = current_quote.quote;
	       author.innerHTML = current_quote.author;
	    }
	};
})


document.onload = document.getElementById("brighter").click();