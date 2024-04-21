// script.
var paragraph = document.getElementById("search_results");

document.addEventListener('DOMContentLoaded', function() {
    console.log('Script loaded');

    fetch('http://127.0.0.1:5000/initialize', {
        method: 'POST',
        headers: {
            'Content-Type': 'text/plain'  // Set content type to text/csv
        } 
    })
    .then(response => response.json())
    .then(data => {
        console.log('initialized successfully:', data);
    })
    .catch(error => {
        console.error('Error connecting', error);
    });
});

function submit(){
    const csvValue = document.getElementById('description').value;
    console.log(csvValue);

        // Make an HTTP POST request to the Flask backend
    fetch('http://127.0.0.1:5000/send-csv', {
        method: 'POST',
        headers: {
            'Content-Type': 'text/csv'  // Set content type to text/csv
        },
        body: csvValue  // Directly send the CSV string
    })
    .then(response => response.json())  // Convert response to JSON
    .then(data => {
    console.log('Server response:', data);  // Log the server response
    })
    .catch(error => {
        console.error('Error sending CSV:', error);
    });

    fetch('http://127.0.0.1:5000/rec', {
        method: 'POST',
        mode: 'cors',
        headers: {
            'Content-Type': 'text/plain'  // Set content type to text/plain
        },
        body: 'your data here'  // Include your data here
    })
    .then(response => response.json())
    .then(data => {
        if (Array.isArray(data)) {
            paragraph.innerText = data.map(item => item.description).join('\n');
            console.log('Received data:', data);
        } else {
            console.error('Unexpected data format');
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });


}





