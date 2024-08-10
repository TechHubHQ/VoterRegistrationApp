document.addEventListener("DOMContentLoaded", () => {
  const loginForm = document.querySelector("form");
  const fields = {
    username: document.getElementById("username"),
    password: document.getElementById("password"),
  };
  const passwordError = document.getElementById("password-error");

  loginForm.addEventListener("submit", async (event) => {
    event.preventDefault();

    const formData = Object.fromEntries(
      Object.entries(fields).map(([key, field]) => [key, field.value.trim()])
    );

    if (formData.password === "") {
      passwordError.classList.remove("hidden");
      return;
    }
    passwordError.classList.add("hidden");

    try {
      const response = await fetch("/api/login", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(formData),
      });

      const data = await response.json();
      console.log(data);

      if (data.success) {
        window.location.href = "/dashboard";
      } else {
        alert(`Login failed: ${data.message}`);
      }
    } catch (error) {
      console.error("Error:", error);
      alert("An error occurred. Please try again.");
    }
  });
});
