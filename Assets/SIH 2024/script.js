document
  .getElementById("generate-video")
  .addEventListener("click", function () {
    const frame1 = document.getElementById("frame1").files[0];
    const frame2 = document.getElementById("frame2").files[0];
    const numFrames = document.getElementById("num-frames").value;

    if (!frame1 || !frame2) {
      alert("Please upload both frames.");
      return;
    }

    // Simulate video generation and display
    const videoPlayer = document.getElementById("video-player");
    videoPlayer.src = "https://www.w3schools.com/html/mov_bbb.mp4"; // Placeholder video URL
    videoPlayer.play();
  });
