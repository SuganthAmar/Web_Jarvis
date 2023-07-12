const startBtn = document.querySelector("#start");
const stopBtn = document.querySelector("#stop");
const speakBtn = document.querySelector("#speak");
// speech recognition setup
const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
const recognition = new SpeechRecognition();
// sr start
recognition.onstart = function () {
    console.log("vr active");
};
// sr stop
recognition.onend = function () {
    console.log("vr deactive");
};
recognition.onresult = function (event) {
    let current = event.resultIndex;
    let transcript = event.results[current][0].transcript;
    console.log (transcript);
};
recognition.continuous = true;
startBtn.addEventListener("click", ()=>{
    recognition.start();
});
stopBtn.addEventListener("click", ()=>{
    recognition.stop();
});

function readOut(message) {
    const speech = new SpeechSynthesisUtterance();
    // different voices
    const allVoices = speechSynthesis.getVoices();
    speech.text = message;
    speech.voice = allVoices[6];
    speech.volume = 1;
    window.speechSynthesis.speak(speech);
    console.log("speaking out");
}
    // example
    speakBtn.addEventListener("click", () => {
    readOut("hello, my dear enthusiastic devs on the planet");
    });