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

// Webhook GHL Provitro (Workflow → Trigger → Webhook)
const PV_WEBHOOK_URL = 'https://services.leadconnectorhq.com/hooks/m4jX0WSU2ubSdUqING3H/webhook-trigger/ffd4351f-5c5d-4b86-964e-6611574ab270';

// TODO : une fois la conversion "Demande de devis" créée dans le compte
// Google Ads Provitro, colle ici le AW-XXXXXXXXX/XXXXXXXXXX (même pattern que H2O)
const PV_GOOGLE_CONVERSION_ID = ''; // ex: 'AW-XXXXXXXXX/XXXXXXXXXX'

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
  setTimeout(() => popup.querySelector('.pv-popup__input')?.focus(), 50);
}

function closePopup() {
  popup.hidden = true;
  document.body.style.overflow = '';
  popupForm.reset();
  popupForm.hidden = false;
  popupSuccess.hidden = true;
  popupError.hidden = true;
  popupBtn.disabled = false;
  popupBtnText.hidden = false;
  popupSpinner.hidden = true;
  popupForm.querySelectorAll('.pv-invalid').forEach(el => el.classList.remove('pv-invalid'));
}

document.querySelectorAll('.pv-popup-trigger').forEach(el => {
  el.addEventListener('click', e => {
    e.preventDefault();
    openPopup();
  });
});

popup?.querySelector('.pv-popup__close')?.addEventListener('click', closePopup);
popup?.querySelector('.pv-popup__backdrop')?.addEventListener('click', closePopup);

document.addEventListener('keydown', e => {
  if (e.key === 'Escape' && !popup?.hidden) closePopup();
});

popupForm?.addEventListener('submit', async (e) => {
  e.preventDefault();

  const fullName = popupForm.querySelector('[name="fullName"]');
  const phone    = popupForm.querySelector('[name="phone"]');
  const email    = popupForm.querySelector('[name="email"]');
  const address  = popupForm.querySelector('[name="address"]');

  let valid = true;
  [fullName, phone].forEach(field => {
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

  const fullNameValue = fullName.value.trim();
  const nameParts = fullNameValue.split(/\s+/);

  const payload = {
    fullName: fullNameValue,
    name: fullNameValue,
    firstName: nameParts[0] || '',
    lastName: nameParts.slice(1).join(' ') || '',
    phone: phone.value.trim(),
    email: email.value.trim(),
    address: address.value.trim(),
    source: 'Site web Provitro',
    tags: ['site-web-provitro'],
    ...getUtmParams(),
  };

  try {
    await fetch(PV_WEBHOOK_URL, {
      method:  'POST',
      headers: { 'Content-Type': 'application/json' },
      body:    JSON.stringify(payload),
    });

    if (PV_GOOGLE_CONVERSION_ID && typeof gtag === 'function') {
      gtag('event', 'conversion', { 'send_to': PV_GOOGLE_CONVERSION_ID });
    }

    popupForm.hidden = true;
    popupSuccess.hidden = false;

  } catch (err) {
    console.error('Webhook error:', err);
    popupForm.hidden = true;
    popupSuccess.hidden = false;
  }
});

/* TODO: Google Autocomplete - réactiver quand clé fonctionnelle */
function initAutocomplete() {
  const input = document.getElementById('pp-city');
  if (!input || !window.google) return;
  new google.maps.places.Autocomplete(input, {
    types: ['address'],
    componentRestrictions: { country: 'ca' },
  });
}

/* ─── FAQ ACCORDION ─── */
document.querySelectorAll('.pv-faq__question').forEach(btn => {
  btn.addEventListener('click', () => {
    const item = btn.closest('.pv-faq__item');
    const answer = item.querySelector('.pv-faq__answer');
    const isOpen = btn.getAttribute('aria-expanded') === 'true';

    document.querySelectorAll('.pv-faq__question').forEach(other => {
      if (other !== btn) {
        other.setAttribute('aria-expanded', 'false');
        other.closest('.pv-faq__item').querySelector('.pv-faq__answer').classList.remove('is-open');
      }
    });

    btn.setAttribute('aria-expanded', String(!isOpen));
    answer.classList.toggle('is-open', !isOpen);
  });
});

/* ─── FORMULAIRE PAGE CONTACT (contact.html) ─── */
const contactForm = document.getElementById('pvContactForm');
const contactError = document.getElementById('pvContactError');
const contactBtn = document.getElementById('pvContactBtn');
const contactSuccess = document.getElementById('pvContactSuccess');

contactForm?.addEventListener('submit', async (e) => {
  e.preventDefault();
  const fullName = contactForm.querySelector('[name="fullName"]');
  const phone = contactForm.querySelector('[name="phone"]');

  let valid = true;
  [fullName, phone].forEach(f => {
    f.classList.remove('pv-invalid');
    if (!f.value.trim()) { f.classList.add('pv-invalid'); valid = false; }
  });
  if (!valid) { contactError.hidden = false; return; }

  contactError.hidden = true;
  contactBtn.disabled = true;
  contactBtn.querySelector('.pv-contact-page__submit-text').hidden = true;
  contactBtn.querySelector('.pv-contact-page__submit-spinner').hidden = false;

  const fullNameValue = fullName.value.trim();
  const nameParts = fullNameValue.split(/\s+/);

  const payload = {
    fullName: fullNameValue,
    name: fullNameValue,
    firstName: nameParts[0] || '',
    lastName: nameParts.slice(1).join(' ') || '',
    phone: phone.value.trim(),
    email: contactForm.querySelector('[name="email"]').value.trim(),
    address: contactForm.querySelector('[name="address"]').value.trim(),
    message: contactForm.querySelector('[name="message"]').value.trim(),
    source: 'Page Contact Provitro',
    tags: ['contact-provitro'],
    ...getUtmParams(),
  };

  try {
    await fetch(PV_WEBHOOK_URL, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(payload) });
  } catch (err) { console.error(err); }

  contactForm.hidden = true;
  contactSuccess.hidden = false;
});
