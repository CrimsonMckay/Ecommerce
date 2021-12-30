window.addEventListener("load", () => {
    document.body.classList.remove("preload");
});

document.addEventListener("DOMContentLoaded", () => {
    const nav = document.querySelector(".nav");

    document.querySelector("#btnNav").addEventListener("click", () => {
        nav.classList.add("nav--open");
    });


    document.querySelector(".cart-close-button").addEventListener("click", () => {
        nav.classList.remove("nav--open");
    });
});