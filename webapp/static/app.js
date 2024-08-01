document.getElementById('segmentation-form').addEventListener('submit', function(e) {
    e.preventDefault();
    const fileInput = document.getElementById('file-input');
    const formData = new FormData();
    formData.append('file', fileInput.files[0]);

    fetch('/segment', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        // Display results
        const resultsDiv = document.getElementById('results');
        resultsDiv.innerHTML = JSON.stringify(data, null, 2);
    })
    .catch(error => console.error('Error:', error));
});
