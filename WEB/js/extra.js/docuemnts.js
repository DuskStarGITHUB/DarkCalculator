document.addEventListener("DOMContentLoaded", function () {
  const sections = document.querySelectorAll(".content section");
  const links = document.querySelectorAll(".sidebar li a");

  links.forEach((link, index) => {
    link.addEventListener("click", (e) => {
      e.preventDefault();

      if (link.parentElement.tagName === "LI") {
        sections.forEach((section) => {
          section.style.display = "none";
        });
        sections[index].style.display = "block";
      }
    });
  });
});
