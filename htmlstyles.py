claude = """:root {
  --primary: #2c3e50;
  --secondary: #3498db;
  --success: #27ae60;
  --background: #f5f6fa;
  --text: #2c3e50;
  --border: #dcdde1;
  --shadow: rgba(0, 0, 0, 0.1);
}

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: 'Segoe UI', system-ui, -apple-system, sans-serif;
}

body {
  background: var(--background);
  color: var(--text);
  line-height: 1.6;
  padding: 2rem;
  max-width: 1200px;
  margin: 0 auto;
}

h1 {
  color: var(--primary);
  margin: 2rem 0 1.5rem;
  padding-bottom: 0.5rem;
  border-bottom: 2px solid var(--secondary);
  font-weight: 600;
}

form {
  background: white;
  padding: 2rem;
  border-radius: 10px;
  box-shadow: 0 4px 6px var(--shadow);
  margin-bottom: 2rem;
}

label {
  display: block;
  margin-bottom: 0.5rem;
  color: var(--primary);
  font-weight: 500;
}

input, select {
  width: 100%;
  padding: 0.8rem;
  margin-bottom: 1rem;
  border: 1px solid var(--border);
  border-radius: 5px;
  font-size: 1rem;
  transition: border-color 0.3s ease;
}

input:focus, select:focus {
  outline: none;
  border-color: var(--secondary);
  box-shadow: 0 0 0 3px rgba(52, 152, 219, 0.1);
}

button {
  background: var(--secondary);
  color: white;
  padding: 0.8rem 2rem;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-size: 1rem;
  font-weight: 500;
  transition: background-color 0.3s ease;
}

button:hover {
  background: #2980b9;
}

/* Database display styling */
ul {
  list-style: none;
  background: white;
  padding: 1rem;
  border-radius: 5px;
  box-shadow: 0 2px 4px var(--shadow);
  margin-bottom: 1rem;
}

li {
  padding: 0.5rem 0;
  border-bottom: 1px solid var(--border);
}

li:last-child {
  border-bottom: none;
}

/* Responsive Design */
@media (max-width: 768px) {
  body {
    padding: 1rem;
  }
  
  form {
    padding: 1rem;
  }
  
  button {
    width: 100%;
  }
}

/* Animation */
@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

form {
  animation: fadeIn 0.5s ease-out;
}

/* Custom select styling */
select {
  appearance: none;
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='%232c3e50' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpolyline points='6 9 12 15 18 9'%3E%3C/polyline%3E%3C/svg%3E");
  background-repeat: no-repeat;
  background-position: right 1rem center;
  background-size: 1em;
}

/* Additional form group spacing */
.form-group {
  margin-bottom: 1.5rem;
}

/* Success message styling */
.success-message {
  background: var(--success);
  color: white;
  padding: 1rem;
  border-radius: 5px;
  margin-bottom: 1rem;
  animation: fadeIn 0.5s ease-out;
}

/* Error message styling */
.error-message {
  background: #e74c3c;
  color: white;
  padding: 1rem;
  border-radius: 5px;
  margin-bottom: 1rem;
  animation: fadeIn 0.5s ease-out;
}

/* Database JSON display */
pre {
  background: white;
  padding: 1rem;
  border-radius: 5px;
  box-shadow: 0 2px 4px var(--shadow);
  overflow-x: auto;
  margin-bottom: 2rem;
  font-family: 'Consolas', monospace;
  font-size: 0.9rem;
}

/* Grid layout for larger screens */
@media (min-width: 1024px) {
  .forms-container {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 2rem;
  }
}
"""
gpt4 = """
/* General Reset */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

/* Body Styling */
body {
    font-family: 'Arial', sans-serif;
    background-color: #f4f7f6;
    color: #333;
    padding: 20px;
    line-height: 1.6;
}

h1 {
    color: #2c3e50;
    font-size: 2em;
    margin-bottom: 20px;
}

h3 {
    color: #34495e;
    font-size: 1.5em;
    margin-top: 20px;
    margin-bottom: 10px;
}

/* Form Styling */
form {
    background-color: #ffffff;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    margin-bottom: 30px;
}

label {
    font-size: 1.1em;
    color: #34495e;
}

input, select {
    width: 100%;
    padding: 10px;
    margin: 10px 0 20px;
    border: 1px solid #ccc;
    border-radius: 4px;
    font-size: 1em;
}

input[type="text"],
input[type="tel"],
input[type="datetime-local"] {
    font-family: 'Arial', sans-serif;
}

button {
    background-color: #3498db;
    color: white;
    border: none;
    padding: 12px 20px;
    font-size: 1.2em;
    border-radius: 5px;
    cursor: pointer;
    transition: background-color 0.3s ease;
}

button:hover {
    background-color: #2980b9;
}

/* Responsive Styles */
@media (max-width: 768px) {
    body {
        padding: 10px;
    }

    form {
        padding: 15px;
    }

    button {
        width: 100%;
    }
}

/* Database Table and List Styling */
ul {
    list-style-type: none;
    padding-left: 0;
}

li {
    margin-bottom: 10px;
    font-size: 1.1em;
}

ul li:before {
    content: "• ";
    color: #3498db;
    margin-right: 5px;
}

h2 {
    margin-top: 50px;
    font-size: 2.5em;
    text-align: center;
    color: #3498db;
}

.database-container {
    margin-top: 30px;
    padding: 20px;
    background-color: #ffffff;
    border-radius: 8px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.database-content {
    display: flex;
    justify-content: space-between;
    margin-bottom: 20px;
}

.database-section {
    flex: 1;
    margin-right: 20px;
}

.database-section:last-child {
    margin-right: 0;
}

/* Option Styling */
option {
    padding: 10px;
    font-size: 1.1em;
}
"""