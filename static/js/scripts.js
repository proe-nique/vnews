/*!
 * Start Bootstrap - Modern Business v5.0.5 (https://startbootstrap.com/template-overviews/modern-business)
 * Copyright 2013-2021 Start Bootstrap
 * Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-modern-business/blob/master/LICENSE)
 */
// This file is intentionally blank
// Use this file to add JavaScript to your project

const searchButton = document.getElementById('search-button');
const searchInput = document.getElementById('search-input');
searchButton.addEventListener('click', () => {
    const inputValue = searchInput.value;
    alert(inputValue);
});