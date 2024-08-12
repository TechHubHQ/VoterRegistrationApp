document.getElementById('eligibilityForm').addEventListener('submit', function(e) {
  e.preventDefault();
  
  const age = parseInt(document.getElementById('age').value);
  const nationality = document.getElementById('nationality').value;
  const state = document.getElementById('state').value;
  const city = document.getElementById('city').value;
  
  let message = '';
  let isEligible = false;
  
  if (age >= 18 && nationality === 'US') {
    message = `Congratulations! You appear to be eligible to vote in ${city}, ${state}.`;
    isEligible = true;
  } else if (age < 18) {
    message = "Sorry, you must be at least 18 years old to be eligible to vote.";
  } else if (nationality !== 'US') {
    message = "Sorry, only U.S. citizens are eligible to vote in U.S. elections.";
  }
  
  const resultDiv = document.getElementById('eligibilityResult');
  resultDiv.textContent = message;
  resultDiv.className = `mt-4 p-4 rounded-md ${isEligible ? 'bg-green-100 text-green-700' : 'bg-red-100 text-red-700'}`;
  resultDiv.style.display = 'block';
});