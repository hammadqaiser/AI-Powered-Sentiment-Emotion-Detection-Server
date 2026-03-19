const RunEmotionDetection = ()=> {
    let textToAnalyze = document.getElementById("textToAnalyze").value;

    let xhttp = new XMLHttpRequest();

    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            document.getElementById("system_response").innerHTML = this.responseText;
        }
    };

    xhttp.onerror = function() {
        document.getElementById("system_response").innerHTML = "Error: Unable to reach server.";
    };    

    xhttp.open("GET", "emotionDetector?textToAnalyze=" + encodeURIComponent(textToAnalyze), true);
    xhttp.send();
};
