document.addEventListener("DOMContentLoaded", function () {
    const toggleButton = document.querySelector(".navbar-toggle");
    const navbarNav = document.querySelector(".navbar-nav");
    const navLinks = document.querySelectorAll(".navbar-nav a");

    // Toggle navigation menu
    toggleButton.addEventListener("click", function () {
        navbarNav.classList.toggle("active");
    });

    // Close navigation menu when a link is clicked
    navLinks.forEach(link => {
        link.addEventListener("click", function () {
            navbarNav.classList.remove("active");
        });
    });
});