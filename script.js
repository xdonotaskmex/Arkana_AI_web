// Initialize AOS (Animate On Scroll)
document.addEventListener('DOMContentLoaded', function() {
    // Initialize AOS
    AOS.init({
        duration: 1000,
        easing: 'ease-in-out',
        once: true
    });

    // Initialize Feather Icons
    feather.replace();

    // Initialize Vanta.js Globe background
    if (document.getElementById('globe-background')) {
        VANTA.GLOBE({
            el: '#globe-background',
            mouseControls: true,
            touchControls: true,
            gyroControls: false,
            minHeight: 200.00,
            minWidth: 200.00,
            scale: 1.00,
            scaleMobile: 1.00,
            color: 0x4cc9f0,
            color2: 0x9d4edd,
            backgroundColor: 0x0d141f,
            size: 1.00,
            lineColor: 0x4cc9f0,
            lineWidth: 1.00,
            showDots: true,
            dotColor: 0x9d4edd,
            dotSize: 1.00,
            backgroundAlpha: 1.00
        });
    }

    // Smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                window.scrollTo({
                    top: target.offsetTop - 70,
                    behavior: 'smooth'
                });
            }
        });
    });

    // Navbar scroll effect
    window.addEventListener('scroll', function() {
        const navbar = document.querySelector('.navbar');
        if (window.scrollY > 50) {
            navbar.style.padding = '0.5rem 0';
            navbar.style.boxShadow = '0 5px 20px rgba(0, 0, 0, 0.3)';
            navbar.style.background = 'rgba(13, 20, 31, 0.9)';
        } else {
            navbar.style.padding = '1rem 0';
            navbar.style.boxShadow = 'none';
            navbar.style.background = 'rgba(13, 20, 31, 0.7)';
        }
    });

    // Form submission handling (if needed in future)
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', function(e) {
            // Add form validation or submission handling here if needed
        });
    });
    
    // Create flying particles effect
    createFlyingParticles();
    
    // Reinitialize Feather Icons to include new icons in feedback section
    setTimeout(() => {
        feather.replace();
    }, 100);
    
});

// Function to create flying particles effect
function createFlyingParticles() {
    const heroSection = document.querySelector('.hero-section');
    if (!heroSection) return;
    
    // Reduce particle frequency for better performance
    setInterval(() => {
        createParticle(heroSection);
    }, 600); // Changed from 300ms to 600ms
}

// Function to create a single particle
function createParticle(container) {
    const particle = document.createElement('div');
    particle.classList.add('particle');
    
    // Randomly select particle size class
    const sizes = ['particle--1', 'particle--2', 'particle--3', 'particle--4'];
    const randomSize = sizes[Math.floor(Math.random() * sizes.length)];
    particle.classList.add(randomSize);
    
    // Random position around the hero section
    const startX = Math.random() * window.innerWidth;
    const startY = Math.random() * window.innerHeight;
    
    particle.style.left = `${startX}px`;
    particle.style.top = `${startY}px`;
    
    // Use consistent color with glow effect
    const color = '#4cc9f0';
    particle.style.background = color;
    particle.style.boxShadow = `0 0 8px 2px ${color}`;
    
    container.appendChild(particle);
    
    // Remove particle after animation completes
    setTimeout(() => {
        if (particle.parentNode) {
            particle.parentNode.removeChild(particle);
        }
    }, 8000); // Reduced from 15000ms to 8000ms for better performance
}

// Handle window resize
window.addEventListener('resize', function() {
    // Reinitialize any components that need it on resize
});