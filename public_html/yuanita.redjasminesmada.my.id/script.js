let text = document.getElementById('text');
let pohonKiri = document.getElementById('pohon-kiri');
let pohonKanan = document.getElementById('pohon-kanan');
let tulipKiri = document.getElementById('tulip-kiri');
let tulipKanan = document.getElementById('tulip-kanan');

window.addEventListener('scroll', () => {
    let value = window.scrollY;

    text.style.marginTop = value * 1.5 + 'px'
    pohonKiri.style.left = value * -1.5 + 'px'
    pohonKanan.style.left = value * 1.5 + 'px'
    tulipKiri.style.left = value * 0.5 + 'px'
    tulipKanan.style.left = value * -0.5 + 'px'
});