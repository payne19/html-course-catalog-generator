document.addEventListener('DOMContentLoaded', () => {
  // 🌙 Default to dark mode
  document.body.classList.add('dark');

  const darkToggle = document.getElementById('darkModeToggle');
  darkToggle.addEventListener('click', () => {
    document.body.classList.toggle('dark');
  });

  // 🔍 Live search
  const searchBar = document.getElementById('searchBar');
  searchBar.addEventListener('input', (e) => {
    const query = e.target.value.toLowerCase();
    const sections = document.querySelectorAll('section');
    sections.forEach(section => {
      const text = section.textContent.toLowerCase();
      section.style.display = text.includes(query) ? 'block' : 'none';
    });
  });

  // 📂 Collapsibles
  const sections = document.querySelectorAll('section');
  sections.forEach(section => {
    section.classList.add('collapsible');
    const heading = section.querySelector('h2, h3, h4');
    if (!heading) return;

    const content = document.createElement('div');
    content.classList.add('content');

    while (heading.nextSibling) {
      content.appendChild(heading.nextSibling);
    }
    section.appendChild(content);

    heading.addEventListener('click', () => {
      section.classList.toggle('open');
    });
  });

  // 🎬 Inline video on right
  const playerArea = document.getElementById('player-area');

  document.querySelectorAll('ul a').forEach(link => {
    link.addEventListener('click', function (e) {
      const videoUrl = this.getAttribute('href');
      const isVideo = videoUrl.match(/\.(mp4|webm|ogg)$/i);
      if (!isVideo) return;

      e.preventDefault();
      const title = this.textContent;

      playerArea.innerHTML = `
        <div class="player-container">
          <div class="player-header">
            <span>${title}</span>
            <button class="close-btn" onclick="closePlayer()">⨯</button>
          </div>
          <video controls autoplay>
            <source src="${videoUrl}" type="video/mp4">
            Your browser does not support the video tag.
          </video>
        </div>
      `;
    });
  });
});

// 🔒 Close player globally
function closePlayer() {
  const playerArea = document.getElementById('player-area');
  if (playerArea) playerArea.innerHTML = '';
}
