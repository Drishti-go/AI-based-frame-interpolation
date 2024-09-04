document.getElementById('generate-video').addEventListener('click', function () {
  const frame1 = document.getElementById('frame1').files[0];
  const frame2 = document.getElementById('frame2').files[0];
  const dropdownValue = document.getElementById('num-frames').value;
  const generateButton = document.getElementById('generate-video');

  if (!frame1 || !frame2) {
    alert('Please upload both frames.');
    return;
  }

  // Disable the button and show loading text
  generateButton.disabled = true;
  generateButton.textContent = 'Generating...';

  // Create FormData object
  const formData = new FormData();
  formData.append('frame1', frame1);
  formData.append('frame2', frame2);
  formData.append('dropdown', dropdownValue);

  fetch('http://127.0.0.1:5000/upload', {
    method: 'POST',
    body: formData
  })
    .then(response => {
      if (!response.ok) {
        throw new Error(`Server error: ${response.status} ${response.statusText}`);
      }
      return response.json();
    })
    .then(data => {
      console.log('Success:', data);
      alert('Files uploaded successfully!');

      const videoPlayer = document.getElementById("video-player");
      videoPlayer.playbackRate = 0.25;
      videoPlayer.src = "result.mp4"; // Ensure this path is correct
      videoPlayer.play();

      // Re-enable the button and reset text
      generateButton.disabled = false;
      generateButton.textContent = 'Generate Video';
    })
    .catch((error) => {
      console.error('Error:', error);
      alert(`Failed to upload files. ${error.message}`);

      // Re-enable the button and reset text
      generateButton.disabled = false;
      generateButton.textContent = 'Generate Video';
    });
});
