/* =========================
   MOBILE MENU
========================= */
function toggleMenu() {
  document.getElementById("navMenu")?.classList.toggle("show");
}

/* =========================
   SCROLL ANIMATIONS
========================= */
const observer = new IntersectionObserver(entries => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add("visible");
    }
  });
}, { threshold: 0.15 });

document.querySelectorAll(".animate").forEach(el => observer.observe(el));

/* =========================
   FILM SUBMISSION FORM
========================= */
const filmForm = document.getElementById("filmForm");

if (filmForm) {
  filmForm.addEventListener("submit", async (e) => {
    e.preventDefault();

    const data = {
      title: filmForm.title.value,
      director: filmForm.director.value,
      age_group: filmForm.age_group.value,
      link: filmForm.link.value
    };

    await fetch("http://127.0.0.1:8000/submit-film", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(data)
    });

    alert("Film Submitted Successfully");
    filmForm.reset();
  });
}

/* =========================
   REGISTRATION FORM
========================= */
const registerForm = document.getElementById("registerForm");

if (registerForm) {
  registerForm.addEventListener("submit", async (e) => {
    e.preventDefault();

    const data = {
      name: registerForm.name.value,
      email: registerForm.email.value,
      role: registerForm.role.value
    };

    await fetch("http://127.0.0.1:8000/register", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(data)
    });

    alert("Registration Successful");
    registerForm.reset();
  });
}
