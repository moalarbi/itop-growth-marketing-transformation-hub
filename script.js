const revealItems = document.querySelectorAll(".reveal");
const observer = new IntersectionObserver((entries) => {
  entries.forEach((entry) => {
    if (entry.isIntersecting) {
      entry.target.classList.add("is-visible");
      observer.unobserve(entry.target);
    }
  });
}, { threshold: 0.12 });
revealItems.forEach((item) => observer.observe(item));

document.querySelectorAll('a[href$=".html"], a[href^="../index"], a[href^="pages/"]').forEach((link) => {
  if (link.target) return;
  link.addEventListener("click", (event) => {
    const href = link.getAttribute("href");
    if (!href || href.startsWith("#")) return;
    event.preventDefault();
    document.body.classList.add("is-leaving");
    window.setTimeout(() => { window.location.href = href; }, 120);
  });
});

document.addEventListener("keydown", (event) => {
  if (event.key !== "Escape") return;
  const back = document.querySelector(".back-link");
  if (back) window.location.href = back.href;
});