
  document.querySelectorAll('.pv-header__drawer-link, .pv-header__drawer-btn').forEach(link => {
    link.addEventListener('click', () => {
      const drawer = document.querySelector('.pv-header__drawer');
      if (drawer) drawer.removeAttribute('open');
    });
  });

  const socialTrack = document.querySelector('.pv-social__track');
const socialPrev = document.querySelector('.pv-social__nav--prev');
const socialNext = document.querySelector('.pv-social__nav--next');

if (socialTrack && socialPrev && socialNext && window.innerWidth > 980) {
  socialPrev.addEventListener('click', () => {
    socialTrack.scrollBy({ left: -320, behavior: 'smooth' });
  });

  socialNext.addEventListener('click', () => {
    socialTrack.scrollBy({ left: 320, behavior: 'smooth' });
  });
}

document.querySelectorAll('.pv-social-card__video-wrap').forEach((wrap) => {
  wrap.addEventListener('click', () => {
    const card = wrap.closest('.pv-social-card');
    const video = wrap.querySelector('.pv-social-card__video');

    if (!card || !video) return;

    document.querySelectorAll('.pv-social-card.active').forEach((otherCard) => {
      if (otherCard !== card) {
        otherCard.classList.remove('active');
        const otherVideo = otherCard.querySelector('.pv-social-card__video');
        if (otherVideo) {
          otherVideo.pause();
          otherVideo.currentTime = 0;
          otherVideo.removeAttribute('controls');
        }
      }
    });

    card.classList.add('active');
    video.setAttribute('controls', 'controls');
    video.play().catch(() => {});
  });
});