document.getElementById("chatbot-toggle").addEventListener("click", function() {
    document.getElementById("chatbot-window").classList.remove("d-none");
});

document.getElementById("chatbot-close").addEventListener("click", function() {
    document.getElementById("chatbot-window").classList.add("d-none");
});

document.getElementById("chatbot-send").addEventListener("click", function() {
    const input = document.getElementById("chatbot-input");
    const message = input.value.trim();
    if (message !== "") {
        const msgDiv = document.createElement("div");
        msgDiv.className = "chatbot-message";
        msgDiv.textContent = message;
        document.getElementById("chatbot-body").appendChild(msgDiv);
        input.value = "";
        // You can now call your AI backend here to get a response and append it
    }
});
