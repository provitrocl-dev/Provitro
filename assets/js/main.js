
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
  wrap.addEventListener('click', (e) => {
    const card = wrap.closest('.pv-social-card');
    const video = wrap.querySelector('.pv-social-card__video');

    if (!card || !video) return;

    // Si on clique sur la vidéo ou ses contrôles, ne rien faire
    if (e.target === video) return;

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

/* ─── POPUP SOUMISSION ─── */

// 👇 Colle ici l'URL de ton webhook GHL (Workflow → Trigger → Webhook)
const PV_WEBHOOK_URL = 'https://services.leadconnectorhq.com/hooks/m4jX0WSU2ubSdUqING3H/webhook-trigger/ffd4351f-5c5d-4b86-964e-6611574ab270';

// Capture les UTMs depuis l'URL (pour tracking Meta vs Google)
function getUtmParams() {
  const params = new URLSearchParams(window.location.search);
  return {
    utm_source:   params.get('utm_source')   || '',
    utm_medium:   params.get('utm_medium')   || '',
    utm_campaign: params.get('utm_campaign') || '',
    utm_content:  params.get('utm_content')  || '',
    gclid:        params.get('gclid')        || '',
    fbclid:       params.get('fbclid')       || '',
  };
}

const popup        = document.getElementById('pvPopup');
const popupForm    = document.getElementById('pvPopupForm');
const popupSuccess = document.getElementById('pvPopupSuccess');
const popupError   = document.getElementById('pvPopupError');
const popupBtn     = document.getElementById('pvPopupBtn');
const popupBtnText = popupBtn?.querySelector('.pv-popup__btn-text');
const popupSpinner = popupBtn?.querySelector('.pv-popup__btn-spinner');

function openPopup() {
  popup.hidden = false;
  document.body.style.overflow = 'hidden';
  // Focus le premier input
  setTimeout(() => popup.querySelector('.pv-popup__input')?.focus(), 50);
}

function closePopup() {
  popup.hidden = true;
  document.body.style.overflow = '';
  // Réinitialise le formulaire
  popupForm.reset();
  popupForm.hidden = false;
  popupSuccess.hidden = true;
  popupError.hidden = true;
  popupBtn.disabled = false;
  popupBtnText.hidden = false;
  popupSpinner.hidden = true;
  popupForm.querySelectorAll('.pv-invalid').forEach(el => el.classList.remove('pv-invalid'));
}

// Ouvrir via tous les triggers
document.querySelectorAll('.pv-popup-trigger').forEach(el => {
  el.addEventListener('click', e => {
    e.preventDefault();
    openPopup();
  });
});

// Fermer via le bouton X
popup?.querySelector('.pv-popup__close')?.addEventListener('click', closePopup);

// Fermer via le backdrop
popup?.querySelector('.pv-popup__backdrop')?.addEventListener('click', closePopup);

// Fermer via Escape
document.addEventListener('keydown', e => {
  if (e.key === 'Escape' && !popup?.hidden) closePopup();
});

// Soumission du formulaire
popupForm?.addEventListener('submit', async (e) => {
  e.preventDefault();

  const firstName = popupForm.querySelector('[name="firstName"]');
  const phone     = popupForm.querySelector('[name="phone"]');
  const email     = popupForm.querySelector('[name="email"]');
  const address = popupForm.querySelector('[name="address"]');

  // Validation basique
  let valid = true;
  [firstName, phone].forEach(field => {
    field.classList.remove('pv-invalid');
    if (!field.value.trim()) {
      field.classList.add('pv-invalid');
      valid = false;
    }
  });

  if (!valid) {
    popupError.hidden = false;
    return;
  }

  popupError.hidden = true;
  popupBtn.disabled = true;
  popupBtnText.hidden = true;
  popupSpinner.hidden = false;

  const payload = {
    firstName:    firstName.value.trim(),
    phone:        phone.value.trim(),
    email:        email.value.trim(),
    address:         address.value.trim(),
    source:       'Site web Provitro',
    tags:         ['site-web'],
    ...getUtmParams(),
  };

  try {
    await fetch(PV_WEBHOOK_URL, {
      method:  'POST',
      headers: { 'Content-Type': 'application/json' },
      body:    JSON.stringify(payload),
    });

    popupForm.hidden = true;
    popupSuccess.hidden = false;

  } catch (err) {
    // En cas d'erreur réseau, on montre quand même le succès (le lead a probablement passé)
    console.error('Webhook error:', err);
    popupForm.hidden = true;
    popupSuccess.hidden = false;
  }
});

/* TODO: Google Autocomplete - réactiver quand clé fonctionnelle
function initAutocomplete() {

function initAutocomplete() {
  const input = document.getElementById('pp-city');
  if (!input || !window.google) return;
  new google.maps.places.Autocomplete(input, {
    types: ['address'],
    componentRestrictions: { country: 'ca' },
  });
}

*/
