document.addEventListener('DOMContentLoaded', function() {
    const toggleButton = document.getElementById('dark-mode-toggle');
    const iconMoon = document.getElementById('moon-icon');
    const iconSun = document.getElementById('sun-icon');
    const body = document.body;

    // Aplica o estado do modo escuro salvo quando a página é carregada
    if (localStorage.getItem('darkMode') === 'enabled') {
        body.classList.add('dark-mode');
        iconMoon.classList.add('hidden');
        iconSun.classList.remove('hidden');
    }

    // Listener para o botão de toggle do modo escuro
    if (toggleButton) {
        toggleButton.addEventListener('click', () => {
            body.classList.toggle('dark-mode');
            if (body.classList.contains('dark-mode')) {
                localStorage.setItem('darkMode', 'enabled');
                iconMoon.classList.add('hidden');
                iconSun.classList.remove('hidden');
            } else {
                localStorage.setItem('darkMode', 'disabled');
                iconSun.classList.add('hidden');
                iconMoon.classList.remove('hidden');
            }
        });
    } else {
        console.error('Dark mode toggle button not found');
    }

    // Exibir a data e hora atuais
    function updateTime() {
        const dateTimeString = new Date().toLocaleString();
        const dateTimeElement = document.getElementById('date-time');
        if (dateTimeElement) {
            dateTimeElement.textContent = dateTimeString;
        } else {
            console.error('Date-time element not found');
        }
    }
    setInterval(updateTime, 1000);
    updateTime();
});

// Efeito Parallax para elementos com a classe .parallax
window.addEventListener('scroll', function() {
    const parallaxElement = document.querySelector('.parallax');
    if (parallaxElement) {
        let offset = window.pageYOffset;
        parallaxElement.style.backgroundPositionY = offset * 0.7 + "px";
    }
});














