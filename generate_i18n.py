#!/usr/bin/env python3
"""
批量生成 Monkey Mart 多语言页面 + 长尾词页面
运行: python3 generate_i18n.py
"""
import os, json

BASE = os.path.dirname(os.path.abspath(__file__))

# ── 翻译数据 ──────────────────────────────────────────────
LANGS = {
    "es": {
        "lang": "es", "dir": "es",
        "home": "Inicio", "unblocked": "Sin Bloqueo", "how_to_play": "Cómo Jugar", "tips": "Trucos",
        "unblocked_slug": "monkey-mart-sin-bloqueo",
        "howto_slug": "como-jugar-monkey-mart",
        "tips_slug": "trucos-monkey-mart",
        "index": {
            "title": "Monkey Mart – Juega Gratis Online (2026) | MonkeyMartHub",
            "desc": "¡Juega Monkey Mart gratis online! Dirige tu supermercado de monos, cosecha cultivos y atiende clientes. Sin descarga – juega al instante.",
            "h1": "🐒 Monkey Mart – Juega Gratis Online",
            "hero_p": "¡Dirige tu propio supermercado de monos! Cosecha plátanos, llena estantes y atiende clientes en este adictivo juego idle. Sin descarga, sin registro.",
            "btn": "▶ Jugar Ahora – ¡Es Gratis!",
            "loading": "Cargando Monkey Mart…",
            "caption": "🎮 Usa WASD o las teclas de flecha para mover tu mono.",
            "what_h2": "¿Qué es Monkey Mart?",
            "what_p": "<strong>Monkey Mart</strong> es un popular juego idle de simulación de supermercado desarrollado por TinyDobbins. Controlas a un mono que dirige un supermercado desde cero: cosechas cultivos, llenas estantes y atiendes clientes automáticamente.",
            "faq_title": "Preguntas Frecuentes",
            "faq": [
                ("¿Es Monkey Mart gratis?", "¡Sí! Completamente gratis. Sin descarga, sin registro, sin pago."),
                ("¿Puedo jugar en móvil?", "Sí. Funciona en iOS y Android con joystick táctil en pantalla."),
                ("¿Quién creó Monkey Mart?", "Fue desarrollado por TinyDobbins y publicado originalmente en Poki y CrazyGames."),
            ],
            "footer_fan": "Monkey Mart es un juego de TinyDobbins. Este sitio es un sitio de fans y no está afiliado con el desarrollador original.",
            "privacy": "Política de Privacidad",
        },
        "howto": {
            "title": "Cómo Jugar Monkey Mart – Guía Completa para Principiantes 2026",
            "desc": "Aprende a jugar Monkey Mart con nuestra guía completa. Controles, mecánicas, mejoras y estrategias explicadas paso a paso.",
            "h1": "📖 Cómo Jugar Monkey Mart – Guía Completa",
            "hero_p": "Todo lo que necesitas saber para dominar Monkey Mart, desde los controles básicos hasta estrategias avanzadas.",
            "btn": "▶ Jugar Monkey Mart Ahora",
        },
        "tips": {
            "title": "Trucos de Monkey Mart – Mejores Estrategias para Ganar Más Rápido",
            "desc": "Los mejores trucos y consejos de Monkey Mart para ganar monedas más rápido, desbloquear mejoras antes y construir el supermercado definitivo.",
            "h1": "💡 Trucos y Consejos de Monkey Mart",
            "hero_p": "Maximiza tus monedas, desbloquea mejoras más rápido y construye el supermercado más eficiente con estas estrategias probadas.",
            "btn": "▶ Aplicar Estos Trucos Ahora",
        },
        "unblocked": {
            "title": "Monkey Mart Sin Bloqueo – Juega en la Escuela o el Trabajo",
            "desc": "Juega Monkey Mart sin bloqueo en la escuela o el trabajo. Nuestra versión está alojada en un dominio separado, accesible en redes restringidas.",
            "h1": "🔓 Monkey Mart Sin Bloqueo",
            "hero_p": "¿Bloqueado en la escuela o el trabajo? Juega Monkey Mart sin bloqueo directamente aquí. Sin VPN, sin extensiones.",
            "btn": "▶ Jugar Sin Bloqueo Ahora",
        },
    },
    "pt": {
        "lang": "pt", "dir": "pt",
        "home": "Início", "unblocked": "Sem Bloqueio", "how_to_play": "Como Jogar", "tips": "Dicas",
        "unblocked_slug": "monkey-mart-sem-bloqueio",
        "howto_slug": "como-jogar-monkey-mart",
        "tips_slug": "dicas-monkey-mart",
        "index": {
            "title": "Monkey Mart – Jogue Grátis Online (2026) | MonkeyMartHub",
            "desc": "Jogue Monkey Mart grátis online! Gerencie seu supermercado de macacos, colha culturas e atenda clientes. Sem download – jogue instantaneamente.",
            "h1": "🐒 Monkey Mart – Jogue Grátis Online",
            "hero_p": "Gerencie seu próprio supermercado de macacos! Colha bananas, abasteça prateleiras e atenda clientes neste viciante jogo idle. Sem download, sem cadastro.",
            "btn": "▶ Jogar Agora – É Grátis!",
            "loading": "Carregando Monkey Mart…",
            "caption": "🎮 Use WASD ou as teclas de seta para mover seu macaco.",
            "what_h2": "O que é Monkey Mart?",
            "what_p": "<strong>Monkey Mart</strong> é um popular jogo idle de simulação de supermercado desenvolvido pela TinyDobbins. Você controla um macaco que administra um supermercado do zero: colhe culturas, abastece prateleiras e atende clientes automaticamente.",
            "faq_title": "Perguntas Frequentes",
            "faq": [
                ("Monkey Mart é gratuito?", "Sim! Completamente gratuito. Sem download, sem cadastro, sem pagamento."),
                ("Posso jogar no celular?", "Sim. Funciona no iOS e Android com joystick na tela."),
                ("Quem criou o Monkey Mart?", "Foi desenvolvido pela TinyDobbins e publicado originalmente no Poki e CrazyGames."),
            ],
            "footer_fan": "Monkey Mart é um jogo da TinyDobbins. Este site é um site de fãs e não é afiliado ao desenvolvedor original.",
            "privacy": "Política de Privacidade",
        },
        "howto": {
            "title": "Como Jogar Monkey Mart – Guia Completo para Iniciantes 2026",
            "desc": "Aprenda a jogar Monkey Mart com nosso guia completo. Controles, mecânicas, melhorias e estratégias explicadas passo a passo.",
            "h1": "📖 Como Jogar Monkey Mart – Guia Completo",
            "hero_p": "Tudo que você precisa saber para dominar o Monkey Mart, dos controles básicos às estratégias avançadas.",
            "btn": "▶ Jogar Monkey Mart Agora",
        },
        "tips": {
            "title": "Dicas de Monkey Mart – Melhores Estratégias para Ganhar Mais Rápido",
            "desc": "As melhores dicas e truques de Monkey Mart para ganhar moedas mais rápido e construir o supermercado definitivo.",
            "h1": "💡 Dicas e Truques de Monkey Mart",
            "hero_p": "Maximize suas moedas, desbloqueie melhorias mais rápido e construa o supermercado mais eficiente com essas estratégias comprovadas.",
            "btn": "▶ Aplicar Essas Dicas Agora",
        },
        "unblocked": {
            "title": "Monkey Mart Sem Bloqueio – Jogue na Escola ou no Trabalho",
            "desc": "Jogue Monkey Mart sem bloqueio na escola ou no trabalho. Nossa versão está hospedada em um domínio separado, acessível em redes restritas.",
            "h1": "🔓 Monkey Mart Sem Bloqueio",
            "hero_p": "Bloqueado na escola ou no trabalho? Jogue Monkey Mart sem bloqueio diretamente aqui. Sem VPN, sem extensões.",
            "btn": "▶ Jogar Sem Bloqueio Agora",
        },
    },
    "fr": {
        "lang": "fr", "dir": "fr",
        "home": "Accueil", "unblocked": "Débloqué", "how_to_play": "Comment Jouer", "tips": "Astuces",
        "unblocked_slug": "monkey-mart-debloque",
        "howto_slug": "comment-jouer-monkey-mart",
        "tips_slug": "astuces-monkey-mart",
        "index": {
            "title": "Monkey Mart – Jouer Gratuitement en Ligne (2026) | MonkeyMartHub",
            "desc": "Jouez à Monkey Mart gratuitement en ligne ! Gérez votre supermarché de singes, récoltez des cultures et servez des clients. Sans téléchargement.",
            "h1": "🐒 Monkey Mart – Jouer Gratuitement en Ligne",
            "hero_p": "Gérez votre propre supermarché de singes ! Récoltez des bananes, remplissez les rayons et servez les clients dans ce jeu idle addictif. Sans téléchargement, sans inscription.",
            "btn": "▶ Jouer Maintenant – C'est Gratuit !",
            "loading": "Chargement de Monkey Mart…",
            "caption": "🎮 Utilisez WASD ou les touches fléchées pour déplacer votre singe.",
            "what_h2": "Qu'est-ce que Monkey Mart ?",
            "what_p": "<strong>Monkey Mart</strong> est un populaire jeu idle de simulation de supermarché développé par TinyDobbins. Vous contrôlez un singe qui gère un supermarché de zéro : récoltez des cultures, remplissez les rayons et servez automatiquement les clients.",
            "faq_title": "Questions Fréquentes",
            "faq": [
                ("Monkey Mart est-il gratuit ?", "Oui ! Complètement gratuit. Sans téléchargement, sans inscription, sans paiement."),
                ("Puis-je jouer sur mobile ?", "Oui. Fonctionne sur iOS et Android avec un joystick tactile à l'écran."),
                ("Qui a créé Monkey Mart ?", "Développé par TinyDobbins et publié à l'origine sur Poki et CrazyGames."),
            ],
            "footer_fan": "Monkey Mart est un jeu de TinyDobbins. Ce site est un site de fans et n'est pas affilié au développeur original.",
            "privacy": "Politique de Confidentialité",
        },
        "howto": {
            "title": "Comment Jouer à Monkey Mart – Guide Complet pour Débutants 2026",
            "desc": "Apprenez à jouer à Monkey Mart avec notre guide complet. Contrôles, mécaniques, améliorations et stratégies expliqués étape par étape.",
            "h1": "📖 Comment Jouer à Monkey Mart – Guide Complet",
            "hero_p": "Tout ce que vous devez savoir pour maîtriser Monkey Mart, des contrôles de base aux stratégies avancées.",
            "btn": "▶ Jouer à Monkey Mart Maintenant",
        },
        "tips": {
            "title": "Astuces Monkey Mart – Meilleures Stratégies pour Gagner Plus Vite",
            "desc": "Les meilleures astuces et conseils de Monkey Mart pour gagner des pièces plus vite et construire le supermarché ultime.",
            "h1": "💡 Astuces et Conseils Monkey Mart",
            "hero_p": "Maximisez vos pièces, débloquez les améliorations plus vite et construisez le supermarché le plus efficace avec ces stratégies éprouvées.",
            "btn": "▶ Appliquer Ces Astuces Maintenant",
        },
        "unblocked": {
            "title": "Monkey Mart Débloqué – Jouez à l'École ou au Travail",
            "desc": "Jouez à Monkey Mart débloqué à l'école ou au travail. Notre version est hébergée sur un domaine séparé, accessible sur les réseaux restreints.",
            "h1": "🔓 Monkey Mart Débloqué",
            "hero_p": "Bloqué à l'école ou au travail ? Jouez à Monkey Mart débloqué directement ici. Sans VPN, sans extensions.",
            "btn": "▶ Jouer Débloqué Maintenant",
        },
    },
    "de": {
        "lang": "de", "dir": "de",
        "home": "Startseite", "unblocked": "Entsperrt", "how_to_play": "Anleitung", "tips": "Tipps",
        "unblocked_slug": "monkey-mart-entsperrt",
        "howto_slug": "monkey-mart-anleitung",
        "tips_slug": "monkey-mart-tipps",
        "index": {
            "title": "Monkey Mart – Kostenlos Online Spielen (2026) | MonkeyMartHub",
            "desc": "Spiele Monkey Mart kostenlos online! Führe deinen eigenen Affensupermarkt, ernte Pflanzen und bediene Kunden. Kein Download – sofort im Browser spielen.",
            "h1": "🐒 Monkey Mart – Kostenlos Online Spielen",
            "hero_p": "Führe deinen eigenen Affensupermarkt! Ernte Bananen, fülle Regale und bediene Kunden in diesem süchtig machenden Idle-Spiel. Kein Download, keine Anmeldung.",
            "btn": "▶ Jetzt Spielen – Kostenlos!",
            "loading": "Monkey Mart wird geladen…",
            "caption": "🎮 Benutze WASD oder die Pfeiltasten, um deinen Affen zu bewegen.",
            "what_h2": "Was ist Monkey Mart?",
            "what_p": "<strong>Monkey Mart</strong> ist ein beliebtes Idle-Supermarkt-Simulationsspiel von TinyDobbins. Du steuerst einen Affen, der einen Supermarkt von Grund auf aufbaut: Ernte Pflanzen, fülle Regale und bediene Kunden automatisch.",
            "faq_title": "Häufig Gestellte Fragen",
            "faq": [
                ("Ist Monkey Mart kostenlos?", "Ja! Komplett kostenlos. Kein Download, keine Anmeldung, keine Zahlung."),
                ("Kann ich auf dem Handy spielen?", "Ja. Funktioniert auf iOS und Android mit einem Touch-Joystick auf dem Bildschirm."),
                ("Wer hat Monkey Mart entwickelt?", "Entwickelt von TinyDobbins und ursprünglich auf Poki und CrazyGames veröffentlicht."),
            ],
            "footer_fan": "Monkey Mart ist ein Spiel von TinyDobbins. Diese Website ist eine Fan-Website und steht in keiner Verbindung zum ursprünglichen Entwickler.",
            "privacy": "Datenschutzrichtlinie",
        },
        "howto": {
            "title": "Monkey Mart Anleitung – Vollständiger Leitfaden für Anfänger 2026",
            "desc": "Lerne Monkey Mart mit unserem vollständigen Leitfaden. Steuerung, Mechaniken, Upgrades und Strategien Schritt für Schritt erklärt.",
            "h1": "📖 Monkey Mart Anleitung – Vollständiger Leitfaden",
            "hero_p": "Alles, was du wissen musst, um Monkey Mart zu meistern – von der Grundsteuerung bis zu fortgeschrittenen Strategien.",
            "btn": "▶ Monkey Mart Jetzt Spielen",
        },
        "tips": {
            "title": "Monkey Mart Tipps – Beste Strategien um Schneller zu Verdienen",
            "desc": "Die besten Monkey Mart Tipps und Tricks, um schneller Münzen zu verdienen und den ultimativen Supermarkt aufzubauen.",
            "h1": "💡 Monkey Mart Tipps & Tricks",
            "hero_p": "Maximiere deine Münzen, schalte Upgrades schneller frei und baue den effizientesten Supermarkt mit diesen bewährten Strategien.",
            "btn": "▶ Diese Tipps Jetzt Anwenden",
        },
        "unblocked": {
            "title": "Monkey Mart Entsperrt – In der Schule oder Arbeit Spielen",
            "desc": "Spiele Monkey Mart entsperrt in der Schule oder bei der Arbeit. Unsere Version ist auf einer separaten Domain gehostet, zugänglich in eingeschränkten Netzwerken.",
            "h1": "🔓 Monkey Mart Entsperrt",
            "hero_p": "In der Schule oder bei der Arbeit gesperrt? Spiele Monkey Mart entsperrt direkt hier. Kein VPN, keine Erweiterungen.",
            "btn": "▶ Jetzt Entsperrt Spielen",
        },
    },
}

# ── 长尾词页面数据 ──────────────────────────────────────────
LONGTAIL_PAGES = [
    {
        "slug": "monkey-mart-cheats",
        "title": "Monkey Mart Cheats & Secret Tips – Unlimited Coins Guide 2026",
        "desc": "Looking for Monkey Mart cheats? Discover the best secret tips, hidden tricks, and strategies that work like cheats to get unlimited coins fast.",
        "h1": "🎯 Monkey Mart Cheats & Secret Tips",
        "hero_p": "No cheat codes exist in Monkey Mart — but these secret strategies work just as well. Get unlimited coins faster with these proven tricks.",
        "content": """
        <h2>Are There Real Monkey Mart Cheats?</h2>
        <p>Monkey Mart doesn't have official cheat codes or hacks. However, there are several <strong>legitimate strategies</strong> that dramatically speed up your progress — players call these "cheats" because they feel unfair compared to playing without them.</p>

        <h2>The 5 Best "Cheat" Strategies</h2>
        <h3>1. The Helper Rush (Best Early Game "Cheat")</h3>
        <p>Skip all other upgrades and save every coin for your first helper monkey. Once assigned to bananas, your income doubles instantly. This single strategy puts you 2–3x ahead of players who upgrade randomly.</p>

        <h3>2. The Checkout Exploit</h3>
        <p>Upgrade checkout speed to level 2 before unlocking any new sections. A faster checkout means zero queue time, which translates directly to more coins per minute. Most players ignore this — don't be one of them.</p>

        <h3>3. The Idle Overnight Trick</h3>
        <p>Leave the game running overnight with all helpers assigned. When you wake up, you'll have a massive coin pile to reinvest. This is the closest thing to an "unlimited coins cheat" in the game.</p>

        <h3>4. The Full Shelf Bonus</h3>
        <p>When all shelves are stocked simultaneously, customers spend more. Time your restocking runs to fill all shelves at once and trigger this hidden multiplier bonus.</p>

        <h3>5. The Section Unlock Order</h3>
        <p>Unlock sections in this exact order: Banana → Corn → Dairy → Egg → Chocolate → Ice Cream. This order maximizes income at each stage and is the "cheat code" for fast progression.</p>

        <h2>Best Upgrade Order (Cheat Sheet)</h2>
        <div class="cards">
          <div class="card"><div class="icon">1️⃣</div><h3>Helper Monkey #1</h3><p>Assign to bananas immediately.</p></div>
          <div class="card"><div class="icon">2️⃣</div><h3>Checkout Speed</h3><p>Upgrade to level 2 right away.</p></div>
          <div class="card"><div class="icon">3️⃣</div><h3>Unlock Corn</h3><p>More customers, more income.</p></div>
          <div class="card"><div class="icon">4️⃣</div><h3>Helper Monkey #2</h3><p>Assign to corn section.</p></div>
        </div>
        """,
        "faq": [
            ("Is there a Monkey Mart cheat code?", "No official cheat codes exist. But the strategies above work like cheats — especially the Helper Rush and Idle Overnight trick."),
            ("How do I get unlimited coins in Monkey Mart?", "The fastest way is to hire helpers for all sections and let the game run idle overnight. Your coins accumulate automatically."),
            ("Can I hack Monkey Mart?", "We don't recommend hacking. The strategies above are completely legitimate and get you to the same result faster."),
        ],
    },
    {
        "slug": "monkey-mart-all-items",
        "title": "Monkey Mart All Items & Sections – Complete List 2026",
        "desc": "Complete list of all Monkey Mart items, sections, and products. Bananas, corn, dairy, chocolate, eggs, ice cream and more — unlock order and tips included.",
        "h1": "🛒 Monkey Mart – All Items & Sections Complete List",
        "hero_p": "Every item, section, and product in Monkey Mart explained. Find out what to unlock next and which sections earn the most coins.",
        "content": """
        <h2>All Monkey Mart Sections & Items</h2>
        <p>Monkey Mart has multiple product sections, each unlocked progressively as you earn coins. Here's the complete list in unlock order:</p>

        <h3>🍌 Banana Section (Starting Section)</h3>
        <p><strong>Unlock cost:</strong> Free (starting section)<br>
        <strong>Harvest speed:</strong> Fast<br>
        <strong>Value per item:</strong> Low<br>
        <strong>Tips:</strong> Your bread and butter. Keep this shelf stocked at all times. Assign your first helper monkey here.</p>

        <h3>🌽 Corn Section</h3>
        <p><strong>Unlock cost:</strong> Early game coins<br>
        <strong>Harvest speed:</strong> Medium<br>
        <strong>Value per item:</strong> Medium<br>
        <strong>Tips:</strong> First unlock priority. Doubles your customer variety and income.</p>

        <h3>🥛 Dairy Section</h3>
        <p><strong>Unlock cost:</strong> Mid-game coins<br>
        <strong>Harvest speed:</strong> Medium<br>
        <strong>Value per item:</strong> Medium-High<br>
        <strong>Tips:</strong> Good steady income. Assign a helper as soon as you unlock it.</p>

        <h3>🥚 Egg Section</h3>
        <p><strong>Unlock cost:</strong> Mid-game coins<br>
        <strong>Harvest speed:</strong> Fast<br>
        <strong>Value per item:</strong> Medium<br>
        <strong>Tips:</strong> Fast harvest makes this easy to automate. Great for idle income.</p>

        <h3>🍫 Chocolate Section</h3>
        <p><strong>Unlock cost:</strong> Late-game coins<br>
        <strong>Harvest speed:</strong> Slow<br>
        <strong>Value per item:</strong> High<br>
        <strong>Tips:</strong> High value but slow harvest. Must have a helper assigned to be efficient.</p>

        <h3>🍦 Ice Cream Section</h3>
        <p><strong>Unlock cost:</strong> Late-game coins (highest)<br>
        <strong>Harvest speed:</strong> Medium<br>
        <strong>Value per item:</strong> Very High<br>
        <strong>Tips:</strong> The premium section. Unlocking this is the late-game goal. Assign your best helper here.</p>

        <h2>All Upgrades List</h2>
        <div class="cards">
          <div class="card"><div class="icon">🐒</div><h3>Helper Monkeys</h3><p>One per section. Automates harvesting and stocking. Most important upgrade.</p></div>
          <div class="card"><div class="icon">💳</div><h3>Checkout Speed</h3><p>Multiple levels. Reduces customer wait time. High ROI upgrade.</p></div>
          <div class="card"><div class="icon">🎒</div><h3>Carry Capacity</h3><p>Lets you carry more items per trip. Useful before you have helpers.</p></div>
          <div class="card"><div class="icon">🏪</div><h3>Section Unlocks</h3><p>Each new section adds products and customers. Unlock in order.</p></div>
        </div>
        """,
        "faq": [
            ("How many sections are in Monkey Mart?", "There are 6 main sections: Banana, Corn, Dairy, Egg, Chocolate, and Ice Cream. Each is unlocked progressively."),
            ("What is the best section in Monkey Mart?", "Ice Cream has the highest value per item. But Banana is the most important early on due to its fast harvest speed."),
            ("What is the last item to unlock in Monkey Mart?", "Ice Cream is typically the final premium section to unlock in the base game."),
        ],
    },
    {
        "slug": "monkey-mart-how-to-get-more-monkeys",
        "title": "Monkey Mart – How to Get More Monkeys (Helper Guide 2026)",
        "desc": "Learn exactly how to get more helper monkeys in Monkey Mart. Step-by-step guide to hiring, assigning, and maximizing your monkey helpers for full automation.",
        "h1": "🐒 Monkey Mart – How to Get More Helper Monkeys",
        "hero_p": "Helper monkeys are the key to winning Monkey Mart. Here's exactly how to get them, assign them, and use them to fully automate your store.",
        "content": """
        <h2>What Are Helper Monkeys?</h2>
        <p>Helper monkeys are NPCs you hire to automate specific sections of your supermarket. Once assigned, a helper will independently harvest crops and stock shelves for their section — without any input from you. They are the single most important upgrade in the game.</p>

        <h2>How to Get Your First Helper Monkey</h2>
        <ol>
          <li><strong>Earn enough coins</strong> — The first helper monkey costs a set amount of coins. Focus on keeping shelves stocked to earn coins quickly.</li>
          <li><strong>Open the upgrade menu</strong> — Click on any section or the upgrade icon to open the shop.</li>
          <li><strong>Find "Hire Helper"</strong> — Look for the helper monkey option in the upgrade list for the banana section.</li>
          <li><strong>Purchase and assign</strong> — Once purchased, the helper is automatically assigned to that section and starts working immediately.</li>
        </ol>

        <h2>How Many Helper Monkeys Can You Have?</h2>
        <p>You can have <strong>one helper monkey per section</strong>. Since there are 6 sections (Banana, Corn, Dairy, Egg, Chocolate, Ice Cream), the maximum is <strong>6 helper monkeys</strong> — one for each section. When all 6 are hired, your store runs on full autopilot.</p>

        <h2>Best Order to Hire Helper Monkeys</h2>
        <div class="cards">
          <div class="card"><div class="icon">1️⃣</div><h3>Banana Helper</h3><p>First priority. Frees you from the most repetitive task immediately.</p></div>
          <div class="card"><div class="icon">2️⃣</div><h3>Corn Helper</h3><p>Second priority after unlocking corn section.</p></div>
          <div class="card"><div class="icon">3️⃣</div><h3>Dairy Helper</h3><p>Mid-game. High value section worth automating early.</p></div>
          <div class="card"><div class="icon">4️⃣</div><h3>Remaining Helpers</h3><p>Egg, Chocolate, Ice Cream — in unlock order.</p></div>
        </div>

        <h2>Tips for Maximizing Helper Monkeys</h2>
        <ul>
          <li><strong>Always hire the next helper before unlocking a new section</strong> — Don't spread yourself thin managing too many sections manually.</li>
          <li><strong>Helpers work while you're idle</strong> — Leave the game running and helpers will keep earning coins for you.</li>
          <li><strong>Prioritize high-value sections</strong> — If you have to choose, assign helpers to Chocolate and Ice Cream first for maximum coin generation.</li>
          <li><strong>Full automation is the end goal</strong> — Once all 6 helpers are hired, your only job is collecting coins and buying upgrades.</li>
        </ul>
        """,
        "faq": [
            ("How do I hire a helper monkey in Monkey Mart?", "Click on a section or the upgrade icon, find the 'Hire Helper' option, and purchase it with coins. The helper is automatically assigned to that section."),
            ("How many monkeys can you have in Monkey Mart?", "Up to 6 helper monkeys — one per section. Plus your main monkey that you control directly."),
            ("Do helper monkeys work when I'm not playing?", "Yes! Helper monkeys continue working while the game is idle. This is how you earn coins passively."),
            ("What does a helper monkey do in Monkey Mart?", "A helper monkey automatically harvests crops and stocks shelves for their assigned section, removing the need for manual management."),
        ],
    },
]

# ── HTML 模板函数 ──────────────────────────────────────────

HREFLANG_BLOCK = """  <link rel="alternate" hreflang="en" href="https://monkeymarthub.com/" />
  <link rel="alternate" hreflang="es" href="https://monkeymarthub.com/es/" />
  <link rel="alternate" hreflang="pt" href="https://monkeymarthub.com/pt/" />
  <link rel="alternate" hreflang="fr" href="https://monkeymarthub.com/fr/" />
  <link rel="alternate" hreflang="de" href="https://monkeymarthub.com/de/" />
  <link rel="alternate" hreflang="x-default" href="https://monkeymarthub.com/" />"""

def ga_block():
    return """  <script async src="https://www.googletagmanager.com/gtag/js?id=G-1SY7GENFYR"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', 'G-1SY7GENFYR');
  </script>"""

def faq_html(items):
    out = ""
    for q, a in items:
        out += f"  <details>\n    <summary>{q}</summary>\n    <p>{a}</p>\n  </details>\n"
    return out

def game_script():
    return """<script>
function centerOnGame() {
  var w = document.getElementById('gameWrapper');
  var r = w.getBoundingClientRect();
  window.scrollTo({ top: window.pageYOffset + r.top - Math.max(0,(window.innerHeight-r.height)/2), behavior:'smooth' });
}
function scrollToGame(e) { e.preventDefault(); centerOnGame(); }
function loadGame() {
  document.getElementById('gameCover').style.display='none';
  document.getElementById('gameLoading').style.display='flex';
  document.getElementById('gameFrame').style.display='block';
  setTimeout(centerOnGame,60);
  var f=document.createElement('iframe');
  f.src='https://monkey-mart.io/iframe/index.html';
  f.title='Monkey Mart';
  f.allow='autoplay; fullscreen *; payment';
  f.allowFullscreen=true;
  f.setAttribute('sandbox','allow-forms allow-modals allow-orientation-lock allow-pointer-lock allow-popups allow-popups-to-escape-sandbox allow-presentation allow-scripts allow-same-origin');
  f.style.cssText='position:absolute;inset:0;width:100%;height:100%;border:none;';
  f.onload=function(){document.getElementById('gameLoading').style.display='none';};
  setTimeout(function(){document.getElementById('gameLoading').style.display='none';},15000);
  document.getElementById('gameFrame').appendChild(f);
}
</script>"""

def build_index(lang_code, d):
    t = d["index"]
    us = d["unblocked_slug"]
    hs = d["howto_slug"]
    ts = d["tips_slug"]
    base = f"/{lang_code}/"
    return f"""<!DOCTYPE html>
<html lang="{lang_code}">
<head>
  <meta charset="UTF-8" />
{ga_block()}
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{t['title']}</title>
  <meta name="description" content="{t['desc']}" />
  <link rel="canonical" href="https://monkeymarthub.com/{lang_code}/" />
  <meta name="robots" content="index, follow" />
{HREFLANG_BLOCK}
  <link rel="icon" type="image/x-icon" href="/favicon.ico" />
  <link rel="icon" type="image/svg+xml" href="/favicon.svg" />
  <meta name="theme-color" content="#2d7a2d" />
  <link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png" />
  <meta property="og:type" content="website" />
  <meta property="og:title" content="{t['title']}" />
  <meta property="og:description" content="{t['desc']}" />
  <meta property="og:url" content="https://monkeymarthub.com/{lang_code}/" />
  <meta property="og:image" content="https://monkeymarthub.com/og-image.png" />
  <link rel="preload" as="image" href="/cover-bg.jpg" fetchpriority="high" />
  <link rel="stylesheet" href="/style.css?v=3" />
</head>
<body>
<header>
  <a class="logo" href="{base}">🐒 MonkeyMartHub</a>
  <nav>
    <a href="{base}">{d['home']}</a>
    <a href="{base}{us}">{d['unblocked']}</a>
    <a href="{base}{hs}">{d['how_to_play']}</a>
    <a href="{base}{ts}">{d['tips']}</a>
  </nav>
</header>
<section class="hero">
  <h1>{t['h1']}</h1>
  <p>{t['hero_p']}</p>
  <a href="#play" class="btn-play" onclick="scrollToGame(event)">{t['btn']}</a>
</section>
<section class="game-section" id="play">
  <div class="game-wrapper" id="gameWrapper">
    <div class="game-cover" id="gameCover" onclick="loadGame()">
      <div class="cover-content">
        <div class="cover-title">Monkey Mart</div>
        <div class="cover-meta"><span>⭐ 4.7 / 5</span><span>🎮 No Download</span><span>📱 Mobile Ready</span></div>
        <button class="cover-play-btn"><svg viewBox="0 0 24 24" fill="currentColor" width="28" height="28"><path d="M8 5v14l11-7z"/></svg>{t['btn']}</button>
      </div>
    </div>
    <div class="game-loading" id="gameLoading" style="display:none"><div class="spinner"></div><p>{t['loading']}</p></div>
    <div id="gameFrame" style="position:absolute;inset:0;display:none"></div>
  </div>
  <p class="game-caption">{t['caption']}</p>
</section>
{game_script()}
<div class="content">
  <h2>{t['what_h2']}</h2>
  <p>{t['what_p']}</p>
</div>
<section class="faq">
  <h2>{t['faq_title']}</h2>
{faq_html(t['faq'])}</section>
<section class="related">
  <div class="related-grid">
    <a class="related-card" href="{base}{hs}"><div class="r-icon">📖</div><div class="r-name">{d['how_to_play']}</div></a>
    <a class="related-card" href="{base}{ts}"><div class="r-icon">💡</div><div class="r-name">{d['tips']}</div></a>
    <a class="related-card" href="{base}{us}"><div class="r-icon">🔓</div><div class="r-name">{d['unblocked']}</div></a>
    <a class="related-card" href="/"><div class="r-icon">🌐</div><div class="r-name">English</div></a>
  </div>
</section>
<footer>
  <p>© 2026 MonkeyMartHub.com &nbsp;|&nbsp; <a href="/privacy">{t['privacy']}</a> &nbsp;|&nbsp; <a href="/sitemap.xml">Sitemap</a></p>
  <p style="margin-top:8px;font-size:.8rem;opacity:.7">{t['footer_fan']}</p>
</footer>
</body>
</html>"""

def build_subpage(lang_code, d, page_key, slug, breadcrumb_name):
    t = d[page_key]
    base = f"/{lang_code}/"
    us = d["unblocked_slug"]
    hs = d["howto_slug"]
    ts = d["tips_slug"]
    return f"""<!DOCTYPE html>
<html lang="{lang_code}">
<head>
  <meta charset="UTF-8" />
{ga_block()}
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{t['title']}</title>
  <meta name="description" content="{t['desc']}" />
  <link rel="canonical" href="https://monkeymarthub.com/{lang_code}/{slug}" />
  <meta name="robots" content="index, follow" />
{HREFLANG_BLOCK}
  <link rel="icon" type="image/x-icon" href="/favicon.ico" />
  <link rel="icon" type="image/svg+xml" href="/favicon.svg" />
  <meta name="theme-color" content="#2d7a2d" />
  <meta property="og:type" content="article" />
  <meta property="og:title" content="{t['title']}" />
  <meta property="og:description" content="{t['desc']}" />
  <meta property="og:url" content="https://monkeymarthub.com/{lang_code}/{slug}" />
  <meta property="og:image" content="https://monkeymarthub.com/og-image.png" />
  <link rel="stylesheet" href="/style.css?v=3" />
</head>
<body>
<header>
  <a class="logo" href="{base}">🐒 MonkeyMartHub</a>
  <nav>
    <a href="{base}">{d['home']}</a>
    <a href="{base}{us}">{d['unblocked']}</a>
    <a href="{base}{hs}">{d['how_to_play']}</a>
    <a href="{base}{ts}">{d['tips']}</a>
  </nav>
</header>
<div class="breadcrumb"><a href="{base}">{d['home']}</a> › {breadcrumb_name}</div>
<section class="hero">
  <h1>{t['h1']}</h1>
  <p>{t['hero_p']}</p>
  <a href="{base}" class="btn-play">{t['btn']}</a>
</section>
<div class="content">
  <p><em>→ <a href="{base}">{d['home']}</a> | <a href="{base}{hs}">{d['how_to_play']}</a> | <a href="{base}{ts}">{d['tips']}</a></em></p>
</div>
<footer>
  <p>© 2026 MonkeyMartHub.com &nbsp;|&nbsp; <a href="/privacy">Privacy</a> &nbsp;|&nbsp; <a href="/sitemap.xml">Sitemap</a></p>
</footer>
</body>
</html>"""

def build_longtail(page):
    faq_html_str = ""
    for q, a in page["faq"]:
        faq_html_str += f"  <details>\n    <summary>{q}</summary>\n    <p>{a}</p>\n  </details>\n"

    schema_faq = json.dumps({
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in page["faq"]
        ]
    }, ensure_ascii=False, indent=2)

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
{ga_block()}
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{page['title']}</title>
  <meta name="description" content="{page['desc']}" />
  <link rel="canonical" href="https://monkeymarthub.com/{page['slug']}" />
  <meta name="robots" content="index, follow" />
  <link rel="icon" type="image/x-icon" href="/favicon.ico" />
  <link rel="icon" type="image/svg+xml" href="/favicon.svg" />
  <meta name="theme-color" content="#2d7a2d" />
  <meta property="og:type" content="article" />
  <meta property="og:title" content="{page['title']}" />
  <meta property="og:description" content="{page['desc']}" />
  <meta property="og:url" content="https://monkeymarthub.com/{page['slug']}" />
  <meta property="og:image" content="https://monkeymarthub.com/og-image.png" />
  <script type="application/ld+json">
  {schema_faq}
  </script>
  <link rel="stylesheet" href="/style.css?v=3" />
</head>
<body>
<header>
  <a class="logo" href="/">🐒 MonkeyMartHub</a>
  <nav>
    <a href="/">Home</a>
    <a href="/monkey-mart-unblocked">Unblocked</a>
    <a href="/how-to-play-monkey-mart">How to Play</a>
    <a href="/monkey-mart-tips">Tips</a>
  </nav>
</header>
<div class="breadcrumb"><a href="/">Home</a> › {page['h1']}</div>
<section class="hero">
  <h1>{page['h1']}</h1>
  <p>{page['hero_p']}</p>
  <a href="/" class="btn-play">▶ Play Monkey Mart Free</a>
</section>
<div class="content">
{page['content']}
</div>
<section class="faq">
  <h2>Frequently Asked Questions</h2>
{faq_html_str}</section>
<section class="related">
  <h2>More Resources</h2>
  <div class="related-grid">
    <a class="related-card" href="/"><div class="r-icon">🐒</div><div class="r-name">Play Monkey Mart</div><div class="r-kd">Free online game</div></a>
    <a class="related-card" href="/monkey-mart-tips"><div class="r-icon">💡</div><div class="r-name">Tips & Tricks</div><div class="r-kd">Advanced strategies</div></a>
    <a class="related-card" href="/how-to-play-monkey-mart"><div class="r-icon">📖</div><div class="r-name">How to Play</div><div class="r-kd">Beginner guide</div></a>
    <a class="related-card" href="/monkey-mart-all-items"><div class="r-icon">🛒</div><div class="r-name">All Items</div><div class="r-kd">Complete list</div></a>
  </div>
</section>
<footer>
  <p>© 2026 MonkeyMartHub.com &nbsp;|&nbsp; <a href="/privacy">Privacy Policy</a> &nbsp;|&nbsp; <a href="/sitemap.xml">Sitemap</a></p>
  <p style="margin-top:8px;font-size:.8rem;opacity:.7">Monkey Mart is a game by TinyDobbins. This site is a fan site and is not affiliated with the original developer.</p>
</footer>
</body>
</html>"""

# ── 生成所有文件 ──────────────────────────────────────────
generated = []

# 1. 多语言页面
for lang_code, d in LANGS.items():
    lang_dir = os.path.join(BASE, lang_code)
    os.makedirs(lang_dir, exist_ok=True)

    # 首页
    path = os.path.join(lang_dir, "index.html")
    with open(path, "w", encoding="utf-8") as f:
        f.write(build_index(lang_code, d))
    generated.append(f"/{lang_code}/")

    # 子页面
    subpages = [
        ("howto", d["howto_slug"], d["how_to_play"]),
        ("tips",  d["tips_slug"],  d["tips"]),
        ("unblocked", d["unblocked_slug"], d["unblocked"]),
    ]
    for page_key, slug, breadcrumb in subpages:
        path = os.path.join(lang_dir, f"{slug}.html")
        with open(path, "w", encoding="utf-8") as f:
            f.write(build_subpage(lang_code, d, page_key, slug, breadcrumb))
        generated.append(f"/{lang_code}/{slug}")

# 2. 长尾词页面
for page in LONGTAIL_PAGES:
    path = os.path.join(BASE, f"{page['slug']}.html")
    with open(path, "w", encoding="utf-8") as f:
        f.write(build_longtail(page))
    generated.append(f"/{page['slug']}")

print(f"✅ 生成完成！共 {len(generated)} 个页面：")
for p in generated:
    print(f"  {p}")
