document.addEventListener("DOMContentLoaded", () => {
  const signupForm = document.querySelector("#signup_form");
  const fields = {
    username: document.getElementById("username"),
    password: document.getElementById("password"),
    state: document.getElementById("state"),
    city: document.getElementById("city"),
  };

  signupForm.addEventListener("submit", async (event) => {
    event.preventDefault();

    const formData = Object.fromEntries(
      Object.entries(fields).map(([key, field]) => [key, field.value.trim()])
    );

    const validations = {
      username: (value) => value !== "" || "Please enter a username",
      password: (value) =>
        value.length >= 8 || "Password must be at least 8 characters long",
      state: (value) => value !== "" || "Please enter a state",
      city: (value) => value !== "" || "Please choose a city",
    };

    for (const [field, validate] of Object.entries(validations)) {
      const message = validate(formData[field]);
      if (message === false) {
        alert("Form Vailidation Failed, check the fields");
        console.error(message);
        return;
      }
    }

    try {
      const response = await fetch("/api/signup", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(formData),
      });

      const data = await response.json();

      if (data.success) {
        window.location.href = "/dashboard";
      } else {
        alert(data.message);
        console.log(data.message);
      }
    } catch (error) {
      console.error("Error:", error);
      alert("An error occurred. Please try again.");
    }
  });
});
