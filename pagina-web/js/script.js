// AÑO DE FOOTER AUTOMATICO
const currentYearElement = document.getElementById("currentYear");

const currentYear = new Date().getFullYear();

currentYearElement.textContent = currentYear;
