document.addEventListener("DOMContentLoaded", function() {
    const textElement = document.getElementById("typewriter-text");
    const text = textElement.textContent;
    textElement.textContent = "";

    let index = 0;
    function typeWriter() {
        if (index < text.length) {
            textElement.innerHTML += text.charAt(index);
            index++;
            setTimeout(typeWriter, 1);
        }
    }

    typeWriter();
});
