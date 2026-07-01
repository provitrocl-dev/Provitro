#!/usr/bin/env python3
"""
generate-villes-provitro.py
Génère les 10 pages SEO par ville pour provitro.net,
sur le même principe que generate-villes.js utilisé pour vitresh2o.com.

Pour ajouter une ville : ajoute une entrée dans VILLES, relance le script.
"""

import os

VILLES = [
    {
        "slug": "beloeil",
        "nom": "Beloeil",
        "accroche": "Le lavage de vitres à Beloeil, c'est nous.",
        "intro": "À Beloeil, plusieurs propriétés profitent d'une vue exceptionnelle sur le mont Saint-Hilaire, la rivière Richelieu ou les nombreux espaces verts de la région. Pourtant, après un hiver québécois, cette vue est souvent cachée derrière une couche de poussière, de pollen et de résidus accumulés sur les fenêtres.",
        "para2": "C'est particulièrement vrai dans les secteurs près de la montagne et des zones boisées où le pollen est très présent au printemps. Plusieurs propriétaires nous contactent justement à cette période de l'année parce qu'ils réalisent que leurs fenêtres limitent la lumière naturelle qui entre dans la maison.",
        "para3": "À Beloeil, nous remarquons aussi que plusieurs maisons possèdent de grandes fenêtres à l'arrière donnant sur la cour, la piscine ou le paysage. Ces surfaces vitrées deviennent rapidement le point focal de la propriété lorsqu'elles sont propres.",
    },
    {
        "slug": "boucherville",
        "nom": "Boucherville",
        "accroche": "Le lavage de vitres à Boucherville, c'est notre spécialité.",
        "intro": "Boucherville se distingue par ses quartiers résidentiels matures, ses grandes propriétés près des parcs et des îles, et ses maisons aux façades vitrées généreuses. Avec la proximité du fleuve, le vent et l'humidité laissent rapidement leur trace sur les fenêtres.",
        "para2": "Plusieurs résidents de Boucherville nous contactent au printemps et à l'automne, deux moments charnières où la lumière change et où les fenêtres encrassées deviennent particulièrement visibles, surtout dans les maisons avec de grandes baies vitrées au rez-de-chaussée.",
        "para3": "Nous desservons aussi bien les quartiers près du Vieux-Boucherville que les développements plus récents, avec le même souci du détail et la même rapidité d'exécution partout en ville.",
    },
    {
        "slug": "brossard",
        "nom": "Brossard",
        "accroche": "Le lavage de vitres à Brossard, on connaît ça.",
        "intro": "Brossard, avec sa densité résidentielle élevée et ses nombreuses copropriétés et maisons en rangée, présente un défi particulier : des fenêtres nombreuses, souvent hautes, qui demandent un travail précis et sécuritaire.",
        "para2": "Entre le DIX30, les quartiers résidentiels et les développements près du fleuve, les propriétaires de Brossard recherchent un service fiable, rapide et qui respecte leur horaire chargé. C'est exactement ce qu'on offre.",
        "para3": "Que ce soit pour une maison unifamiliale ou une copropriété avec plusieurs fenêtres en hauteur, notre équipe s'adapte à chaque configuration pour un résultat impeccable.",
    },
    {
        "slug": "chambly",
        "nom": "Chambly",
        "accroche": "Le lavage de vitres à Chambly, c'est notre terrain de jeu.",
        "intro": "Chambly, avec son bassin, son canal historique et ses quartiers résidentiels en bordure de l'eau, compte plusieurs propriétés où la vue sur l'eau est un véritable atout — à condition que les fenêtres soient impeccables.",
        "para2": "Les propriétaires près du bassin de Chambly nous contactent souvent après l'hiver, quand le sel et les résidus accumulés sur les fenêtres orientées vers l'eau ternissent une vue qu'ils ont payé cher pour avoir.",
        "para3": "On dessert autant le Vieux-Chambly que les nouveaux quartiers résidentiels, avec un service constant, peu importe le secteur.",
    },
    {
        "slug": "longueuil",
        "nom": "Longueuil",
        "accroche": "Le lavage de vitres à Longueuil, c'est nous qu'il vous faut.",
        "intro": "Longueuil est l'une des plus grandes villes de la Rive-Sud, avec une diversité de propriétés : maisons unifamiliales, copropriétés modernes et résidences plus anciennes près du Vieux-Longueuil.",
        "para2": "Cette diversité demande une équipe qui sait s'adapter — que ce soit pour de grandes fenêtres panoramiques dans les nouveaux développements ou pour des fenêtres à guillotine plus traditionnelles dans les quartiers établis.",
        "para3": "Peu importe votre secteur à Longueuil, on offre le même service rapide, le même souci du détail et la même garantie de résultat.",
    },
    {
        "slug": "mont-saint-hilaire",
        "nom": "Mont-Saint-Hilaire",
        "accroche": "Le lavage de vitres à Mont-Saint-Hilaire, c'est notre passion.",
        "intro": "Mont-Saint-Hilaire offre certains des plus beaux points de vue de la Rive-Sud, entre la montagne, la rivière Richelieu et les vergers environnants. Beaucoup de propriétés sont construites justement pour profiter de cette vue grâce à de grandes surfaces vitrées.",
        "para2": "Le problème, c'est que ces mêmes fenêtres accumulent rapidement poussière, pollen et résidus, surtout dans les secteurs boisés près de la montagne. Plusieurs propriétaires nous contactent au printemps pour redonner de l'éclat à leur vue.",
        "para3": "Notre objectif à Mont-Saint-Hilaire est simple : vous permettre de profiter pleinement du paysage exceptionnel pour lequel vous avez choisi cette ville.",
    },
    {
        "slug": "otterburn-park",
        "nom": "Otterburn Park",
        "accroche": "Le lavage de vitres à Otterburn Park, c'est nous.",
        "intro": "Otterburn Park, petite ville tranquille au pied du mont Saint-Hilaire, compte plusieurs résidences entourées de verdure — magnifique pour le paysage, plus exigeant pour l'entretien des fenêtres.",
        "para2": "Entre la proximité de la montagne et des grands arbres matures qui caractérisent plusieurs quartiers, le pollen et les résidus organiques s'accumulent vite sur les fenêtres, particulièrement au printemps et à l'automne.",
        "para3": "On dessert l'ensemble d'Otterburn Park avec le même engagement : un travail soigné, rapide, et un résultat qui dure.",
    },
    {
        "slug": "saint-bruno",
        "nom": "Saint-Bruno-de-Montarville",
        "accroche": "Le lavage de vitres à Saint-Bruno, c'est chez nous.",
        "intro": "Saint-Bruno-de-Montarville, c'est notre coin de pays — c'est d'ici que Provitro a commencé. On connaît les quartiers, les types de propriétés et les défis particuliers du secteur, entre la proximité du Parc national du Mont-Saint-Bruno et les nombreux quartiers résidentiels matures.",
        "para2": "Les grands arbres qui font la réputation de Saint-Bruno apportent aussi leur lot de résidus sur les fenêtres : pollen, sève et poussière s'accumulent rapidement, surtout dans les quartiers plus boisés.",
        "para3": "En tant qu'entreprise locale, on est fiers d'offrir un service rapide et personnalisé à nos voisins de Saint-Bruno.",
    },
    {
        "slug": "saint-hyacinthe",
        "nom": "Saint-Hyacinthe",
        "accroche": "Le lavage de vitres à Saint-Hyacinthe, c'est notre métier.",
        "intro": "Saint-Hyacinthe, avec ses quartiers résidentiels établis et ses propriétés plus récentes en périphérie, présente une belle variété de styles de maisons — et donc de types de fenêtres à entretenir.",
        "para2": "Le climat de la région, entre les saisons agricoles environnantes et les conditions hivernales rigoureuses, laisse souvent des traces tenaces sur les fenêtres extérieures, surtout sur les façades les plus exposées.",
        "para3": "Notre équipe dessert Saint-Hyacinthe avec le même standard de qualité qu'ailleurs sur la Rive-Sud : rapide, soigné, et garanti.",
    },
    {
        "slug": "sainte-julie",
        "nom": "Sainte-Julie",
        "accroche": "Le lavage de vitres à Sainte-Julie, c'est notre affaire.",
        "intro": "Sainte-Julie, avec ses nombreux quartiers familiaux et ses maisons récentes aux grandes fenêtres, est un secteur où la luminosité naturelle est souvent un argument de vente important — encore faut-il que les fenêtres soient impeccables pour en profiter.",
        "para2": "Les développements résidentiels plus récents de Sainte-Julie comptent souvent de grandes baies vitrées au rez-de-chaussée et à l'étage, qui demandent un entretien régulier pour conserver leur éclat.",
        "para3": "On dessert l'ensemble de Sainte-Julie avec un service ponctuel, professionnel et un résultat qui parle de lui-même.",
    },
]

TEMPLATE = """<!DOCTYPE html>
<html lang="fr">
<head>

<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=AW-16916227020"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){{dataLayer.push(arguments);}}
  gtag('js', new Date());

  gtag('config', 'AW-16916227020');
</script>

  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">

  <title>Lavage de Vitres {nom} | Provitro</title>
  <meta name="description" content="Lavage de vitres professionnel à {nom}. Provitro dessert toute la Rive-Sud — service rapide, résultat impeccable, soumission gratuite.">

  <meta name="robots" content="index, follow">

  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Anton&display=swap" rel="stylesheet">

  <link rel="stylesheet" href="assets/css/main.css">
  <link rel="preload" as="image" href="assets/img/hero.webp">

</head>

<body>

<!-- HEADER -->
<header class="pv-header" role="banner">
  <div class="pv-header__capsule">
    <a class="pv-header__brand" href="index.html" aria-label="Accueil Provitro">
      <img src="assets/img/provitro-logo.svg" alt="Provitro" class="pv-header__logo">
    </a>
    <nav class="pv-header__nav" aria-label="Menu principal">
      <ul class="pv-header__menu">
        <li class="pv-header__item"><a class="pv-header__link" href="index.html">Accueil</a></li>
        <li class="pv-header__item"><a class="pv-header__link" href="about.html">À propos</a></li>
        <li class="pv-header__item"><a class="pv-header__link" href="contact.html">Nous contacter</a></li>
      </ul>
    </nav>
    <div class="pv-header__actions">
      <a class="pv-header__call" href="tel:5149741773">Appelez</a>
      <a class="pv-header__cta pv-popup-trigger" href="#">Soumission</a>
    </div>
    <details class="pv-header__drawer">
      <summary class="pv-header__burger" aria-label="Ouvrir le menu">
        <svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M4 7h16v2H4V7zm0 6h16v2H4v-2zm0 6h16v2H4v-2z"/></svg>
      </summary>
      <div class="pv-header__drawer-panel" role="dialog" aria-modal="true">
        <div class="pv-header__drawer-inner">
          <a class="pv-header__drawer-btn pv-header__drawer-btn--call" href="tel:5149741773">Appelez</a>
          <a class="pv-header__drawer-btn pv-header__drawer-btn--quote pv-popup-trigger" href="#">Soumission</a>
          <nav aria-label="Menu mobile">
            <ul class="pv-header__drawer-menu">
              <li><a class="pv-header__drawer-link" href="index.html">Accueil</a></li>
              <li><a class="pv-header__drawer-link" href="about.html">À propos</a></li>
              <li><a class="pv-header__drawer-link" href="contact.html">Nous contacter</a></li>
            </ul>
          </nav>
        </div>
      </div>
    </details>
  </div>
</header>


<!-- HERO VILLE -->
<section id="top" class="pv-hero">
  <div class="pv-hero__bg">
    <img src="{hero_img}" alt="" class="pv-hero__image" width="1600" height="900" fetchpriority="high">
  </div>
  <div class="pv-hero__overlay"></div>
  <div class="pv-container pv-hero__inner">
    <div class="pv-hero__left">
      <div class="pv-hero__rating">
        <span class="pv-hero__badge"><span class="pv-hero__stars">★★★★★</span></span>
        <a class="pv-hero__rating-link" href="#" target="_blank" rel="noopener noreferrer">
          <span class="pv-hero__rating-text">5 sur Google</span>
          <span class="pv-hero__google" aria-hidden="true">
            <svg viewBox="0 0 48 48" focusable="false">
              <path fill="#EA4335" d="M24 9.5c3.32 0 6.3 1.15 8.64 3.04l6.43-6.43C35.2 2.62 29.9 0 24 0 14.62 0 6.54 5.38 2.56 13.22l7.49 5.82C11.86 13.1 17.48 9.5 24 9.5z"/>
              <path fill="#4285F4" d="M46.5 24.5c0-1.56-.14-3.06-.4-4.5H24v9h12.64c-.54 2.9-2.18 5.36-4.64 7.04l7.08 5.48C43.22 37.7 46.5 31.6 46.5 24.5z"/>
              <path fill="#FBBC05" d="M10.05 28.96A14.3 14.3 0 0 1 9.3 24c0-1.73.31-3.4.75-4.96l-7.49-5.82A23.9 23.9 0 0 0 0 24c0 3.9.93 7.58 2.56 10.78l7.49-5.82z"/>
              <path fill="#34A853" d="M24 48c6.48 0 11.92-2.14 15.89-5.78l-7.08-5.48c-1.97 1.32-4.5 2.1-8.81 2.1-6.52 0-12.14-3.6-13.95-8.54l-7.49 5.82C6.54 42.62 14.62 48 24 48z"/>
            </svg>
          </span>
        </a>
      </div>
      <h1 class="pv-hero__title">Lavage de vitres<br><span class="pv-highlight">{nom}.</span></h1>
      <p class="pv-hero__subtitle">Service résidentiel professionnel à {nom} et partout sur la Rive-Sud. Résultat garanti.</p>
      <a href="#" class="pv-btn pv-btn-primary pv-popup-trigger">Obtenir une soumission</a>
    </div>
  </div>
</section>


<!-- TEXTE SEO VILLE -->
<section class="pv-ville-seo">
  <div class="pv-ville-seo__inner">
    <div class="pv-ville-seo__grid">
      <div class="pv-ville-seo__text">
        <p class="pv-ville-seo__eyebrow">On dessert {nom}</p>
        <h2 class="pv-ville-seo__title">{accroche}</h2>
        <p class="pv-ville-seo__body">{intro}</p>
        <p class="pv-ville-seo__body">{para2}</p>
        <p class="pv-ville-seo__body">{para3}</p>
        <a href="#" class="pv-ville-seo__btn pv-popup-trigger">Obtenir mon prix à {nom}</a>
      </div>
      <div class="pv-ville-seo__img-wrap">
        <img src="assets/img/steps-photo.png" alt="Lavage de vitres à {nom}" class="pv-ville-seo__img" loading="lazy" decoding="async">
      </div>
    </div>
  </div>
</section>


<!-- SERVICES -->
<section class="pv-packages" id="services">
  <div class="pv-packages__container">
    <p class="pv-packages__eyebrow">Nos services</p>
    <h2 class="pv-packages__title">Adaptés à vos besoins</h2>
    <div class="pv-packages__grid">
      <article class="pv-package-card">
        <p class="pv-package-card__label">L'essentiel</p>
        <h3 class="pv-package-card__title">Lavage extérieur</h3>
        <p class="pv-package-card__text">Ce plan inclut le lavage des vitres extérieures, cadrages, portes vitrées/patios et seuils (sous-sol inclus).</p>
      </article>
      <article class="pv-package-card">
        <p class="pv-package-card__label">Le complet</p>
        <h3 class="pv-package-card__title">Lavage intérieur et extérieur</h3>
        <p class="pv-package-card__text">Ce plan inclut le lavage complet des vitres intérieures et extérieures, des portes patio et vitrées, des cadrages et des seuils.</p>
      </article>
      <article class="pv-package-card">
        <p class="pv-package-card__label">Deluxe</p>
        <h3 class="pv-package-card__title">Lavage int. et ext. + rails</h3>
        <p class="pv-package-card__text">Ce plan inclut le lavage des vitres intérieures et extérieures, des portes patio et vitrées, des seuils, des moustiquaires, des cadrages et des seuils de portes.</p>
      </article>
    </div>
    <div class="pv-packages__cta-wrap">
      <a href="#" class="pv-packages__cta pv-popup-trigger">Obtenir mon prix</a>
    </div>
  </div>
</section>


<!-- FAQ -->
<section class="pv-faq">
  <div class="pv-faq__inner">
    <p class="pv-faq__eyebrow">Questions fréquentes</p>
    <h2 class="pv-faq__title">À propos du service à {nom}</h2>

    <div class="pv-faq__item">
      <button class="pv-faq__question" aria-expanded="false">
        <span>Combien de temps prend un lavage de vitres à {nom}?</span>
        <span class="pv-faq__icon"></span>
      </button>
      <div class="pv-faq__answer">
        <div class="pv-faq__answer-inner">Pour une maison unifamiliale standard, comptez généralement entre 1h et 2h selon le forfait choisi et le nombre de fenêtres.</div>
      </div>
    </div>

    <div class="pv-faq__item">
      <button class="pv-faq__question" aria-expanded="false">
        <span>Offrez-vous des soumissions gratuites à {nom}?</span>
        <span class="pv-faq__icon"></span>
      </button>
      <div class="pv-faq__answer">
        <div class="pv-faq__answer-inner">Oui, la soumission est toujours gratuite et sans engagement. On vous revient généralement en moins de 24h.</div>
      </div>
    </div>

    <div class="pv-faq__item">
      <button class="pv-faq__question" aria-expanded="false">
        <span>Le nettoyage de gouttières est-il offert à {nom}?</span>
        <span class="pv-faq__icon"></span>
      </button>
      <div class="pv-faq__answer">
        <div class="pv-faq__answer-inner">Oui, on offre le nettoyage de gouttières en service complémentaire. Mentionnez-le simplement dans votre demande de soumission.</div>
      </div>
    </div>
  </div>
</section>


<!-- BANNIÈRE CTA -->
<section class="pv-cta-banner">
  <div class="pv-cta-banner__bg">
    <img src="assets/img/bg_text.webp" alt="" class="pv-cta-banner__img">
  </div>
  <div class="pv-cta-banner__overlay"></div>
  <div class="pv-cta-banner__inner">
    <div class="pv-cta-banner__content">
      <h2 class="pv-cta-banner__title">Vous êtes à {nom}?</h2>
      <p class="pv-cta-banner__subtitle">Soumission à distance et prise de RDV selon vos disponibilités!</p>
      <a href="#" class="pv-cta-banner__btn pv-popup-trigger">Obtenir mon prix</a>
    </div>
  </div>
</section>


<!-- ===================================== -->
<!-- FOOTER -->
<!-- ===================================== -->

<footer class="pv-footer">
  <div class="pv-footer__inner">
    <div class="pv-footer__grid pv-footer__grid--5col">

      <div class="pv-footer__brand">
        <img src="assets/img/logo-footer.svg" alt="Provitro" class="pv-footer__logo">
        <p class="pv-footer__brand-text">Lavage de vitres professionnel sur la Rive-Sud de Montréal.</p>
        <div class="pv-footer__socials">
          <a href="https://www.instagram.com/provitro.qc/" class="pv-footer__social" target="_blank" rel="noopener noreferrer">Instagram</a>
          <a href="https://www.tiktok.com/@provitro.qc" class="pv-footer__social" target="_blank" rel="noopener noreferrer">TikTok</a>
          <a href="https://www.facebook.com/p/ProVitro-100093541280861/" class="pv-footer__social" target="_blank" rel="noopener noreferrer">Facebook</a>
        </div>
      </div>

      <div class="pv-footer__col">
        <h3 class="pv-footer__heading">Navigation</h3>
        <ul class="pv-footer__list">
          <li><a href="index.html" class="pv-footer__link">Accueil</a></li>
          <li><a href="about.html" class="pv-footer__link">À propos</a></li>
          <li><a href="index.html#services" class="pv-footer__link">Services</a></li>
          <li><a href="index.html#reviews" class="pv-footer__link">Avis</a></li>
          <li><a href="contact.html" class="pv-footer__link">Contact</a></li>
        </ul>
      </div>

      <div class="pv-footer__col">
        <h3 class="pv-footer__heading">Services</h3>
        <ul class="pv-footer__list">
          <li><a href="index.html#services" class="pv-footer__link">Lavage extérieur</a></li>
          <li><a href="index.html#services" class="pv-footer__link">Lavage intérieur et extérieur</a></li>
          <li><a href="index.html#services" class="pv-footer__link">Deluxe</a></li>
          <li><a href="contact.html" class="pv-footer__link">Nettoyage de gouttières</a></li>
        </ul>
      </div>

      <div class="pv-footer__col">
        <h3 class="pv-footer__heading">Villes desservies</h3>
        <ul class="pv-footer__list">
          <li><a href="beloeil.html" class="pv-footer__link">Beloeil</a></li>
          <li><a href="boucherville.html" class="pv-footer__link">Boucherville</a></li>
          <li><a href="brossard.html" class="pv-footer__link">Brossard</a></li>
          <li><a href="chambly.html" class="pv-footer__link">Chambly</a></li>
          <li><a href="longueuil.html" class="pv-footer__link">Longueuil</a></li>
          <li><a href="mont-saint-hilaire.html" class="pv-footer__link">Mont-Saint-Hilaire</a></li>
          <li><a href="otterburn-park.html" class="pv-footer__link">Otterburn Park</a></li>
          <li><a href="saint-bruno.html" class="pv-footer__link">Saint-Bruno-de-Montarville</a></li>
          <li><a href="saint-hyacinthe.html" class="pv-footer__link">Saint-Hyacinthe</a></li>
          <li><a href="sainte-julie.html" class="pv-footer__link">Sainte-Julie</a></li>
          <li><span class="pv-footer__text">Et bien d'autres!</span></li>
        </ul>
      </div>

      <div class="pv-footer__col">
        <h3 class="pv-footer__heading">Coordonnées</h3>
        <ul class="pv-footer__list">
          <li><a href="tel:5149741773" class="pv-footer__link">(514) 974-1773</a></li>
          <li><a href="mailto:info@provitro.net" class="pv-footer__link">info@provitro.net</a></li>
          <li><span class="pv-footer__text">Rive-Sud de Montréal</span></li>
        </ul>
      </div>

    </div>

    <div class="pv-footer__bottom">
      <div class="pv-footer__line"></div>
      <p class="pv-footer__copyright">© 2026 Provitro. Tous droits réservés.</p>
    </div>
  </div>
</footer>


<!-- POPUP -->
<div class="pv-popup" id="pvPopup" role="dialog" aria-modal="true" aria-label="Obtenir une soumission" hidden>
  <div class="pv-popup__backdrop"></div>
  <div class="pv-popup__panel">
    <button class="pv-popup__close" aria-label="Fermer" type="button">
      <svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M18 6L6 18M6 6l12 12" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/></svg>
    </button>
    <p class="pv-popup__eyebrow">Service rapide & professionnel</p>
    <h2 class="pv-popup__title">Obtenir une soumission</h2>
    <p class="pv-popup__lead">Laissez-nous vos coordonnées, on vous rappelle sous 24h avec votre prix.</p>
    <form class="pv-popup__form" id="pvPopupForm" novalidate>
      <div class="pv-popup__fields">
        <div class="pv-popup__field">
          <label for="pp-name" class="pv-popup__label">Nom complet *</label>
          <input id="pp-name" name="fullName" type="text" class="pv-popup__input" placeholder="Votre nom complet" required autocomplete="name">
        </div>
        <div class="pv-popup__field">
          <label for="pp-phone" class="pv-popup__label">Téléphone *</label>
          <input id="pp-phone" name="phone" type="tel" class="pv-popup__input" placeholder="(514) 000-0000" required autocomplete="tel">
        </div>
        <div class="pv-popup__field">
          <label for="pp-email" class="pv-popup__label">Courriel</label>
          <input id="pp-email" name="email" type="email" class="pv-popup__input" placeholder="vous@exemple.com" autocomplete="email">
        </div>
        <div class="pv-popup__field">
          <label for="pp-city" class="pv-popup__label">Adresse postale</label>
          <input id="pp-city" name="address" type="text" class="pv-popup__input" placeholder="123 Rue des Érables, Saint-Bruno" autocomplete="address-level2">
        </div>
      </div>
      <div class="pv-popup__error" id="pvPopupError" hidden>Veuillez remplir les champs obligatoires.</div>
      <button type="submit" class="pv-popup__btn" id="pvPopupBtn">
        <span class="pv-popup__btn-text">Envoyer ma demande</span>
        <span class="pv-popup__btn-spinner" hidden>
          <svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="10" stroke="currentColor" stroke-width="3" fill="none" stroke-dasharray="40" stroke-dashoffset="20"/></svg>
        </span>
      </button>
    </form>
    <div class="pv-popup__success" id="pvPopupSuccess" hidden>
      <div class="pv-popup__success-icon">✓</div>
      <h3 class="pv-popup__success-title">Demande reçue!</h3>
      <p class="pv-popup__success-text">On vous contacte sous 24h avec votre prix. Merci!</p>
    </div>
  </div>
</div>

<script src="assets/js/main.js"></script>
</body>
</html>
"""

def main():
    out_dir = os.path.dirname(os.path.abspath(__file__))
    for v in VILLES:
        html = TEMPLATE.format(**v)
        path = os.path.join(out_dir, f"{v['slug']}.html")
        with open(path, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"  ✓ {v['slug']}.html généré")
    print(f"\n{len(VILLES)} pages villes générées avec succès.")

if __name__ == "__main__":
    main()
