(function (){
    const yearLabel = document.querySelector('.footer-year');
    const now = new Date();

    yearLabel.innerHTML = now.getFullYear();
})();