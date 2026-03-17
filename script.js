// Navbar scroll effect
const navbar = document.querySelector('.navbar');

window.addEventListener('scroll', () => {
    if (window.scrollY > 50) {
        navbar.classList.add('scrolled');
    } else {
        navbar.classList.remove('scrolled');
    }
});

// Intersection Observer for fade-in animations
const fadeElements = document.querySelectorAll('.fade-in');

const appearOptions = {
    threshold: 0.05,
    rootMargin: "0px 0px -50px 0px"
};

const appearOnScroll = new IntersectionObserver(function(entries, observer) {
    entries.forEach(entry => {
        if (!entry.isIntersecting) {
            return;
        } else {
            entry.target.classList.add('appear');
            observer.unobserve(entry.target);
        }
    });
}, appearOptions);

fadeElements.forEach(element => {
    appearOnScroll.observe(element);
});

// Interactive Mouse Glow Effect
const mouseGlow = document.getElementById('mouse-glow');

document.addEventListener('mousemove', (e) => {
    const x = e.clientX;
    const y = e.clientY;
    
    mouseGlow.style.left = `${x}px`;
    mouseGlow.style.top = `${y}px`;
});

// Add hover effect to interactive elements for the mouse glow
const interactiveElements = document.querySelectorAll('a, button, .glass-card, .skill-item');

interactiveElements.forEach(el => {
    el.addEventListener('mouseenter', () => {
        mouseGlow.style.width = '600px';
        mouseGlow.style.height = '600px';
        mouseGlow.style.background = 'radial-gradient(circle, rgba(233, 0, 116, 0.15) 0%, transparent 60%)';
    });
    
    el.addEventListener('mouseleave', () => {
        mouseGlow.style.width = '400px';
        mouseGlow.style.height = '400px';
        mouseGlow.style.background = 'radial-gradient(circle, rgba(255, 255, 255, 0.1) 0%, transparent 60%)';
    });
});

// Mobile Menu Functionality
const mobileMenuToggle = document.querySelector('.mobile-menu-toggle');
const navLinks = document.querySelector('.nav-links');
const body = document.body;

mobileMenuToggle.addEventListener('click', () => {
    mobileMenuToggle.classList.toggle('active');
    navLinks.classList.toggle('active');
    body.classList.toggle('menu-open');
});

// Close menu when clicking on a link
const navItems = document.querySelectorAll('.nav-links a');
navItems.forEach(item => {
    item.addEventListener('click', () => {
        mobileMenuToggle.classList.remove('active');
        navLinks.classList.remove('active');
        body.classList.remove('menu-open');
    });
});

// Close menu when clicking outside
document.addEventListener('click', (e) => {
    if (!navLinks.contains(e.target) && !mobileMenuToggle.contains(e.target) && navLinks.classList.contains('active')) {
        mobileMenuToggle.classList.remove('active');
        navLinks.classList.remove('active');
        body.classList.remove('menu-open');
    }
});
