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

// Stagger index for grid children with fade-in
document.querySelectorAll('.media-grid, .edu-grid, .skills-cloud, .hero-tags, .achievement-list, .contact-links').forEach(grid => {
    Array.from(grid.children).forEach((child, i) => {
        child.style.setProperty('--stagger-index', i);
    });
});

// Mobile Menu Functionality
const mobileMenuToggle = document.querySelector('.mobile-menu-toggle');
const navLinks = document.querySelector('.nav-links');
const body = document.body;

function setMenuOpen(open) {
    mobileMenuToggle.classList.toggle('active', open);
    navLinks.classList.toggle('active', open);
    body.classList.toggle('menu-open', open);
    mobileMenuToggle.setAttribute('aria-expanded', open ? 'true' : 'false');
}

mobileMenuToggle.addEventListener('click', () => {
    setMenuOpen(!navLinks.classList.contains('active'));
});

document.querySelectorAll('.nav-links a').forEach(item => {
    item.addEventListener('click', () => setMenuOpen(false));
});

document.addEventListener('click', (e) => {
    if (
        navLinks.classList.contains('active') &&
        !navLinks.contains(e.target) &&
        !mobileMenuToggle.contains(e.target)
    ) {
        setMenuOpen(false);
    }
});

// Close on Escape
document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && navLinks.classList.contains('active')) {
        setMenuOpen(false);
        mobileMenuToggle.focus();
    }
});
