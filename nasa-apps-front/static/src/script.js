document.getElementById('uploadButton').addEventListener('click', async () => {
    const fileInput = document.getElementById('fileInput');
    const file = fileInput.files[0];

    if (!file) {
        alert('Please select a CSV file to upload.');
        return;
    }

    // Create FormData object
    const formData = new FormData();
    formData.append('file', file);

    try {
        const response = await fetch('http://nasa.thebayre.com:5000/seismic_detection', {
            method: 'POST', // Ensure this matches your backend's expected method
            body: formData,
        });

        if (!response.ok) {
            throw new Error('Network response was not ok: ' + response.statusText);
        }

        // Assuming the response contains a URL to the image
        const result = await response.json();

        // Check if the image URL is present in the response
        if (result.imageUrl) {
            const imgElement = document.getElementById('resultImage');
            imgElement.src = result.imageUrl; // Set the image source
            imgElement.style.display = 'block'; // Make the image visible
        } else {
            console.error('Image URL not found in response:', result);
        }
    } catch (error) {
        console.error('Error:', error);
    }
});
