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
            navbar.style.boxShadow = '0 5px 20px rgba(0, 0, 0, 0.1)';
        } else {
            navbar.style.padding = '1rem 0';
            navbar.style.boxShadow = 'none';
        }
    });

    // Form submission handling (if needed in future)
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', function(e) {
            // Add form validation or submission handling here if needed
        });
    });
    
    // Check for logo and display it
    checkAndDisplayLogo();
});

// Function to check for logo and display it
function checkAndDisplayLogo() {
    const logoContainer = document.querySelector('.logo-container');
    if (logoContainer) {
        // Create an image element for the logo
        const logoImg = document.createElement('img');
        logoImg.src = 'images/IMG_1548.JPG';
        logoImg.alt = 'ARKANA AI Logo';
        logoImg.className = 'hero-logo';
        
        // Add load event to show logo when it's available
        logoImg.onload = function() {
            logoContainer.innerHTML = '';
            logoContainer.appendChild(logoImg);
            logoContainer.style.display = 'block';
        };
        
        // Add error handling
        logoImg.onerror = function() {
            // If logo doesn't exist, remove the container
            logoContainer.style.display = 'none';
        };
    }
}

// Handle window resize
window.addEventListener('resize', function() {
    // Reinitialize any components that need it on resize
});