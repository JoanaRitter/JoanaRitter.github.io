import re

def translate_html():
    with open('en.html', 'r', encoding='utf-8') as f:
        content = f.read()

    replacements = {
        r'lang="pt-BR"': r'lang="en"',
        r'<title>Joana Ritter \| Senior Product Designer</title>': r'<title>Joana Ritter | Senior Product Designer</title>',
        r'content="Portfólio de Joana Ritter, Product Designer focada em produtos digitais complexos e orientados por IA."': r'content="Portfolio of Joana Ritter, Product Designer focused on complex and AI-driven digital products."',
        r'<li><a href="#about">Sobre</a></li>': r'<li><a href="#about">About</a></li>',
        r'<li><a href="#experience">Experiência</a></li>': r'<li><a href="#experience">Experience</a></li>',
        r'<li><a href="#education">Formação</a></li>': r'<li><a href="#education">Education</a></li>',
        r'<li><a href="#media">Impacto e Mídia</a></li>': r'<li><a href="#media">Impact & Media</a></li>',
        r'<li><a href="#contact">Contato</a></li>': r'<li><a href="#contact">Contact</a></li>',
        
        r'<p class="greeting">Olá, eu sou a</p>': r'<p class="greeting">Hi, I am</p>',
        r'<span class="gradient-text">focada em IA & Produtos\s+Complexos</span>': r'<span class="gradient-text">focused on AI & Complex Products</span>',
        
        r'Especializada em produtos digitais complexos e ecossistemas orientados por IA\. Com histórico no\s+setor financeiro e tecnologia \(XP Inc, TOTVS, Vindi, Banco Original\), conecto pesquisa e dados\s+para escalar decisões de produto, equilibrando negócio e tecnologia\.': r'Specialized in complex digital products and AI-driven ecosystems. With a background in finance and tech (XP Inc, TOTVS, Vindi, Banco Original), I connect research and data to scale product decisions, balancing business and technology.',
        
        r'<span class="tag">Design Estratégico</span>': r'<span class="tag">Strategic Design</span>',
        r'<a href="#contact" class="btn btn-primary">Vamos conversar</a>': r'<a href="#contact" class="btn btn-primary">Let\'s talk</a>',
        r'<a href="#experience" class="btn btn-secondary">Ver minha trajetória</a>': r'<a href="#experience" class="btn btn-secondary">View my journey</a>',
        
        r'<h3 class="section-title">Sobre Mim</h3>': r'<h3 class="section-title">About Me</h3>',
        r'Product Designer focada em produtos digitais complexos e orientados por IA, ajudando times a\s+reduzir incertezas e tomar decisões melhores ao conectar pesquisa com usuários, dados,\s+contexto de negócio e tecnologia\.': r'Product Designer focused on complex digital products and AI, helping teams reduce uncertainties and make better decisions by connecting research with users, data, business context, and technology.',
        
        r'<span class="skill-item">Discovery de Produto</span>': r'<span class="skill-item">Product Discovery</span>',
        r'<span class="skill-item">Arquitetura da Informação</span>': r'<span class="skill-item">Information Architecture</span>',
        r'<span class="skill-item">Design de Interação</span>': r'<span class="skill-item">Interaction Design</span>',
        r'<span class="skill-item">UX Conversacional</span>': r'<span class="skill-item">Conversational UX</span>',
        r'<span class="skill-item">Design de Produtos com IA</span>': r'<span class="skill-item">AI Product Design</span>',
        r'<span class="skill-item">Testes de Usabilidade</span>': r'<span class="skill-item">Usability Testing</span>',
        r'<span class="skill-item">Estratégia de Design</span>': r'<span class="skill-item">Design Strategy</span>',
        
        r'<h4 class="small-title">Reconhecimentos & Certificações</h4>': r'<h4 class="small-title">Awards & Certifications</h4>',
        r'<strong>Campeã Mundial</strong>': r'<strong>Global Winner</strong>',
        r'<strong>Speaker - EducaXperience 2024</strong>': r'<strong>Speaker - EducaXperience 2024</strong>',
        r'<span>Palestrante em grande evento de educação e tech</span>': r'<span>Speaker at major education and tech event</span>',
        r'<strong>Finalista</strong>': r'<strong>Finalist</strong>',
        
        r'<h3 class="section-title">Cases & Portfólio</h3>': r'<h3 class="section-title">Cases & Portfolio</h3>',
        r'Conheça alguns dos projetos e experiências onde atuei, conectando design, tecnologia e as necessidades do negócio\.': r'Discover some of the projects and experiences I have worked on, connecting design, technology, and business needs.',
        r'Em Breve': r'Coming Soon',
        r'Transformação Digital e UX': r'Digital Transformation and UX',
        r'Estratégia de produto e design system para ecossistema enterprise\.': r'Product strategy and design system for enterprise ecosystem.',
        r'Design Orientado a Dados \(AI\)': r'Data-Driven Design (AI)',
        r'Uso de inteligência artificial para otimização de fluxos\.': r'Use of artificial intelligence to optimize workflows.',
        r'Experiência Financeira \(Fintech\)': r'Financial Experience (Fintech)',
        r'Redesenho da jornada de pagamentos B2B diminuindo atrito\.': r'Redesign of B2B payment journey decreasing friction.',
        
        r'<h3 class="section-title">Experiência Profissional</h3>': r'<h3 class="section-title">Professional Experience</h3>',
        r'Atual': r'Present',
        r'Maio': r'May',
        r'Agosto': r'August',
        r'Abril': r'April',
        r'Outubro': r'October',
        r'Anterior': r'Previous',
        
        r'Lidero o design end-to-end do Programa Júpiter, focado em ecossistemas enterprise\s+complexos\. Atuo na descoberta da solução e entrega em alta fidelidade, equilibrando as\s+necessidades de negócios com tecnologia, em grande escala e impacto para milhares de\s+usuários B2B\.': r'I lead the end-to-end design of the Jupiter Program, focusing on complex enterprise ecosystems. I act in solution discovery and high-fidelity delivery, balancing business needs with technology, at scale and impact for thousands of B2B users.',

        r'Design de experi[^<]+cias centradas no usuário para os sistemas de pagamento e POS da\s+marca, em um ambiente altamente engajado e regulado \(Bacen\), estruturando decisões\s+orientadas por m[^<]+tricas de adoção e satisfação no mercado\.': r'Design of user-centered experiences for the brand\'s payment systems and POS in a highly engaged and regulated environment (Bacen), structuring decisions driven by adoption metrics and market satisfaction.',

        r'Liderei a definição e construção da estratégia da <a href="#" class="inline-link">Nova\s+Home e Menu do App de Investimentos da XP</a>, criando soluções intuitivas a partir\s+de regras complexas do mercado e consolidando uma experiência segura e fácil para os\s+investidores \(B2C\)\.': r'Led the definition and construction of the strategy for the <a href="#" class="inline-link">New Home and Menu of XP\'s Investment App</a>, creating intuitive solutions from complex market rules and consolidating a secure and easy experience for investors (B2C).',

        r'Atuação focada na estruturação da experiência bancária com forte inovação para o primeiro\s+banco 100% digital do Brasil\.': r'Focused on structuring the banking experience with strong innovation for the first 100% digital bank in Brazil.',

        r'<h3 class="section-title">Formação Acadêmica</h3>': r'<h3 class="section-title">Academic Background</h3>',
        r'Pós-Graduação em Arquitetura da Informação e UX': r'Postgraduate Certificate in Information Architecture and UX',
        r'Especialização em Arquitetura da Informação e UX': r'Specialization in Information Architecture and UX',
        r'Licenciatura em Pedagogia': r'Bachelor\'s Degree in Pedagogy',
        
        r'<h3 class="section-title">Impacto & Mídia</h3>': r'<h3 class="section-title">Impact & Media</h3>',
        r'Destaque\s+Global': r'Global\nHighlight',
        r'Campeã Mundial do Hackathon\s+da NASA': r'NASA Hackathon Global Winner',
        r'Co-criadora de uma Inteligência Artificial capaz de detectar manchas de óleo no oceano\. O\s+projeto foi o vencedor global do <strong>NASA Space Apps Challenge</strong>, superando\s+milhares de equipes ao redor do mundo e gerando grande repercussão na imprensa nacional e\s+internacional\.': r'Co-creator of an Artificial Intelligence capable of detecting oil spills in the ocean. The project was the global winner of the <strong>NASA Space Apps Challenge</strong>, overcoming thousands of teams worldwide and generating great repercussion in the national and international press.',
        
        r'Cobertura na Mídia - Projeto NASA': r'Media Coverage - NASA Project',
        r'Leia a reportagem': r'Read the article',
        r'O squad da ciência contra o óleo no mar': r'The science squad against oil at sea',
        r'Mogiana desenvolve IA e vence concurso': r'Mogi native develops AI and wins contest',
        r'Brasileiros recebem prêmio da NASA': r'Brazilians receive NASA award',
        r'Ganham concurso de soluções tecnológicas': r'Winners of technological solutions contest',
        r'Premiação por projeto de Inteligência Artificial': r'Award for Artificial Intelligence project',
        
        r'Maratona\s+& Minissérie': r'Marathon\n& Miniseries',
        r'Fui, por duas vezes, uma das <strong>Top 100 finalistas</strong> da Maratona Behind The Code\s+da IBM, na qual competiram mais de 70\.000 desenvolvedores e designers por toda a América\s+Latina\. Essa jornada deu origem à minissérie documental <strong>C0D3RS\s+Championship</strong>, disponível no Prime Video, que promove o impacto da tecnologia e\s+inovação na região\.': r'I was twice one of the <strong>Top 100 finalists</strong> of the IBM Behind The Code Marathon, in which more than 70,000 developers and designers competed across Latin America. This journey gave rise to the documentary miniseries <strong>C0D3RS Championship</strong>, available on Prime Video, which promotes the impact of technology and innovation in the region.',
        
        r'Assista à Minissérie C0D3RS': r'Watch the C0D3RS Miniseries',
        r'A primeira minissérie tech da América Latina': r'The first tech miniseries in Latin America',
        r'Leia a reportagem no IBM Newsroom': r'Read the article in IBM Newsroom',
        
        r'Podcasts & Entrevistas': r'Podcasts & Interviews',
        r'Como a Tecnologia nos levou à Nasa\?': r'How Technology took us to NASA?',
        r'Hackathons, NASA e Manchas de Óleo': r'Hackathons, NASA and Oil Spills',
        r'Participação e Entrevista': r'Participation and Interview',
        r'Assista no YouTube': r'Watch on YouTube',
        r'Bate-papo: Design & Carreira': r'Chat: Design & Career',
        r'Talk e Apresentação': r'Talk and Presentation',
        r'Participação Especial': r'Special Participation',
        r'Design e Produtos Digitais': r'Design and Digital Products',
        
        r'<h3 class="section-title">Vamos criar algo incrível juntos\?</h3>': r'<h3 class="section-title">Let\'s create something amazing together?</h3>',
        r'Estou sempre aberta a conversar sobre design, tecnologia e novas oportunidades\.': r'I am always open to chatting about design, technology, and new opportunities.',
        
        r'Todos os direitos reservados\.': r'All rights reserved.'

    }
    
    for pt, en in replacements.items():
        content = re.sub(pt, en, content, flags=re.MULTILINE)
        
    with open('en.html', 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == '__main__':
    translate_html()
