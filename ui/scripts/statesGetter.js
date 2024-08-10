document.addEventListener("DOMContentLoaded", () => {
  const stateSelect = document.getElementById("state");
  const citySelect = document.getElementById("city");

  fetch("../../ui/scripts/json/us_states_cities.json")
    .then((response) => response.json())
    .then((data) => {
      const states = Object.keys(data.USA);
      states.forEach((state) => {
        const option = document.createElement("option");
        option.value = state;
        option.textContent = state;
        stateSelect.appendChild(option);
      });

      stateSelect.addEventListener("change", (event) => {
        const selectedState = event.target.value;
        const cities = data.USA[selectedState] || [];

        citySelect.innerHTML = '<option value="">Select your city</option>';
        cities.forEach((city) => {
          const option = document.createElement("option");
          option.value = city;
          option.textContent = city;
          citySelect.appendChild(option);
        });
      });
    })
    .catch((error) => console.error("Error loading JSON data:", error));
});
