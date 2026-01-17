// Film Submission
const filmForm = document.getElementById("filmForm");
if (filmForm) {
  filmForm.addEventListener("submit", async (e) => {
    e.preventDefault();
    const data = {
      title: title.value,
      director: director.value,
      age_group: age_group.value,
      link: link.value
    };
    await fetch("http://127.0.0.1:8000/submit-film", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(data)
    });
    alert("Film Submitted Successfully");
  });
}

// Registration
const registerForm = document.getElementById("registerForm");
if (registerForm) {
  registerForm.addEventListener("submit", async (e) => {
    e.preventDefault();
    const data = {
      name: name.value,
      email: email.value,
      role: role.value
    };
    await fetch("http://127.0.0.1:8000/register", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(data)
    });
    alert("Registration Successful");
  });
}
