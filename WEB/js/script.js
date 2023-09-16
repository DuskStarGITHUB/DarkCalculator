// AÑO DE FOOTER AUTOMATICO
const currentYearElement = document.getElementById("currentYear");

const currentYear = new Date().getFullYear();

currentYearElement.textContent = currentYear;

// SMOOTH SCROLL
const navbarLinks = document.querySelectorAll(".navbar a");

for (const link of navbarLinks) {
  link.addEventListener("click", smoothScroll);
}

function smoothScroll(event) {
  event.preventDefault();
  const targetId = this.getAttribute("href");
  const targetPosition = document.querySelector(targetId).offsetTop;
  const startPosition = window.pageYOffset;
  const distance = targetPosition - startPosition;
  const duration = 1000; // Duración en milisegundos

  let start = null;
  function step(timestamp) {
    if (!start) start = timestamp;
    const progress = timestamp - start;
    window.scrollTo(
      0,
      easeInOutCubic(progress, startPosition, distance, duration)
    );
    if (progress < duration) window.requestAnimationFrame(step);
  }

  window.requestAnimationFrame(step);
}

// Función de interpolación para el desplazamiento suave
function easeInOutCubic(t, b, c, d) {
  t /= d / 2;
  if (t < 1) return (c / 2) * t * t * t + b;
  t -= 2;
  return (c / 2) * (t * t * t + 2) + b;
}
