document.getElementById("chat-toggle").addEventListener("click", function () {
  const chatContainer = document.getElementById("chat-container");
  chatContainer.style.display =
    chatContainer.style.display === "none" || chatContainer.style.display === ""
      ? "flex"
      : "none";

  setTimeout(() => {
    chatContainer.classList.toggle("visible");
  }, 10);
});

function navigate(section) {
  const sections = {
    home: document.querySelector(".main"),
    shopping: document.querySelector(".shopping"),
    about: document.querySelector(".about"),
    contact: document.querySelector(".contact"),
  };

  Object.values(sections).forEach((sec) => (sec.style.display = "none"));
  sections[section].style.display = "block";
  const targetSection = sections[section];
  targetSection.style.display = "flex";
}

document.addEventListener("DOMContentLoaded", function () {
  navigate("home");
});

function showProduct(image) {
  alert("Product details will be shown here.");
}

document
  .getElementById("contactForm")
  .addEventListener("submit", function (event) {
    event.preventDefault();
    alert("Thank you for connecting with us!");
  });
