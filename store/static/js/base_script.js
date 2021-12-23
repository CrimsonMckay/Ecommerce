window.addEventListener("load", () => {
    document.body.classList.remove("preload");
});

document.addEventListener("DOMContentLoaded", () => {
    const nav = document.querySelector(".nav");
    const sidenav = document.querySelector(".right-sidebar");

    document.querySelector("#btnNav").addEventListener("click", () => {
        nav.classList.add("nav--open");
    });


    document.querySelector(".container-wrapper").addEventListener("click", () => {
        nav.classList.remove("nav--open");
    });
    document.querySelector(".cart-close-button").addEventListener("click", () => {
        nav.classList.remove("nav--open");
    });


});