window.addEventListener('load', () => {
  const p = document.getElementById('preloader');
  if (p) p.style.display = 'none';
});

// Safe initialization of particles
if (window.particlesJS) {
  particlesJS('particles-js', {
    particles: { number: { value: 40 }, color: { value: '#fff' },
      shape: { type: 'circle' }, line_linked: { enable: true, opacity: 0.2 }, move: { enable: true, speed: 2 } },
    interactivity: { events: { onhover: { enable: true, mode: 'grab' } }, modes: { grab: { distance: 100 } } },
    retina_detect: true
  });
}
