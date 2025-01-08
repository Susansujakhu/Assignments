const display = document.getElementById('display');

// Append value to the display
function appendValue(value) {
  display.value += value;
}

// Clear the display
function clearDisplay() {
  display.value = '';
}

// Calculate the result
function calculate() {
  try {
    display.value = eval(display.value.replace('x', '*'));
  } catch (error) {
    display.value = 'Error';
  }
}
