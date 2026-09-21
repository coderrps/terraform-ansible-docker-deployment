// ===========================
// NAV SCROLL EFFECT
// ===========================
const nav = document.querySelector('.nav');
window.addEventListener('scroll', () => {
  if (window.scrollY > 50) {
    nav.style.background = 'rgba(10,10,15,0.97)';
    nav.style.borderBottomColor = 'rgba(255,255,255,0.1)';
  } else {
    nav.style.background = 'rgba(10,10,15,0.85)';
    nav.style.borderBottomColor = 'rgba(255,255,255,0.07)';
  }
});

// ===========================
// HAMBURGER MENU
// ===========================
const hamburger = document.getElementById('hamburger');
const navLinks = document.querySelector('.nav-links');

hamburger.addEventListener('click', () => {
  navLinks.style.display = navLinks.style.display === 'flex' ? 'none' : 'flex';
  navLinks.style.flexDirection = 'column';
  navLinks.style.position = 'absolute';
  navLinks.style.top = '100%';
  navLinks.style.left = '0';
  navLinks.style.right = '0';
  navLinks.style.background = 'rgba(10,10,15,0.98)';
  navLinks.style.padding = '1.5rem';
  navLinks.style.borderBottom = '1px solid rgba(255,255,255,0.07)';
  navLinks.style.gap = '1.5rem';
});

// ===========================
// SMOOTH SCROLL
// ===========================
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function (e) {
    e.preventDefault();
    const target = document.querySelector(this.getAttribute('href'));
    if (target) {
      const offset = 80;
      const top = target.getBoundingClientRect().top + window.scrollY - offset;
      window.scrollTo({ top, behavior: 'smooth' });
      if (navLinks.style.display === 'flex' && navLinks.style.position === 'absolute') {
        navLinks.style.display = 'none';
      }
    }
  });
});

// ===========================
// REVEAL ON SCROLL
// ===========================
const revealElements = document.querySelectorAll(
  '.timeline-card, .project-card, .skill-group, .edu-card, .cert-card, .achievement-item'
);

revealElements.forEach(el => el.classList.add('reveal'));

const observer = new IntersectionObserver((entries) => {
  entries.forEach((entry, i) => {
    if (entry.isIntersecting) {
      setTimeout(() => {
        entry.target.classList.add('visible');
      }, 80 * (Array.from(revealElements).indexOf(entry.target) % 4));
      observer.unobserve(entry.target);
    }
  });
}, { threshold: 0.1, rootMargin: '0px 0px -40px 0px' });

revealElements.forEach(el => observer.observe(el));

// ===========================
// TYPING EFFECT
// ===========================
function typeEffect(element, text, speed = 45) {
  let i = 0;
  element.textContent = '';
  const interval = setInterval(() => {
    element.textContent += text[i];
    i++;
    if (i >= text.length) clearInterval(interval);
  }, speed);
}

// ===========================
// CONTACT FORM
// ===========================


// ===========================
// SKILL TAGS HOVER EFFECT
// ===========================
document.querySelectorAll('.skill-tag').forEach(tag => {
  tag.addEventListener('mouseenter', () => {
    tag.style.transform = 'translateY(-2px)';
  });
  tag.addEventListener('mouseleave', () => {
    tag.style.transform = 'translateY(0)';
  });
});

// Active nav link highlight
const sections = document.querySelectorAll('section[id]');
window.addEventListener('scroll', () => {
  let current = '';
  sections.forEach(section => {
    const sectionTop = section.offsetTop - 120;
    if (window.scrollY >= sectionTop) current = section.getAttribute('id');
  });
  document.querySelectorAll('.nav-links a').forEach(link => {
    link.style.color = '';
    if (link.getAttribute('href') === `#${current}`) {
      link.style.color = '#a78bfa';
    }
  });
});
