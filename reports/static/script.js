/* Toggle between showing and hiding the navigation menu links when the user clicks on the hamburger menu / bar icon */
document.addEventListener("DOMContentLoaded", (event) => {
    var menuToggle = document.querySelector(".burger");
    var menu = document.querySelector('nav ul');

    menuToggle.addEventListener('click', () => {
        let isVisible = menu.style.display === 'grid';
        menu.style.display = isVisible ? 'none' : 'grid';
    });

    // Ensure the menu resets correctly on window resize
    window.addEventListener('resize', () => {
        if (window.innerWidth >= 640) {
            menu.style.display = 'block';
        } else {
            menu.style.display = 'none';
        }
    });
});