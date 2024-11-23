// Add a welcome message when the page loads
window.addEventListener("DOMContentLoaded", () => {
  const chatBox = document.getElementById("chat-box");
  chatBox.innerHTML += `<p style="background-color: rgb(247, 244, 244); padding: 5px !important; border-radius: 10px;"><strong>Bot:</strong> Hey! Are you looking for help?</p>`;
});

document.getElementById("send-icon").addEventListener("click", async () => {
  const userInput = document.getElementById("user-input").value;
  const chatBox = document.getElementById("chat-box");

  if (userInput.trim()) {
    chatBox.innerHTML += `<p style="padding: 5px !important; margin:3px 0px !important; border-radius: 10px;"><strong>You:</strong> ${userInput}</p>`;
    try {
      const response = await fetch("/api/chatbot/ask", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ question: userInput }),
      });
      if (response.ok) {
        const data = await response.json();
        chatBox.innerHTML += `<p style="background-color: rgb(247, 244, 244); padding: 5px !important; border-radius: 10px;"><strong>Bot:</strong> ${
          data.answer || "Sorry, something went wrong!"
        }</p>`;
      } else {
        chatBox.innerHTML += `<p style="background-color: rgb(247, 244, 244); padding: 5px !important; border-radius: 10px;"><strong>Bot:</strong> Sorry, the server returned an error.</p>`;
      }
    } catch (error) {
      chatBox.innerHTML += `<p style="background-color: rgb(247, 244, 244); padding: 5px !important; border-radius: 10px;"><strong>Bot:</strong> Sorry, something went wrong!</p>`;
    }
    document.getElementById("user-input").value = "";
    chatBox.scrollTop = chatBox.scrollHeight;
  }
});
