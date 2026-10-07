from pathlib import Path
import json
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, KeepTogether, Table, TableStyle
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from xml.sax.saxutils import escape

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'docs/Eugenio_Piga_CV.pdf'
FONT=Path('C:/Windows/Fonts')
for name,file in [('Body','arial.ttf'),('BodyBold','arialbd.ttf'),('BodyItalic','ariali.ttf'),('Display','georgia.ttf')]:
    pdfmetrics.registerFont(TTFont(name,str(FONT/file)))
pdfmetrics.registerFontFamily('Body',normal='Body',bold='BodyBold',italic='BodyItalic',boldItalic='BodyBold')
INK=HexColor('#192e38'); MUTED=HexColor('#53636a'); ACCENT=HexColor('#185c55')
styles={
'name':ParagraphStyle('name',fontName='Display',fontSize=28,leading=33,textColor=INK,spaceAfter=7),
'contact':ParagraphStyle('contact',fontName='Body',fontSize=8.7,leading=12,textColor=MUTED,spaceAfter=4),
'section':ParagraphStyle('section',fontName='BodyBold',fontSize=9.4,leading=12,textColor=ACCENT,spaceBefore=10,spaceAfter=6,keepWithNext=True),
'body':ParagraphStyle('body',fontName='Body',fontSize=9,leading=11.7,textColor=INK,spaceAfter=4),
'small':ParagraphStyle('small',fontName='Body',fontSize=8.3,leading=10.4,textColor=MUTED,spaceAfter=4),
'entry':ParagraphStyle('entry',fontName='Body',fontSize=9,leading=11.7,textColor=INK,spaceAfter=1),
}
story=[]
def p(s,style='body'): return Paragraph(s,styles[style])
def section(s): story.append(p(s.upper(),'section'))
def entry(title, detail='', date=''):
    row=Table([[p('<b>'+title+'</b>','entry'),p(date,'small')]],colWidths=[390,100],hAlign='LEFT')
    row.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),0),('RIGHTPADDING',(0,0),(-1,-1),0),('TOPPADDING',(0,0),(-1,-1),0),('BOTTOMPADDING',(0,0),(-1,-1),0)]))
    elements=[row]
    if detail: elements.append(p(detail,'small'))
    elements.append(Spacer(1,2))
    story.append(KeepTogether(elements))

story += [p('Eugenio Piga','name'),p('Ph.D. Student in Economics · University of California, San Diego','contact'),p('<link href="mailto:epiga@ucsd.edu" color="#185c55">epiga@ucsd.edu</link> · +1 (858) 373-8865 · <link href="https://eugeniopiga.github.io/" color="#185c55">eugeniopiga.github.io</link>','contact')]
section('Research interests')
story.append(p('Macroeconomics; Labor Economics; Innovation; Artificial Intelligence'))
section('Education')
entry('University of California, San Diego','Ph.D. in Economics · San Diego, USA','2024-present')
entry('Bocconi University','M.Sc. in Economics and Finance · Milan, Italy<br/>Thesis: “Modeling Salience, Stereotypes, and Social Identity in Financial Markets”<br/>Advisor: Nicola Gennaioli','2022')
entry('Bocconi University','B.Sc. in Computer Science and Economics · Milan, Italy<br/>Thesis: “Heterogeneous Borrowing and COVID-19 Monetary Policies”<br/>Advisor: Luigi Iovino','2020')
section('Work in progress')
for project in json.loads((ROOT/'scripts/projects.json').read_text(encoding='utf-8')):
    story.append(KeepTogether([p('<b>'+escape(project['title'])+'</b>','entry')]+([p(escape(project['authors']),'small')] if project['authors'] else [Spacer(1,6)])))
story.append(p('<b>BEA-BLS Accounts and the NBER-CES Manufacturing Database: The Productivity Gap</b><br/>with John Fernald'))
section('Publications')
story.append(p('<b>Comment on “Bottlenecks: Sectoral Imbalances and the US Productivity Slowdown”</b><br/>with John G. Fernald. <i>NBER Macroeconomics Annual 2023</i>, Vol. 38, pp. 208-221. Published 2024. <link href="https://doi.org/10.1086/729203" color="#185c55">Article</link>'))
story.append(p('<b>Comment on “Bottlenecks: Sectoral Imbalances and the US Productivity Slowdown”</b><br/>with Jennifer La’O. <i>NBER Macroeconomics Annual 2023</i>, Vol. 38, pp. 222-235. Published 2024. <link href="https://doi.org/10.1086/729204" color="#185c55">Article</link>'))
section('Research positions')
entry('INSEAD','Pre-doctoral Research Associate, Economics and Political Science · Fontainebleau, France','2022-2024')
entry('Bocconi University','Pre-doctoral Research Associate, Department of Economics · Milan, Italy','2021-2022')
entry('Bocconi University, IGIER','Visiting Student · Milan, Italy','2019-2021')
entry('Shanghai Advanced Institute of Finance','Visiting Student · Shanghai, China','2022')
story.append(PageBreak())
section('Teaching')
for title,info,date in [
('LIIT 1AX - Analysis of Italian','UC San Diego · Italian language instruction · Chiara Carnelos','Fall 2026'),
('ECON 112 - Macroeconomic Data Analysis','UC San Diego · Undergraduate TA · Giacomo Rondina','2026'),
('ECON 86 - 10×10 Career Lessons','UC San Diego · Undergraduate TA · Marc Muendler','2026'),
('ECON 210B - Macroeconomics','UC San Diego · Ph.D. TA · Giacomo Rondina','Winter 2026'),
('ECON 110B - Short-Run Macroeconomics','UC San Diego · Undergraduate TA · Fabian Trottner','Fall 2025'),
('Business and Society','INSEAD · Graduate TA · Philippe Aghion','2022-2023'),
('Prices and Markets','INSEAD · MBA TA · Timothy Van Zandt','2022-2023'),
('Theory of Finance','Bocconi University · Graduate TA · Carlo Favero and Claudio Tebaldi','2020-2021')]: entry(title,info,date)
section('Presentations and conference participation')
story.append(p('<b>Upcoming presentations:</b> CODE@MIT, poster and flash talk (November 2026); UC San Diego Macro and Labor workshops (October 2026).'))
story.append(p('<b>2026:</b> Atkinson Conference on Economic and Social Inequality, Nuffield College, Oxford (presentation); AI &amp; Economics Summer Conference, University of Chicago (presentation); UC San Diego Macro Seminar Series; JIE Summer School in International Economics, Bocconi University (attendance).'))
story.append(p('<b>2025:</b> AI+Economics Summer Institute and Machine Learning in Economics Summer Conference, University of Chicago (participation).'))
story.append(p('<b>2023:</b> NBER 38th Annual Conference on Macroeconomics; XVIII Seminario Internacional del Boletín Informativo Techint.'))
section('Awards and honors')
story.append(p('Regents Fellowship, UC San Diego (2024-2026); France Excellence Eiffel Scholarship, French Ministry of Foreign Affairs (2024); Distinction in Master’s Thesis, Bocconi (2022); PerTe Prestito con Lode Grant, Banca Intesa Sanpaolo (2018-2022); International Mobility Award, Bocconi (2021); Teaching Improvement Award, Bocconi (2021); Distinction in Bachelor’s Thesis, Bocconi (2020); National Registry of Excellence, Italian Ministry of Education (2017).'))
section('Other writings')
story.append(p('Timothy Van Zandt, <i>Firms, Prices, and Markets</i>, MBA managerial economics textbook. Contributor to chapters on firm decision-making and market design.','small'))
story.append(p('<i>Social Media, Sentiment, and Investments: NLP and Network Analysis of Twitter Data.</i> Shanghai Jiao Tong University Master’s Project, 2022.','small'))
story.append(p('<i>From Daniel Defoe’s Coffee Houses to GameStop’s Livestreaming Platforms: Investors Are Not Rational.</i> Comment on “Behavioural Finance and Markets Efficiency: Is There a Dialogue?” <i>Law and Economics Yearly Review</i>, Vol. 5, Part 2.','small'))
section('Affiliations and skills')
story.append(p('Computational Social Sciences Affiliate, UC San Diego (2025-2026); IGIER (2019-2021).<br/><b>Programming:</b> Python, R, Stata, MATLAB, Julia, SQL.<br/><b>Languages:</b> Italian, English, French, Spanish.','small'))

def footer(c,doc):
    c.saveState(); w,h=doc.pagesize
    c.setStrokeColor(HexColor('#d7ddd9'));c.setLineWidth(.5);c.line(52,42,w-52,42)
    c.setFont('Body',7.3);c.setFillColor(MUTED)
    c.drawString(52,29,'Eugenio Piga · Curriculum Vitae')
    c.drawCentredString(w/2,29,'Updated October 2026')
    c.drawRightString(w-52,29,str(doc.page));c.restoreState()
doc=SimpleDocTemplate(str(OUT),pagesize=(612,792),leftMargin=52,rightMargin=52,topMargin=36,bottomMargin=50,title='Eugenio Piga - Curriculum Vitae',author='Eugenio Piga')
doc.build(story,onFirstPage=footer,onLaterPages=footer)
from pypdf import PdfReader
r=PdfReader(OUT)
print(f'Created CV: {len(r.pages)} pages')
for i,pg in enumerate(r.pages): print(f'Page {i+1}: {len(pg.extract_text().split())} words')
